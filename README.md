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

### 1. `saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`
- **Keyword-only arguments**
- Performs withdrawals with proper balance, limit, and daily withdrawal checks.  
- **Returns:** `saldo, extrato`

---

### 2. `deposito(saldo, valor, extrato, /)`
- **Positional-only arguments**
- Performs deposits into the account.  
- **Returns:** `saldo, extrato`

---

### 3. `extrato(saldo, /, *, extrato)`
- **Positional and keyword-only arguments**
- Displays or returns the transaction statement.  
- **Returns:** None (prints or formats output)

---

### 4. `criar_usuario(usuarios)`
- Registers a new user in the system.
- Each user contains:- **Address format:** `"logradouro, nro - bairro - cidade/sigla_estado"`
- CPF must contain **only digits**, and duplicate CPFs are **not allowed**.

---

### 5. `criar_conta_corrente(contas, usuarios)`
- Creates a new checking account linked to an existing user.
- Each account contains:
- **Agência:** `"0001"`  
- **Número da conta:** sequentially assigned, starting at 1.  
- One user can have multiple accounts, but each account belongs to only one user.
