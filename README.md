# Global Banking System

A simple, console-based banking application built with Python. This project simulates basic banking operations like creating accounts, managing funds, and viewing transaction histories. It's designed as a straightforward demonstration of object-oriented programming principles.

## Features

* **Account Creation:** Easily create a new bank account with an initial deposit.
* **Deposit Funds:** Add money to an existing account.
* **Withdraw Funds:** Withdraw money from an account, with checks for insufficient balances.
* **Balance Inquiry:** Check the current balance of any account.
* **Transaction History:** View a detailed history of all transactions for an account.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Mukasshaf/Global_banking_system.git](https://github.com/Mukasshaf/Global_banking_system.git)
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd Global_banking_system
    ```

## Usage

1.  **Run the application:**
    ```sh
    python main.py
    ```

2.  **Follow the on-screen menu:**
    Once the script is running, you will be presented with a menu of options. Enter the number corresponding to the action you wish to perform.

   
## How It Works

The system is built around a `BankingSystem` class that manages all accounts and transactions. Each account is a dictionary entry within the `BankingSystem` instance, storing its balance and transaction history. All operations are handled through methods in this class, providing a clear and organized structure.
