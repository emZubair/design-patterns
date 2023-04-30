### Singleton Pattern

```markdown
Singleton pattern make sure there is only instance and points global access to it. 
```
Singleton is a creational design pattern that lets you ensure that a class has only one instance, 
while providing a global access point to this instance. The most common reason for this is to control access 
to some shared resource—for example, a database or a file.

`Note:` that this behavior is impossible to implement with a regular constructor since a constructor call must always
return a new object by design.

The government is an excellent example of the Singleton pattern. A country can have only one official government. 