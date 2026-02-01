# 🧠 Python Data Structures & Refactoring Homework

This repository contains solutions for several Python homework tasks focused on:
- data structures (stack),
- algorithmic problem solving (balanced brackets),
- code refactoring and PEP8 style.

All tasks are implemented using pure Python 🐍.

---

## 📁 Project Structure

The project consists of the following main files:

- **`stack.py`**  
  Contains the implementation of a simple Stack data structure (LIFO).  
  Includes basic methods such as push, pop, peek, size, and empty check.

- **`stack_balance_check.py`**  
  Contains the function that checks whether a string of brackets is balanced.  
  The solution is implemented using the Stack class.

- **`test_stack.py`**  
  Unit tests for checking balanced and unbalanced bracket sequences.  
  Tests are parameterized and cover multiple edge cases ✅.

- **`hw_refactoring.py`**  
  Refactored mail client implementation.  
  The original script was converted into a reusable class with:
  - clear separation of logic and configuration,
  - no hardcoded values,
  - PEP8-compliant naming,
  - documented methods.

- **`.gitignore`**  
  Ignores cache files and unnecessary artifacts.

---

## ✉️ Mail Client Overview

The `MailClient` class provides:
- sending emails via SMTP,
- receiving emails via IMAP,
- clean initialization through the constructor,
- configurable credentials and server addresses.

The implementation focuses on readability, maintainability, and clean architecture 🧩.

---

## 🧪 Testing

Bracket balance logic is covered with unit tests using `unittest`.
Both valid and invalid cases are tested to ensure correctness.




