#!/usr/bin/env python3

## Function to print details (ID, Type & Value) about a python data structure
def tell_about(data_structure):
	print("-----------------------------------")
	print("Id: ", id(data_structure))
	print("Type: ", type(data_structure))
	print("Value: ", data_structure)
	print("-----------------------------------")

## Ordering and Unordering of Data Structure
def experiment_order_unorder_ds(data_structure):
	tell_about(data_structure)
	ds_list = list(data_structure)
	tell_about(ds_list)
	ds_set = set(data_structure)
	tell_about(ds_set)

## Mutability & Immutability experiment with changing zero index as example'''
def experiment_mutability_immutability_ds(data_structure):
	data_structure[0] = "$$experiment_changing_zero_index$$"
	tell_about(data_structure)


def main():
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	experiment_order_unorder_ds(alphabet)
	#experiment_mutability_immutability_ds(letters) #string
	#experiment_mutability_immutability_ds(list(letters)) #list
	#experiment_mutability_immutability_ds(set(letters)) #set


# When running the script directly in shell, python interpreter assigns "__main__" to __name__, i.e., __name__= "__main__"
if __name__ == "__main__":
	main()
