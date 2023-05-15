## NamedThingCollection-processes-with-io
### Input
```yaml
material_entities:
- color: RED
  id: beril_model:samp1
  mass_g: 100
  name: sample 1
  type_value: beril_model:MaterialEntity
- color: GREEN
  id: beril_model:samp2
  mass_g: 100
  name: sample 3
  type_value: beril_model:MaterialEntity
processes:
- id: beril_model:proc1
  inputs:
  - beril_model:samp1
  name: changing sample color
  outputs:
  - beril_model:samp2
  type_value: beril_model:Process

```
## NamedThingCollection-material_entities-multiple-materials
### Input
```yaml
material_entities:
- color: RED
  id: beril_model:1
  mass_g: 100
  name: sample 1
  type_value: beril_model:MaterialEntity
- color: RED
  id: beril_model:2
  mass_g: 100
  name: sample 2
  type_value: beril_model:MaterialEntity
- color: GREEN
  id: beril_model:3
  mass_g: 100
  name: sample 3
  type_value: beril_model:MaterialEntity
- color: GREEN
  id: beril_model:4
  mass_g: 100
  name: sample 4
  type_value: beril_model:MaterialEntity

```
## NamedThingCollection-material_entities-minimal
### Input
```yaml
material_entities:
- id: beril_model:1
  name: sample 1
  type_value: beril_model:MaterialEntity

```
## NamedThingCollection-material_entities-illegal-mass_g
### Input
```yaml
material_entities:
- id: beril_model:2
  mass_g: heavy
  name: sample 2
  type_value: beril_model:MaterialEntity

```
## NamedThingCollection-material_entities-illegal-color
### Input
```yaml
material_entities:
- color: transparent
  id: beril_model:2
  name: sample 2
  type_value: beril_model:MaterialEntity

```
## NamedThingCollection-material_entities-untyped
### Input
```yaml
material_entities:
- id: beril_model:1
  name: sample 1

```
## NamedThingCollection-material_entities-missing-id
### Input
```yaml
material_entities:
- color: RED
  name: sample 1
  type_value: beril_model:MaterialEntity

```
## NamedThingCollection-material_entities-undefined-slot
### Input
```yaml
material_entities:
- id: beril_model:1
  name: sample 1
  type_value: beril_model:MaterialEntity
  undefined_slot: this slot is not defined in the schema

```
