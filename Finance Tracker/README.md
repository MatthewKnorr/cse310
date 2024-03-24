# Overview

**Important! Do not say in this section that this is a college assignment. Talk about what you are trying to accomplish as a software engineer to further your learning.**

**Description of the software and its integration with a Cloud Database**

I developed a Personal Finance Tracker application to enhance my skills in software development, particularly focusing on integrating a cloud database. The software allows users to track their income, expenses, and budgets effectively. It integrates with a Firestore cloud database to store and manage financial transactions securely.

### How to Use the Program

1. **Add Transaction**: 
    - Enter the date in YYYY-MM-DD format.
    - Enter the category of the transaction.
    - Provide a brief description of the transaction.
    - Enter the amount of the transaction.

2. **Update Transaction**: 
    - Enter the ID of the transaction to be updated.
    - Update the transaction details.

3. **Delete Transaction**: 
    - Enter the ID of the transaction to be deleted.

4. **View Transactions**: 
    - Displays a list of all transactions stored in the Firestore database.

**Purpose for writing this software**

The purpose of developing this software is to enhance my understanding and practical experience with cloud database integration in software development. It serves as a practical application to manage personal finances, offering a real-world application of cloud database functionalities.

### Software Demo Video

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

**Description of the cloud database you are using**

I am using Firestore, a flexible, scalable database for mobile, web, and server development from Firebase and Google Cloud Platform.

**Structure of the database created**

The Firestore database contains a collection named `transactions` with the following fields:

- `date`: Date of the transaction (String)
- `category`: Category of the transaction (String)
- `description`: Description of the transaction (String)
- `amount`: Amount of the transaction (Float)

# Development Environment

**Tools used to develop the software**

- Python 3.x
- Firebase Admin SDK

**Programming language used and any libraries**

- Python
    - firebase_admin
    - firestore

# Useful Websites

- [Firestore Documentation](https://firebase.google.com/docs/firestore)
- [Firebase Admin SDK Documentation](https://firebase.google.com/docs/admin/setup)

# Future Work

**Things to fix, improve, and add in the future**

- Implement user authentication for enhanced security.
- Add data validation to prevent incorrect input.
- Implement data visualization for better insights and analysis.