# Python-piscine
Here's a structured learning plan to help you master Python from the ground up for the 42 School's Python Piscine project:
Stage 1: Python Basics
1. **Syntax and Variables 
   - Printing output (`print()`)
   - Variables and data types (`int`, `float`, `str`, `bool`)
   - Type conversion (`int()`, `str()`, `float()`)

2. Operators and Expressions 
   - Arithmetic (`+`, `-`, `*`, `/`, `%`, `//`, `**`)
   - Comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`)
   - Logical (`and`, `or`, `not`)

3. Control Flow 
   - Conditional statements (`if`, `elif`, `else`)
   - Loops (`for`, `while`)
   - Loop control (`break`, `continue`, `pass`)

---

Stage 2: Data Structures
4. Strings and String Methods  
   - Indexing and slicing
   - String methods (`strip()`, `lower()`, `upper()`, `split()`, `join()`)

5. Lists and List Methods  
   - Creating lists, indexing, and slicing
   - List methods (`append()`, `remove()`, `pop()`, `sort()`, `reverse()`)

6. Tuples and Sets 
   - Immutable nature of tuples
   - Set operations (`union()`, `intersection()`, `difference()`)

7. Dictionaries  
   - Key-value pairs
   - Dictionary methods (`get()`, `keys()`, `values()`, `items()`)

---

Stage 3: Functions and Modules
8. Defining Functions  
   - Parameters and return values
   - Default arguments, `*args`, `**kwargs`

9. Lambda Functions 
   - Anonymous functions (`lambda`)

10. Modules and Imports  
   - Using built-in modules (`math`, `random`, `datetime`)
   - Importing (`import`, `from ... import`)

---

Stage 4: File Handling and Error Handling
11. File Handling  
   - Reading and writing files (`open()`, `read()`, `write()`, `close()`)

12. Exception Handling  
   - Using `try`, `except`, `finally`
   - Raising exceptions (`raise`)

---

Stage 5: Object-Oriented Programming (OOP)
13. Classes and Objects  
   - Defining classes and creating objects
   - Instance and class variables

14. Inheritance and Polymorphism  
   - Single and multiple inheritance
   - Overriding methods

---

Stage 6: Advanced Concepts
15. Iterators and Generators  
   - `__iter__` and `__next__`
   - Using `yield`

16. Decorators  
   - Function decorators (`@staticmethod`, `@classmethod`)

17. Regular Expressions (`re` module) 
   - Pattern matching (`match()`, `search()`, `findall()`)

---

Stage 7: Algorithms and Problem-Solving
18. Sorting and Searching  
   - Bubble sort, merge sort, binary search

19. Recursion 
   - Writing recursive functions

20. Basic Data Structures (Stacks, Queues, Linked Lists) 
   - Implementing using lists or `collections.deque`

---

Stage 8: Python for System and Network Programming
21. Working with the OS Module 
   - Interacting with the file system

22. Networking with `socket` 
   - Basic socket programming

---

Stage 9: Using Git and Shell Scripting
23. Git Basics 
   - Cloning, branching, committing

24. Bash and Python Integration  
   - Running Python scripts in the terminal
   - 
1) Work Inside a Virtual Machine (VM)
            OR
2) Use Local Installation (Without Admin Rights)

### **What is Conda?**  
**Conda** is a **package manager and environment manager** that helps you install and manage **Python** and other dependencies without requiring **admin rights**.  

It is especially useful if:  
✔️ You **can’t install Python system-wide** (like in your case).  
✔️ You **need multiple Python versions** for different projects.  
✔️ You **want an easy way to install packages** without `pip` conflicts.

---

### **Why Use Conda?**  
✔️ **Works Without Admin Rights** – You can install Python in your **home directory**.  
✔️ **Manages Python Versions** – Install and switch between **Python 2, 3.10, etc.**  
✔️ **Manages Dependencies** – Easily install packages like `numpy`, `pandas`, etc.  

---

### **How to Install Conda (Without Admin Rights)**
Since you don’t have admin rights, you can **install Miniconda (lightweight version of Conda)** in your home directory.

#### **Step 1: Download Miniconda**
Run this in your terminal:
```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

#### **Step 2: Install in Your User Space**
Run:
```sh
bash Miniconda3-latest-Linux-x86_64.sh
```
- When it asks for the installation path, choose a location **inside your home directory** (e.g., `~/miniconda`).
- Say **yes** when it asks if you want to initialize Conda.

#### **Step 3: Restart Your Shell**
Close and reopen your terminal or run:
```sh
source ~/.bashrc  # or source ~/.zshrc if you're using Zsh
```

#### **Step 4: Create a Python 3.10 Environment**
Now that Conda is installed, create an environment with **Python 3.10**:
```sh
conda create --name python310 python=3.10
```
Activate the environment:
```sh
conda activate python310
```
Now, running:
```sh
python --version
```
should show **Python 3.10**.

---

### **Using Conda for the 42 Piscine**
✔️ **You can install packages without admin rights**:  
```sh
conda install numpy pandas
```
✔️ **Switch between Python versions easily**:  
```sh
conda activate python310  # Switch to Python 3.10
conda deactivate          # Exit the environment
```
✔️ **Keeps your workspace clean** – No need to modify system-wide settings.  

---

### **🚀 Best Choice for You?**
Yes! Since you **don’t have admin rights**, using **Conda** is one of the best ways to get Python 3.10 working for your 42 School Python Piscine. Would you like help setting it up?
