#!/usr/bin/env python3


# function to get details about a python data structure
# Object - ID, Type & Value
def tell_about(data_structure):
	print("-----------------------------------")
	print("ID: ", id(data_structure))
	print("Type: ", type(data_structure))
	print("Length: ", len(data_structure))
	print("Contents: ", data_structure)
	print("-----------------------------------")


# Mutability & Immutability experiment
def experiment_changing_zero_index(data_structure):
	tell_about(data_structure)
	data_structure[0] = "$$experiment_changing_zero_index$$"


# Ordering and Unordering of Data Structure
def experiment_order_unorder_ds(data_structure):
	tell_about(data_structure)
	ds_list = list(data_structure)
	tell_about(ds_list)
	ds_set = set(data_structure)
	tell_about(ds_set)


letters = "abcdefghijklmnopqrstuvwxyz"
experiment_order_unorder_ds(letters)