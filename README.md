# Resolution for the Clean Code for Bank System Challenge 

Original source code:  
[Digital Innovation One – Python Bank Challenge](https://github.com/digitalinnovationone/trilha-python-dio/blob/00_fundamentos/00%20-%20Fundamentos/desafio.py)

## Goal

Separate the logic into functions for:

- Deposits  
- Withdrawals  
- Viewing transaction history (statement)  
- Registering users (clients)  
- Creating checking accounts linked to users  

---

## Function Specifications

### 1. `withdrawal(*, balance, amount, statement, limit, withdraw_count, withdraw_limit)`
- **Keyword-only arguments**
- Performs withdrawals with proper balance, limit, and daily withdrawal checks.
- Validates if withdrawal amount exceeds balance, daily limit, or maximum number of withdrawals.
- Updates balance and statement on successful withdrawal.
- **Returns:** `balance, statement, withdraw_count, success`

---

### 2. `deposit(balance, amount, statement, /)`
- **Positional-only arguments**
- Performs deposits into the account.
- Validates that deposit amount is positive.
- Updates balance and statement on successful deposit.
- **Returns:** `balance, statement` or `False` for invalid amounts

---

### 3. `retrieve_statement(balance, /, *, statement)`
- **Positional and keyword-only arguments**
- Displays the transaction statement and current balance.
- Shows "No transactions have been made" if no transactions exist.
- **Returns:** None (prints output directly)

---

### 4. `register_client(clients)`
- Registers a new user (client) in the system.
- Collects CPF, full name, and address information.
- Validates that all required fields are provided.
- Prevents duplicate CPF registrations.
- **Returns:** `True` on success, `False` on failure

---

### 5. `create_checking_account(clients, accounts)`
- Creates a new checking account linked to an existing user.
- Each account contains:
  - **Agency:** `"0001"` (fixed)
  - **Account number:** sequentially assigned, starting at 1
  - **Owner CPF:** links to registered client
- Validates that the CPF exists in the client registry.
- **Returns:** `True` on success, `False` on failure


## Usage

Run the `main()` function to start the banking system. The program provides a menu with options to:
- Create new user (`u`)
- Create new checking account (`c`) 
- Deposit funds (`d`)
- Withdraw funds (`s`)
- View statement (`e`)
- Quit the system (`q`)