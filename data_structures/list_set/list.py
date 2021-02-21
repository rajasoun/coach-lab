#!/usr/bin/env python3


# function to get details about a python data structure
def tell_about(data_structure):
	print("ID: ", id(data_structure))
	print("Type: ", type(data_structure))
	print("Length: ", len(data_structure))
	print("Contents: ", data_structure)

def get_input_numbers_as_list():
  input_prompt="Enter Numbers [use space for seperation] : \n"
  #    map() function returns a map object after applying the given function to each item of a given iterable (list, tuple etc.)
  #  input() function to take input from the user
  # rsplit() method returns a list of strings after breaking the given string from right side by the specified separator - default is space
  #  split() method splits a string into a list
  num_list=list(map(int,input(input_prompt).rstrip().split()))
  return num_list

def largest_number_in_list(number_list : list):
  return(max(number_list))

## List Data Stucture Basics

# empty list
fruits = []
tell_about(fruits)

# Get List of Numbers 
number_list = get_input_numbers_as_list()

# Print Largest Number
print(largest_number_in_list(number_list))
