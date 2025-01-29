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
1️⃣ Work Inside a Virtual Machine (VM)
Since your school allows using a virtual machine, this is the best approach.

✅ Steps:

Check if you can install a VM

If you can, install Ubuntu 22.04 (or any Linux OS with Python 3.10).
Use VirtualBox or VMware (if your school allows).
Use a Pre-installed VM

If 42 provides a VM image (like on intranet), use that.
Inside the VM, install Python 3.10

If Python 3.10 is missing, install it with:
sh
Copy
Edit
sudo apt update
sudo apt install python3.10
Check the version:
sh
Copy
Edit
python3.10 --version
2️⃣ If a VM is Not Allowed, Use the Cluster Computers
If you cannot use a VM, use the 42 school computers directly and check if Python 3.10 is available.

✅ Steps:

Check if Python 3.10 is already installed:

sh
Copy
Edit
python3.10 --version
If it works, you're good to go!
If not, check if you can install Python in a local directory (like goinfre).
Install Python 3.10 in Your User Space (Goinfre)

If your campus has goinfre, install Python there to avoid needing admin rights.
Run:
sh
Copy
Edit
mkdir -p $HOME/goinfre/python310
cd $HOME/goinfre
wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tgz
tar -xvf Python-3.10.12.tgz
cd Python-3.10.12
./configure --prefix=$HOME/goinfre/python310
make -j$(nproc)
make install
Then, add it to your path:
sh
Copy
Edit
echo 'export PATH=$HOME/goinfre/python310/bin:$PATH' >> ~/.zshrc
source ~/.zshrc
Now, check if Python 3.10 is available:
sh
Copy
Edit
python3.10 --version
3️⃣ General Rules Summary
No Segmentation Faults: Your programs must not crash (e.g., segfault, bus error).
Testing is Encouraged: You should write test programs to validate your code.
Use Git for Submissions: Everything must be in the assigned Git repository.
Deepthought Grading: If an error occurs in your work, grading stops immediately.
Use Explicit Imports:
✅ Allowed: import numpy as np
❌ Not Allowed: from numpy import *
No Global Variables: Declare all variables inside functions/classes.
📌 Recommended Action for You
🔹 First Choice: Use a Virtual Machine with Python 3.10.
🔹 Second Choice: Use Python 3.10 pre-installed on 42's computers.
🔹 Third Choice (if required): Install Python 3.10 in goinfre.
