# Budget Calculator

## Project Overview

**Budget Calculator** is a desktop application built with Python and Tkinter that helps users calculate their monthly budget. The application allows users to enter their total income, record expenses across multiple categories, and instantly view their remaining balance and savings percentage.

The application also provides spending alerts when expenses exceed predefined thresholds, helping users become more aware of their financial habits.

The graphical interface uses a soft pastel color palette designed to create a comfortable and user-friendly experience.

---

## Features

* Enter total monthly income.
* Add expenses using predefined categories:

  * Food
  * Transport
  * Entertainment
  * Utilities
* Dynamically add custom expense categories.
* Calculate total expenses and remaining balance.
* Display the percentage of income that remains after expenses.
* Validate user input using `try/except` blocks.
* Show alerts when:

  * A single expense category exceeds 85% of the total income.
  * Total spending exceeds 85% of the total income.
  * Total expenses are greater than total income.
* Replace empty category names with `"Unnamed Category"`.
* Treat empty expense fields as a value of `0`.
* Provide a pastel-themed graphical user interface built with Tkinter.

---

## Installation

### Prerequisites

Make sure you have **Python 3** installed on your computer.

Tkinter is included with most standard Python installations.

### Clone or Download the Project

```bash
git clone <https://github.com/mxnixcc/budget_calculator.git>
```

or download the project files manually.

### Run the Application

Open a terminal in the project directory and execute:

```bash
python main.py
```

> Replace `main.py` with the actual filename if your Python script uses a different name.

---

## How to Use

### 1. Launch the Application

Run the Python file to open the Cozy Budget Calculator window.

### 2. Enter Total Income

Type your monthly income into the **Total Income** field.

* The value must be numeric.
* The value must be greater than zero.

If the input is invalid, an error message will appear.

### 3. Enter Expense Amounts

The application initially provides four expense categories:

* Food
* Transport
* Entertainment
* Utilities

Enter the amount spent for each category.

Notes:

* Empty expense fields are interpreted as `0`.
* Expense values must be numeric.

### 4. Add Additional Expense Categories

Click the **"+ Add Expense Category"** button to create a new expense row.

Each new row contains:

* A category name field.
* An expense amount field.

If the category name is left blank, the application automatically labels it as **"Unnamed Category"** during the calculation process.

### 5. Calculate the Budget

Click the **"Calculate Budget"** button.

The application will:

1. Validate the income value.
2. Validate all expense amounts.
3. Sum all expenses.
4. Calculate the remaining balance.
5. Calculate the savings percentage.
6. Generate spending alerts when applicable.
7. Update the result section of the interface.

---

## Calculation Logic

### Remaining Balance

```text
Remaining Balance = Total Income − Total Expenses
```

### Savings Percentage

```text
Savings Percentage = (Remaining Balance ÷ Total Income) × 100
```

### Spending Threshold

The application uses a safety threshold of **85% of total income**.

Warnings are displayed when:

* An individual expense category exceeds 85% of the user's income.
* Total expenses exceed 85% of the user's income.

Additional warnings are shown when expenses exceed income.

---

## Example Usage

### Input

```text
Total Income: $3000

Food: $500
Transport: $200
Entertainment: $150
Utilities: $250
Healthcare: $300
```

### Calculations

```text
Total Expenses: $1400
Remaining Balance: $1600
Savings Percentage: 53.33%
```

### Result Display

```text
Remaining Balance: $1600.00
Savings Percentage: 53.33%

✓ Great job! Your spending is within a healthy range.
```

---

## Validation Rules

### Income Validation

The application requires the income value to:

* Be numeric.
* Be greater than zero.

Otherwise, the following error message is displayed:

```text
Please enter a valid numeric income.
```

### Expense Validation

Expense values must be numeric.

If a non-numeric value is entered, the application displays an error message indicating which category contains the invalid input.

---

## User Interface

The application uses a cozy pastel theme composed of:

* Pastel pink backgrounds.
* Mint accent colors.
* Lavender action buttons.
* Soft green indicators for positive balances.
* Soft red indicators for negative balances.

The remaining balance label changes color depending on the calculation result:

* Green background for non-negative balances.
* Red background for negative balances.

---

## Future Improvements

The following enhancements are not currently implemented but could be considered in future versions:

* Save and load budget data from files.
* Generate visual charts for spending analysis.
* Edit or remove expense categories.
* Export budget reports.
* Track budgets across multiple months.
* Add recurring expense management.

---

## Technologies Used

* Python
* Tkinter

---

## Application Entry Point

The application starts by creating a Tkinter window and launching the event loop:

```python
if __name__ == "__main__":
    main()
```

The event loop keeps the interface responsive and handles user interactions such as button clicks and data entry.
