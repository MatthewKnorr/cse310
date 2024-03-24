import firebase_admin
from firebase_admin import credentials, firestore
import json
import os

# Function to create serviceAccount.json file
def create_service_account_file():
    try:
        # Initialize Firebase app
        app = firebase_admin.initialize_app()
        
        # Get credentials
        cred = app.credential.get_credential()
        
        # Get the service account info
        service_account_info = {
            "type": cred.get_type(),
            "project_id": cred.get_project_id(),
            "private_key_id": cred.get_private_key_id(),
            "private_key": cred.get_private_key(),
            "client_email": cred.get_client_email(),
            "client_id": cred.get_client_id(),
            "auth_uri": cred.get_auth_uri(),
            "token_uri": cred.get_token_uri(),
            "auth_provider_x509_cert_url": cred.get_auth_provider_x509_cert_url(),
            "client_x509_cert_url": cred.get_client_x509_cert_url()
        }
        
        # Save the service account info to a JSON file
        with open('serviceAccount.json', 'w') as json_file:
            json.dump(service_account_info, json_file)
        
        print("serviceAccount.json file created successfully!")
        
    except Exception as e:
        print(f"Error creating serviceAccount.json file: {e}")

# Initialize Firestore database with the generated serviceAccount.json
try:
    # Check if serviceAccount.json exists, if not, create it
    if not os.path.exists('serviceAccount.json'):
        create_service_account_file()
    
    # Initialize Firestore with the serviceAccount.json file
    cred = credentials.Certificate('serviceAccount.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()

except Exception as e:
    print(f"Error initializing Firestore: {e}")

# Function to add transaction
def add_transaction(date, category, description, amount):
    transaction = {
        'date': date,
        'category': category,
        'description': description,
        'amount': amount
    }
    db.collection('transactions').add(transaction)
    print("Transaction added successfully!")

# Function to update transaction
def update_transaction(transaction_id, date, category, description, amount):
    transaction_ref = db.collection('transactions').document(transaction_id)
    transaction_data = {
        'date': date,
        'category': category,
        'description': description,
        'amount': amount
    }
    transaction_ref.update(transaction_data)
    print("Transaction updated successfully!")

# Function to delete transaction
def delete_transaction(transaction_id):
    db.collection('transactions').document(transaction_id).delete()
    print("Transaction deleted successfully!")

# Function to retrieve transactions
def retrieve_transactions():
    transactions_ref = db.collection('transactions')
    transactions = transactions_ref.stream()
    for transaction in transactions:
        print(f'Transaction ID: {transaction.id}, Data: {transaction.to_dict()}')

# Main function to run the app
if __name__ == '__main__':
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. Update Transaction")
        print("3. Delete Transaction")
        print("4. View Transactions")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            add_transaction(date, category, description, amount)
        
        elif choice == '2':
            transaction_id = input("Enter transaction ID to update: ")
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            update_transaction(transaction_id, date, category, description, amount)
        
        elif choice == '3':
            transaction_id = input("Enter transaction ID to delete: ")
            delete_transaction(transaction_id)
        
        elif choice == '4':
            retrieve_transactions()
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please enter a valid option.")
