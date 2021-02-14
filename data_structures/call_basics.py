#!/usr/bin/env python3

from basics import *

def main():
	letters = "abcdefghijklmnopqrstuvwxyz"
	experiment_order_unorder_ds(letters)
	#experiment_mutability_immutability_ds(letters) #string
	#experiment_mutability_immutability_ds(list(letters)) #list
	#experiment_mutability_immutability_ds(set(letters)) #set


# When running the script directly in shell, python interpreter assigns "__main__" to __name__, i.e., __name__= "__main__"
if __name__ == "__main__":
	main()