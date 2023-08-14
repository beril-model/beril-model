## NamedThingCollection-processes-with-io
### Input
```yaml
material_entities:
- color: RED
  id: beril_model:samp1
  mass_g: 100
  name: sample 1
- color: GREEN
  id: beril_model:samp2
  mass_g: 100
  name: sample 3
processes:
- id: beril_model:proc1
  inputs:
  - beril_model:samp1
  name: changing sample color
  outputs:
  - beril_model:samp2

```
## NamedThingCollection-min-mixed-coll
### Input
```yaml
material_entities:
- color: RED
  id: beril_model:1
  mass_g: 100
  name: sample 1
- color: RED
  id: beril_model:2
  mass_g: 100
  name: sample 2
- color: GREEN
  id: beril_model:3
  mass_g: 100
  name: sample 3
- color: GREEN
  id: beril_model:4
  mass_g: 100
  name: sample 4
processes:
- id: beril_model:proc1
  name: changing sample color

```
## NamedThingCollection-material_entities-multiple-materials
### Input
```yaml
material_entities:
- color: RED
  id: beril_model:1
  mass_g: 100
  name: sample 1
- color: RED
  id: beril_model:2
  mass_g: 100
  name: sample 2
- color: GREEN
  id: beril_model:3
  mass_g: 100
  name: sample 3
- color: GREEN
  id: beril_model:4
  mass_g: 100
  name: sample 4

```
## NamedThingCollection-material_entities-minimal
### Input
```yaml
material_entities:
- id: beril_model:1
  name: sample 1

```
## NamedThingCollection-material_entities-illegal-mass_g
### Input
```yaml
material_entities:
- id: beril_model:2
  mass_g: heavy
  name: sample 2

```
## NamedThingCollection-material_entities-illegal-color
### Input
```yaml
material_entities:
- color: transparent
  id: beril_model:2
  name: sample 2

```
## NamedThingCollection-material_entities-missing-id
### Input
```yaml
material_entities:
- color: RED
  name: sample 1

```
## NamedThingCollection-material_entities-undefined-slot
### Input
```yaml
material_entities:
- id: beril_model:1
  name: sample 1
  undefined_slot: this slot is not defined in the schema

```
## NamedThingCollection-material_entities-missing-prefix
### Input
```yaml
material_entities:
- color: RED
  id: undefined1
  mass_g: 100
  name: sample 1

```
