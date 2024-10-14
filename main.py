import csv
from datetime import datetime
import sys 

"""
Load grocery data from the grocery CSV file into a list of dictionaries

Each dictionary contains:
grocery_id (int): Unique identifier for the grocery item
grocery_name (str): Name of the grocery item
price (float): Price of one unit of the grocery item. Float Coz of Decimal Values
stock (int): Current stock level of the grocery item

Returns:
A list of grocery product dictionaries, or an empty list if an error occurs

""" 

def load_csv_groceries(file_path):

    groceries = []  # I Initialize an empty list to store new grocery data
    
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile) # Read the CSV file into a dictionary reader
        for row in reader:
            # Create a dictionary for the grocery item and convert it to types needed
            grocery_item = { 
                'grocery_id': int(row['grocery_id']), 
                'grocery_name': row['grocery_name'],
                'price': float(row['price']),  
                'stock': int(row['stock'])
                }
                groceries.append(grocery_item)  # Append the dictionary to the list
                
    return groceries  



#Load sales transactions from the CSV file into a list and return a list of sales transactions

def load_csv_transactions(file_path):

    transactions = [] # I Initialize an empty list to store new transaction data
    
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Append each transaction to the list
            transactions.append(row)

    return transactions 

    



