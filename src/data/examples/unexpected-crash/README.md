If collection C has slot s that points to instances of class I, 
and I only has one required slot r, then the following will crash most LinkML tools
with error ???

```yaml
s:
  - r: value1
```

