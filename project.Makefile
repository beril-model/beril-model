## Add your own custom Makefile targets here

RUN = poetry run

.PHONY: check-jsonschema-example run-linkml-validation check-all-invalid-examples check-all-valid-examples

JSON_SCHEMA_FILE := project/jsonschema/beril_model.schema.json
INVALID_EXAMPLES_DIR := src/data/examples/invalid
INVALID_EXAMPLE_FILES := $(wildcard src/data/examples/invalid/*.yaml)
VALID_EXAMPLES_DIR := src/data/examples/valid
VALID_EXAMPLE_FILES := $(wildcard src/data/examples/valid/*.yaml)

# the check-jsonschema utility can be used to check JSON or YAML data
#  against the JSON schema generated from teh LinkML schema
# Future versions of LinkML will include reporting of all errors like check-jsonschema
#  at which time these tests will be rewritten
# see https://github.com/turbomam/examples-first-cookiecutter/issues/99

jsonschema-check-all-examples: check-all-invalid-examples check-all-valid-examples

check-all-invalid-examples: $(patsubst $(INVALID_EXAMPLES_DIR)/%.yaml,jsonschema-vs-invalid--%,$(INVALID_EXAMPLE_FILES))

jsonschema-vs-invalid--%: $(JSON_SCHEMA_FILE) $(INVALID_EXAMPLES_DIR)/%.yaml
	! $(RUN) check-jsonschema --schemafile $^

check-all-valid-examples: $(patsubst $(VALID_EXAMPLES_DIR)/%.yaml,jsonschema-vs-valid-%,$(VALID_EXAMPLE_FILES))

jsonschema-vs-valid-%: $(JSON_SCHEMA_FILE) $(VALID_EXAMPLES_DIR)/%.yaml
	$(RUN) check-jsonschema --schemafile $^


linkml-validation-confirm-invalid-dupe-ids: src/beril_model/schema/beril_model.yaml \
src/data/examples/unexpected-pass/NamedThingCollection-material_entities-dupe-ids.yaml
	# target-class is inferred from whatever class has the tree_root attribute
	# we could make that more explicit here
	! $(RUN) linkml-validate \
	  --schema $^


src/data/dh_vs_linkml_json/material_entities_linkml_raw.yaml: src/data/dh_vs_linkml_json/material_entities.json
	$(RUN) dh-json2linkml \
		--input-file $< \
		--output-file $@ \
		--output-format yaml \
		--key material_entities


#src/data/dh_vs_linkml_json/material_entities_linkml_normalized.yaml: src/data/dh_vs_linkml_json/material_entities_linkml_raw.yaml
#	# what does or doesn't get normalized?
#	# NotImplementedError
#	$(RUN) linkml-normalize \
#		--schema src/beril_model/schema/beril_model.yaml \
#		--output $@ \
#		--no-expand-all $<

# src/data/examples/valid/NamedThingCollection-material_entities-multiple-materials.yaml
# data/examples/valid/NamedThingCollection-processes-with-io.yaml
src/data/dh_vs_linkml_json/material_entities.json: src/data/examples/valid/NamedThingCollection-processes-with-io.yaml
	# the name of the output is discovered from the outer slot
	$(RUN) linkml-json2dh \
		--input-file $< \
		--input-format yaml \
		--output-dir $(dir $@)


project/json/beril_model.json: src/beril_model/schema/beril_model.yaml
	mkdir -p $(@D)
	$(RUN) gen-linkml \
		--format json  \
		--materialize-attributes \
		--materialize-patterns $< > $@

#examples/output/NamedThingCollection-processes-with-io.db: src/beril_model/schema/beril_model.yaml \
#src/data/examples/valid/NamedThingCollection-processes-with-io.yaml
#	# 		--module src/beril_model/datamodel/beril_model.py \
#	# --schema src/beril_model/schema/beril_model.yaml
#	# AttributeError: 'MaterialEntityId' object has no attribute '_sa_instance_state'
#	$(RUN) linkml-sqldb dump \
#		--db $@ \
#		--target-class NamedThingCollection \
#		--index-slot material_entities \
#		--no-validate \
#		--force \
#		--module src/beril_model/datamodel/beril_model.py src/data/examples/valid/NamedThingCollection-processes-with-io.yaml

examples/output/NamedThingCollection-processes.tsv: src/beril_model/schema/beril_model.yaml \
src/data/examples/valid/NamedThingCollection-processes-with-io.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--index-slot processes \
		--schema $^


examples/output/NamedThingCollection-material-entities.tsv: src/beril_model/schema/beril_model.yaml \
src/data/examples/valid/NamedThingCollection-processes-with-io.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--index-slot material_entities \
		--schema $^

target/usage_template.tsv: src/beril_model/schema/beril_model.yaml
	mkdir -p $(@D)
	$(RUN) generate_and_populate_template \
		 --destination-template $@ \
		 --source-schema-path $<
