`Editor: Tearsyu`
# DesignPattern
This project is used to practice design pattern in Python and Java. I will note what I understand in this project.

## Creational pattern
Creational design patterns are responsible for efficient object creation mechanisms, it abstracts the process of instance, which increase the flexibility and reuse of existing code.

### Singleton
Singleton is a creational design pattern that lets you ensure that a class has only one instance and provide a global access point to this instance.
I have use this pattern when I do homework of web technique to create a single list of object<Person> without connect to database.

#### Python
In python code, I use a class decorator to realize this pattern. The class decorator generates the unique instance.

### Factory
Factory Method is a creational design pattern that provides an interface for creating objects in superclass, but allow subclasses to alter the type of objects that will be created.

## Behavioral Pattern
Behavioral patterns are design pattern that identify common communication patterns between objects and realize these patterns. It not just focus on the structure of class and object, but also their interactions.

### Strategy pattern(policy pattern)
Strategy pattern defines different methods or algorithm and encapsulates them, these methods can be exchanged according to client type.

### Observer pattern
This pattern is a way of notifying change to other concentrated class which is depended on it. I have use it to notify the error message when I have developed a blog web.

### Command pattern
Encapsulating a command request as an object is its essential, it's no need to identify the starter of this command. I use it in creating a connexion pool of database and a simple server.

## Structual Pattern
Structural design patterns are responsible for building simple and efficient class hierarchies and relations between different classes. It focus on the compo of classes.

### Adapter Pattern
It converts the interface of a class into another interface that clients expect. With this pattern, we wrap an existing class with a new interface without modifying the original code. I may used this pattern when developing Android app(ListView needs adapters to adapt the size of phone...I guess).
