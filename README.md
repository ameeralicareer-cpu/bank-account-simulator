# bank-account-simulator
A Python CLI program simulating basic bank account operations

## Project Description

Bank Account Simulator is a simple Python project that simulates basic banking operations. In this project, you can create different types of bank accounts and perform operations on them such as deposit, withdraw, and displaying account details.

## Functionalities

This project includes the following features:

* Create a **Savings Account**
* Create a **Current Account**
* Deposit money into an account
* Withdraw money from an account
* Add interest to a Savings Account
* Overdraft facility for a Current Account
* Display details of all accounts
* Save account data to a JSON file
* Load saved accounts from a JSON file
* Menu-driven interface

## Account Types

### Savings Account

The Savings Account inherits from the `Account` class and includes an interest rate feature.

### Current Account

The Current Account also inherits from the `Account` class and includes a limited overdraft facility.

## How to Run

To run the project, use the following command in the VS Code terminal:

​```bash
python bank_simulator.py
​```

Once the program runs, a menu will be displayed from where different options can be selected.

## What I Learned

While building this project, I learned several important Python concepts:

* Python Classes and Objects
* Constructors (`__init__`)
* Inheritance
* Method Overriding
* Functions
* Loops and Conditions
* User Input
* JSON File Handling
* Reading and Writing Files
* Working with Lists
* Menu-driven Programs
* Using `isinstance()`
* Saving and loading data
