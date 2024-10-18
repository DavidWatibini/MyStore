import csv
from datetime import datetime
import sys


# Loading the CSV Files

def load_groceries_csv(file_path):
    groceries = {}
    with open(file_path, mode='r', newline='', encoding='utf-8-sig') as csvfile:
        #print("CSV Headers:", stockCsv.fieldnames)
        stockCsv = csv.DictReader(csvfile)
        for row in stockCsv:
            grocery_item = { 
                'name': row['name'],
                'price': float(row['price']),  
                'stock': int(row['stock'])
            }
            groceries[row['id']] = grocery_item
    return groceries


def load_transactions_csv(file_path):
    transactions = []
    with open(file_path, mode='r', newline='', encoding='utf-8-sig') as csvfile:
        transactionCsv = csv.DictReader(csvfile)
        for row in transactionCsv:
            transaction = {
                'date': row['date'],
                'time': row['time'],
                'id': int(row['id']), 
                'quantity': int(row['quantity']),
                'payment': float(row['payment'])
            }
            transactions.append(transaction)
    return transactions


#Load users from csv file 
 
def load_csv_users(file_path="users.csv"):
    users = {}
    with open(file_path, mode='r', newline='', encoding='utf-8-sig') as csvfile:
        usersCsv = csv.DictReader(csvfile)
        for row in usersCsv:
            users[row['username']] = {
                'password': row['password'],
                'type': row['type']
            }
    return users


# Saving data back to our CSV files
def save_transactions(transaction_file, transactions):
    with open(transaction_file, 'a', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['date', 'time', 'id', 'quantity', 'payment']
        transactionsCsv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        transactionsCsv.writerows(transactions)



def save_groceries(grocery_file, groceries):
    with open(grocery_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['id', 'name', 'price', 'stock']
        stockCsv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        stockCsv.writeheader()
        for id, details in groceries.items():
            stockCsv.writerow({'id': id, 'name': details['name'], 'price': details['price'], 'stock': details['stock']})


# User authentication
def authenticate_user(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password:
        print(f"Welcome, {username}!")
        return users[username]['type']
    print("Invalid username or password.")
    return None


# Enter a sales transaction
def enter_sales_transaction(groceries, transactions):
    print("\nAvailable Groceries:")
    for id, g_details in groceries.items():
        print(f"ID: {id}, Name: {g_details['name']}")
    
    grocery_id = input("\nEnter the grocery ID: ")
    quantity = input("Enter quantity sold: ")
    payment = input("Enter payment received: ")
    
    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%I:%M:%S %p')

    groceries[grocery_id]['stock'] = str(int(groceries[grocery_id]['stock']) - int(quantity))
    
    transactions.append({
        'date': date,
        'time': time,
        'id': grocery_id,
        'quantity': int(quantity),
        'payment': float(payment)
    })

    print("Transaction has been recorded successfully.\n")



# Managers to add new inventory a 
def add_new_grocery(groceries):
    new_id = f"{len(groceries) + 1}"
    name = input("Enter the grocery name: ")
    price = float(input("Enter the price of each item: "))
    stock = int(input("Enter the stock level: "))

    groceries[new_id] = {
        'name': name,
        'price': price,
        'stock': stock
    }

    print("New grocery added.")


def main(transaction_file, grocery_file):
    transactions = load_transactions_csv(transaction_file)
    groceries = load_groceries_csv(grocery_file)
    users = load_csv_users()

    user_type = authenticate_user(users)
    if not user_type:
        return

    while True:
        print("\nMenu:")
        print("1. Enter a sales transaction")
        if user_type == 'manager':
            print("2. Add a new grocery product")
        print("3. Logout")

        choice = input("\nSelect an option: ")

        if choice == '1':
            enter_sales_transaction(groceries, transactions)
        elif choice == '2' and user_type == 'manager':
            add_new_grocery(groceries)
        elif choice == '3':
            save_transactions(transaction_file, transactions)
            save_groceries(grocery_file, groceries)
            print("Data saved. Logging out...")
            break
        else:
            print("Please try again.")


if __name__ == "__main__":
    transaction_file = sys.argv[1]
    grocery_file = sys.argv[2]
    main(transaction_file, grocery_file)
