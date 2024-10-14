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
    
    with open(file_path, mode='r', newline='') as csvfile:
        storeCsv = csv.DictReader(csvfile) # Read the CSV file into a dictionary reader
        for row in storeCsv:
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
    
    with open(file_path, mode='r', newline='') as csvfile:
        storeCsv = csv.DictReader(csvfile)
        for row in storeCsv:
            # Append each transaction to the list
            transactions.append(row)

    return transactions 

    
#Save new imput grocery products to the CSV file.

def save_groceries_csv(file_path, groceries):

    with open(file_path, mode='w', newline='') as csvfile:
         storeCsv = csv.writer(csvfile)
        storeCsv.writerow(['id', 'name', 'price', 'stock'])

        for grocery_id, data in groceries.items():
            # Write each grocery item as a row in the CSV
            storeCsv.writerow([grocery_id, data['name'], data['price'], data['stock']])


#Save sales transactions to the CSV file.

def save_transactions_csv(file_path, transactions):
    with open(file_path, mode='w', newline='') as csvfile:
        
        storeCsv = csv.writer(csvfile)
        storeCsv.writerow(['date_time', 'grocery_id', 'quantity', 'payment']) 
        for transaction in transactions:
            storeCsv.writerow([transaction['date_time'], transaction['grocery_id'], transaction['quantity'], transaction['payment']])

