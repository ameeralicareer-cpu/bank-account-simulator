# Bank Account Simulator

## Project Description

Bank Account Simulator ek simple Python project hai jo basic banking operations ko simulate karta hai. Is project mein different types ke bank accounts create kiye ja sakte hain aur un par deposit, withdraw aur account details display karne jaisi operations perform ki ja sakti hain.

## Functionalities

This project includes the following features:

* Create a **Savings Account**
* Create a **Current Account**
* Deposit money into an account
* Withdraw money from an account
* Savings Account mein interest add karna
* Current Account mein overdraft facility
* Saare accounts ki details display karna
* Accounts ka data JSON file mein save karna
* Saved accounts ko JSON file se load karna
* Menu-driven interface

## Account Types

### Savings Account

Savings Account, `Account` class se inherit karta hai aur ismein interest rate ka feature bhi hai.

### Current Account

Current Account bhi `Account` class se inherit karta hai aur ismein limited overdraft facility available hai.

## How to Run

Project ko run karne ke liye VS Code ke terminal mein yeh command use karein:

```bash
python bank_simulator.py
```

Program run hone ke baad menu show hoga jahan se different options select kiye ja sakte hain.

## What I Learned

Is project ko banate waqt maine Python ke important concepts seekhe:

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
* `isinstance()` ka use
* Data ko save aur load karna
