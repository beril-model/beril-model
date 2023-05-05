## PersonCollection-minimal-plus
### Input
```yaml
entries:
- id: example:Person001
  name: foo bar
- id: example:Person002
  name: foo bar

```
## Person-minimal
### Input
```yaml
id: example:Person001

```
## PersonCollection-no-id
### Input
```yaml
age_in_years: 33
name: foo bar
primary_email: foo.bar@example.com

```
## PersonCollection-dupe-ids
### Input
```yaml
entries:
- id: example:Person001
  name: foo bar
- id: example:Person001
  name: foo bar
  undefined: undefined

```
## PersonCollection-bad-id-pattern
### Input
```yaml
entries:
- id: example_Person001
  name: foo bar
- id: example_Person002
  name: foo bar

```
## PersonCollection-undefined-slot
### Input
```yaml
entries:
- id: example:Person001
  name: foo bar
- id: example:Person002
  name: foo bar
  undefined: undefined

```
