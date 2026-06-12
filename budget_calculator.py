"""
Cozy Budget Calculator
----------------------
A desktop budget calculator built with Tkinter.

Features:
- Total income input
- Expense category inputs
- Dynamic expense addition
- Remaining balance calculation
- Savings percentage tracking
- Spending threshold alerts
- Input validation using try/except
- Cozy pastel UI design

All variable names, function names, and comments are written in English.
"""

import tkinter as tk
from tkinter import messagebox


# ==========================================================
# COLOR PALETTE CONSTANTS (Soft Cozy Pastel Theme)
# ==========================================================
BACKGROUND_COLOR = "#FFC0CC"      # Pastel pink background
CARD_COLOR = "#FED5D2"            # Pastel pink card background
ACCENT_MINT = "#CFE8D5"           # Pastel mint
ACCENT_PINK = "#F6D6D6"           # Pastel pink
ACCENT_LAVENDER = "#E5D9F2"       # Light lavender
TEXT_COLOR = "#4A4A4A"            # Dark gray
SUCCESS_COLOR = "#D8F0D2"         # Soft green
WARNING_COLOR = "#FFE0B5"         # Soft orange
ALERT_COLOR = "#F5C2C7"           # Soft red
BORDER_COLOR = "#FFFFFF"

SAFE_THRESHOLD = 0.85  # 85%


class BudgetCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Cozy Budget Calculator")
        self.root.geometry("850x650")
        self.root.configure(bg=BACKGROUND_COLOR)

        # List that stores all expense entries dynamically
        self.expense_entries = []

        # ==========================
        # TITLE SECTION
        # ==========================
        title_label = tk.Label(
            root,
            text="☁ Budget Calculator ☁",
            font=("Helvetica", 22, "bold"),
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR
        )
        title_label.pack(pady=15)

        # ==========================
        # MAIN CONTAINER
        # ==========================
        self.main_frame = tk.Frame(
            root,
            bg=CARD_COLOR,
            bd=2,
            relief="solid",
            padx=20,
            pady=20
        )
        self.main_frame.pack(fill="both", expand=True, padx=25, pady=10)

        # ==================================================
        # INCOME SECTION
        # ==================================================
        income_frame = tk.Frame(
            self.main_frame,
            bg=CARD_COLOR,
            padx=10,
            pady=10
        )
        income_frame.grid(row=0, column=0, sticky="ew", pady=10)

        income_label = tk.Label(
            income_frame,
            text="Total Income:",
            font=("Helvetica", 12, "bold"),
            bg=CARD_COLOR,
            fg=TEXT_COLOR
        )
        income_label.grid(row=0, column=0, sticky="w")

        self.income_entry = tk.Entry(
            income_frame,
            width=20,
            font=("Helvetica", 11)
        )
        self.income_entry.grid(row=0, column=1, padx=10)

        # ==================================================
        # EXPENSE SECTION
        # ==================================================
        expense_title = tk.Label(
            self.main_frame,
            text="Expense Categories",
            font=("Helvetica", 14, "bold"),
            bg=CARD_COLOR,
            fg=TEXT_COLOR
        )
        expense_title.grid(row=1, column=0, sticky="w", pady=(10, 5))

        # Container for dynamic expense rows
        self.expense_frame = tk.Frame(
            self.main_frame,
            bg=CARD_COLOR,
            bd=1,
            relief="solid",
            padx=10,
            pady=10
        )
        self.expense_frame.grid(row=2, column=0, sticky="nsew")

        # Configure grid expansion
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Add default expense categories
        self.add_expense_row("Food")
        self.add_expense_row("Transport")
        self.add_expense_row("Entertainment")
        self.add_expense_row("Utilities")

        # ==================================================
        # BUTTONS SECTION
        # ==================================================
        button_frame = tk.Frame(self.main_frame, bg=CARD_COLOR)
        button_frame.grid(row=3, column=0, pady=15)

        add_button = tk.Button(
            button_frame,
            text="+ Add Expense Category",
            bg=ACCENT_MINT,
            fg=TEXT_COLOR,
            font=("Helvetica", 10, "bold"),
            padx=12,
            pady=8,
            command=self.add_custom_expense
        )
        add_button.grid(row=0, column=0, padx=5)

        calculate_button = tk.Button(
            button_frame,
            text="Calculate Budget",
            bg=ACCENT_LAVENDER,
            fg=TEXT_COLOR,
            font=("Helvetica", 10, "bold"),
            padx=12,
            pady=8,
            command=self.calculate_budget
        )
        calculate_button.grid(row=0, column=1, padx=5)

        # ==================================================
        # RESULTS SECTION
        # ==================================================
        result_frame = tk.Frame(
            self.main_frame,
            bg=CARD_COLOR,
            bd=1,
            relief="solid",
            padx=15,
            pady=15
        )
        result_frame.grid(row=4, column=0, sticky="ew", pady=10)

        self.balance_label = tk.Label(
            result_frame,
            text="Remaining Balance: $0.00",
            font=("Helvetica", 16, "bold"),
            bg=CARD_COLOR,
            fg=TEXT_COLOR
        )
        self.balance_label.pack(pady=5)

        self.savings_label = tk.Label(
            result_frame,
            text="Savings Percentage: 0.00%",
            font=("Helvetica", 13),
            bg=CARD_COLOR,
            fg=TEXT_COLOR
        )
        self.savings_label.pack(pady=5)

        self.alert_label = tk.Label(
            result_frame,
            text="",
            font=("Helvetica", 11, "bold"),
            bg=CARD_COLOR,
            fg="#B25D5D",
            wraplength=700,
            justify="center"
        )
        self.alert_label.pack(pady=5)

    # ==========================================================
    # FUNCTION: ADD EXPENSE ROW
    # ----------------------------------------------------------
    # Creates a new expense row using Tkinter grid layout.
    # Each row contains:
    # - Category name entry
    # - Expense amount entry
    # ==========================================================
    def add_expense_row(self, category_name=""):
        row_index = len(self.expense_entries)

        category_entry = tk.Entry(
            self.expense_frame,
            width=25,
            font=("Helvetica", 10)
        )
        category_entry.grid(row=row_index, column=0, padx=5, pady=5)

        category_entry.insert(0, category_name)

        amount_entry = tk.Entry(
            self.expense_frame,
            width=15,
            font=("Helvetica", 10)
        )
        amount_entry.grid(row=row_index, column=1, padx=5, pady=5)

        self.expense_entries.append(
            (category_entry, amount_entry)
        )

    # ==========================================================
    # FUNCTION: ADD CUSTOM EXPENSE
    # ----------------------------------------------------------
    # Called when user presses the add button.
    # Adds an empty expense row dynamically.
    # ==========================================================
    def add_custom_expense(self):
        self.add_expense_row()

    # ==========================================================
    # FUNCTION: CALCULATE BUDGET
    # ----------------------------------------------------------
    # Handles:
    # - Validation using try/except
    # - Expense calculations
    # - Savings percentage
    # - Threshold warnings
    # ==========================================================
    def calculate_budget(self):

        try:
            total_income = float(self.income_entry.get())

            if total_income <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid numeric income."
            )
            return

        total_expenses = 0
        warning_messages = []

        # Process all expense rows
        for category_entry, amount_entry in self.expense_entries:

            category_name = category_entry.get().strip()

            if category_name == "":
                category_name = "Unnamed Category"

            amount_text = amount_entry.get().strip()

            if amount_text == "":
                expense_amount = 0

            else:
                try:
                    expense_amount = float(amount_text)

                except ValueError:
                    messagebox.showerror(
                        "Invalid Input",
                        f"Expense value for '{category_name}' must be numeric."
                    )
                    return

            total_expenses += expense_amount

            # Category threshold alert
            if expense_amount > total_income * SAFE_THRESHOLD:
                warning_messages.append(
                    f"⚠ {category_name} alone exceeds 85% of your income."
                )

        balance = total_income - total_expenses

        savings_percentage = (balance / total_income) * 100

        # Total spending threshold alert
        if total_expenses > total_income * SAFE_THRESHOLD:
            warning_messages.append(
                "⚠ Your total spending exceeds 85% of your income."
            )

        # Negative balance alert
        if balance < 0:
            warning_messages.append(
                "⚠ Your expenses are greater than your income."
            )

        # Update balance display
        self.balance_label.config(
            text=f"Remaining Balance: ${balance:.2f}"
        )

        # Update savings percentage display
        self.savings_label.config(
            text=f"Savings Percentage: {savings_percentage:.2f}%"
        )

        # Update result colors
        if balance >= 0:
            self.balance_label.config(
                bg=SUCCESS_COLOR
            )
        else:
            self.balance_label.config(
                bg=ALERT_COLOR
            )

        # Display warning messages
        if warning_messages:
            self.alert_label.config(
                text="\n".join(warning_messages)
            )
        else:
            self.alert_label.config(
                text="✓ Great job! Your spending is within a healthy range."
            )


# ==========================================================
# APPLICATION ENTRY POINT
# ----------------------------------------------------------
# Creates the Tkinter window and starts the event loop.
# The event loop keeps the GUI responsive and listening
# for button clicks and user interactions.
# ==========================================================
def main():
    root = tk.Tk()
    app = BudgetCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()