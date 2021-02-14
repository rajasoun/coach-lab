#!/usr/bin/env python3


# function to get details about a python data structure
def tell_about(data_structure):
	print("ID: ", id(data_structure))
	print("Type: ", type(data_structure))
	print("Length: ", len(data_structure))
	print("Contents: ", data_structure)


## List Data Stucture Basics

# empty list
fruits = []
tell_about(fruits)
