#!/usr/bin/env python3

# function to get details about a python data structure
# Object - ID, Type & Value
def tell_about(data_structure):
	print("-----------------------------------")
	print("Id: ", id(data_structure))
	print("Type: ", type(data_structure))
	print("Value: ", data_structure)
	print("-----------------------------------")
	
def main():
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	tell_about(alphabet)


# When running the script directly in shell, python interpreter assigns "__main__" to __name__, i.e., __name__= "__main__"
if __name__ == "__main__":
	main()