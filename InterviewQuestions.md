## Some Interview questions

Why is StringBuilder more efficient than String concatenation?

Answer: String concatenation uses more memory and time because JVM creates a new string, copies all characters from second string and assigns the new string to the original string. StringBuilder uses character arrays to do the same thing.

What are classes, objects? (and the difference between the two)
Objects are entities that are modeled after real world objects. 
Class is a template definition of a real world object. For example, Car class. Any type of car (SUV, Electric, Hybrid) is an object of type Car

What is instantiation?
The process of creating an object from class

What is a method (as opposed to, say, a C function)?
Method is a function that is associated with a class/object. It allows the object to interact with other objects or changes the behavior of the object

What is virtual method, pure virtual method?

What is class/static method?
Static methods are supposed to be common to all the objects of the type class. To access them, the class need not be instantiated.

What is static/class initializer?
Similar to static method, a static initializer will initialize some generic behaviour that is irrelevant to the different objects of type class.

What is constructor?
It is a method that prepares an object for all its interactions and behaviors. 

What is destructor/finalizer?
It is a method that destroys the intializations inside an object before the object itself is destroyed.

What is superclass or base class?
Superclass is a class from which another class inherits

what is subclass or derived class?
Subclass inherits from a super class

what is inheritance?
It is a mechanism that allows a class to acquire all properties of another class. Allows programmers to specify new properties while maintaining core set of properties from base class. Music Instruments -> Guitar

what is encapsulation?
A mechanism to restrict access to some of an object's properties.

what is multiple inheritance (and give an example)?
what is delegation/forwarding?
what is composition/aggregation?

what is abstract class?
A class that is defined abstract is generally supposed to be a generic type and not supposed to be directly instantiated

what is interface/protocol (and different from abstract class)?

what is method overriding?
Overriding = implementing a method from superclass to suit to the subclass's needs

what is method overloading (and difference from overriding)?
Overloading = declaring methods for different parameters

what is polymorphism (without resorting to examples)?
Ability to behave differently in different conditions

what is is-a versus has-a relationships (with examples)?
is-a = inheritance, has-a = composition

what is method signatures (what's included in one)?

what is method visibility (e.g. public/private/other)?
Access modifier define how other objects can interact with this object's properties.

Describe a OO representation of HTML.
DOM

Describe real-life examples of: tree, graph, hash table, linkedlists and arrays
Graph - Social Network Data, Network data, Maps
Array - storing images
Queue - printer pooler, drive in order system
Trie - Text Search in text editors
Trees - FileSystem, store possible moves in chess
Stack - Back functionality of a browser
Hash table - Caches
LinkedList - 

When would you use linked-list vs vector?
Better memory management in linkedlist for insert and delete than vectors. 

Can you implment a map with a tree? a list?
Yes - lookup of keys - in tree: O(logn), in list: O(n)

how do you implement a priority queue?
Using a heap

