# Python List & Set - Basic Notes

## List: 
* Can have any number of items 
* Created by Placing elements in [] bracket and separated by commas
* Items inside the list can be of any data type 
* Ordered Collection of Objects

    * Underlying Implementation is Dynamic Array. Starting index is 0 

```sh

# empty list
fruits = []

# list of even numbers less than 10
even_numbers = [2, 4, 6, 8]

# list with mixed data types
what_i_like = [ 9, “iPhone”, “Apple”, “Black”]

```

## Set:
* Can have any number of items 
* Created by Placing elements in {} bracket and separated by commas
* Items inside the list can be of any data type 
* UnOrdered Collection of Objects

    * Empty Set is Created Differently  

```sh 

# empty list - note {} create a dict
fruits = set() 

# set of even numbers less than 10
even_numbers = {2, 4, 6, 8}

# set with mixed data types
what_i_like = [ 9, “iPhone”, “Apple”, “Black”]

```

## Ordered and UnOrdered Data Structure:

```sh 
letters = “abcdefghijklmnopqrstuvwxyz” 
print(“List: ”, list(letters) )
print(“List: ”, set(letters) )

```

Output of list will be in same order they are specified. So its a ordered collection 
Output of set will be in different order they are specified, So it a unordered collection

Mutable & Immutable Objects:

