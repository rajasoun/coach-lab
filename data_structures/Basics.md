# Basics 

## Objects in Python 

* Objects are Python abstraction of data
* All data in python is represented by object or as relationship between them
* Every object in python has
    * identity
      * Object Address in Memory
      * Unique integer for the object during lifetime
    * type
      * Type of Object 
      * In Built Object & User Defined
    * value  
      * Value or Content of Object 
      * Objects whose value can change are called Mutable 
      * Objects whose value can not change are called Immutable 

### Objects - Summary
1. id() function returns identity of the object 
2. type() function returns type of the object 
3. is operator compares identity of two objects 
== operator compares value of two objectors 

### Function

* Group of related statements that perform a specific task.
* provide better modularity and a high degree of code reusing

Example:

```sh
## Function to print details (ID, Type & Value) about a python data structure
def tell_about(data_structure):
	print("-----------------------------------")
	print("Id: ", id(data_structure))
	print("Type: ", type(data_structure))
	print("Value: ", data_structure)
	print("-----------------------------------")
```

Calling the function
```sh
tell_about(5)
```

(Advanced) Quick Read : [Python Modules & Import](https://medium.com/python-features/what-happens-behind-the-scenes-when-we-import-a-module-in-python-2775da153790)

### Lab

In Console
```sh
$ cd data_structures
$ python3
>>> from tell_about_ds import *
>>> alphabet = "abcdefghijklmnopqrstuvwxyz"
>>> tell_about(alphabet)
```
#### Assignments:

Use tell_about user defined function with following data types
```sh
>>> tell_about(5)
>>> tell_about(5.0)
>>> tell_about("5")
>>> tell_about(5j)
>>> tell_about([1,2,3])
>>> tell_about({1,2,3})
>>> tell_about((1,2,3))
>>> tell_about({'Name': 'Raja','Hobby': 'Coaching'})
```

> The string  (>>>)  denotes python3 shell. Do not copy it while executing the statements
