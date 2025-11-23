# PROJECT TITLE
EMI_Predictor
# PROBLEM OVERVIEW
This is a Python-based EMI (Equated Monthly Installment) Calculator. 
It allows users to enter loan details such as principal amount, annual interest rate, 
and loan duration in years, and calculates the EMI using the standard financial formula.
# OBJECTIVES
1. To create a Python program that calculates EMI based on user inputs.
2. To apply the standard EMI formula accurately.
3. To practice input handling, functions, and mathematical operations in Python.
4. To provide a simple tool for users to compute monthly loan payments.
5. To document the process using algorithm, flowchart, and system architecture.
# TOOLS AND TECHNOLOGIES USED
1. Programming language-
   Python- Used to implement the EMI calculation logic.
2. Python Libraries-
   math module-for power calculations used in the EMI formula.
3. Development Tool-
   idle- Used for writing code.
4. Documentation Tool-
   READDME.md- For documentation.
# REQUIREMENTS
1. Software Requirements-
  a. Python 3.x
  b. Any code editor (VS Code / PyCharm / IDLE)
  c. Terminal or Command Prompt
2. Hardware Requirements
  a.Computer/laptop with at least 2 GB RAM
  b.Basic storage and display
2. Functional Requirements
 a. Accept user inputs: principal, interest rate, loan term
 b. Calculate EMI using formula
 c. Display EMI result
3. Non-Functional Requirements
 a. Fast and accurate calculation
 b. Easy to use
 c.Should handle zero-interest cases
# PROJECT MODULES
1. Input Module
   Takes user inputs:
   Principal Amount (P)
   Annual Interest Rate (R)
   Loan Duration in Years (Y)
   Validates basic input format.
3. Processing Module
   Converts annual interest into monthly interest.
   Converts years into total number of months.
   Applies the EMI formula.
   Handles special condition (0% interest).
4. EMI Calculation Module
   Contains the function calculate_emi().
   Performs mathematical operations using the math library.
   Returns the final EMI value.
5. Output Module
   Displays:
   Loan amount
   Loan term
   Final EMI
   Formats values properly for user readability.
# ALGORITHM
1. start
2. define function: calculate_emi(principal,annual_rate,years)
 a. Compute monthly intrest rate: monthly_rate=(annual_rate/12)/100
 b. Compute total number of months:months=years*12
 c. If monthly_rate==0
   EMI=principal/months
   return EMI
 d. Compute: EMI=principal*(monthly_rate*power_term)/(power_term-1)
 f.Round EMI to 2 decimals
   return EMI
3. Input Section
 a. Read principal amount P
 b. Read annual rate R
 c. Read loan terms
4. Calculate EMI
  monthly_payment = calculate_emi(P, R, Y)
5. Output Section
 a. Print loan amount
 b. Print loan term
 c. Print calculated EMI
6. End
# HOW TO RUN THE PROGRAM
1. Install Python (if not installed)
2. Download or clone this project
3. Open terminal and run:
   python main.py
4. Enter:
   - Principal Amount
   - Annual Interest Rate
   - Loan Duration (years)
# FUTURE ENHANCEMENT
1. Add GUI using Tkinter
2. Add amortization schedule
3. Export results to PDF
4. Build a mobile version
