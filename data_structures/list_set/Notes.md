# Python List & Set - Basic Notes

## List: 
* Can have any number of items 
* Created by Placing elements in [] bracket and separated by commas
* Items inside the list can be of any data type 
* Ordered Collection of Objects
* Additional Notes
    * Underlying Implementation is Dynamic Array. Starting index is 0 

```sh

# empty list
fruits = []

# list of even numbers less than 10
even_numbers = [2, 4, 6, 8]

# list with mixed data types
what_i_like = [ 9, "iPhone", "Apple", "Black"]

```

## Set:
* Can have any number of items 
* Created by Placing elements in {} bracket and separated by commas
* Items inside the list can be of any data type 
* UnOrdered Collection of Objects
* Set does not hold duplicate Items
* Additional Notes
    * Empty Set is Created (differently)  using set()
    * Empty {} will create dict data structure 😊

```sh 

# empty list - note {} create a dict
fruits = set() 

# set of even numbers less than 10
even_numbers = {2, 4, 6, 8}

# set with mixed data types
what_i_like = [ 9, "iPhone", "Apple", "Black"]

```

## Ordered and UnOrdered Data Structure:

```sh 
letters = "abcdefghijklmnopqrstuvwxyz"

letters_list=list(letters)
letters_set=set(letters)

print("List: ", letters_list )
print("Set: ", letters_set )

```
or 
```sh
~/coach-lab$ python3 data_structures/map_list_set/order_unorder_ds.py
```

Output of list will be in same order they are specified. So its a ordered collection 
Output of set will be in different order they are specified, So it a unordered collection


