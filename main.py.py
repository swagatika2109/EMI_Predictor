import math
# 1. Define the Calculation Function
def calculate_emi(principal, annual_rate, years):
    """Calculates the Equated Monthly Installment (EMI)."""
    monthly_rate = (annual_rate / 12) / 100
    months = years * 12
    # Avoid division by zero in case of 0% interest
    if monthly_rate == 0:
        return principal / months
    # Apply the EMI formula: P * [R * (1 + R)^N] / [(1 + R)^N - 1]
    power_term = math.pow((1 + monthly_rate), months)
    emi = principal * (monthly_rate * power_term) / (power_term - 1)
    return round(emi, 2)
# 2. User Input
P = float(input("Enter Loan Principal Amount: "))
R = float(input("Enter Annual Interest Rate (%): "))
Y = int(input("Enter Loan Term (Years): "))
# 3. Output Calculation
monthly_payment = calculate_emi(P, R, Y)
# 4. Clear Output
print("\n--- EMI Calculation Result ---")
print(f"Loan Amount: ₹{P:,.2f}")
print(f"Loan Term: {Y} years")
print(f"Your Monthly EMI will be: ₹{monthly_payment:,.2f}")
