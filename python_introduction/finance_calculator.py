monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expenses: "))
monthly_savings = int (monthly_income - monthly_expense)
projected_savings = int (monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print ("Your monthly savings are ", monthly_savings)
print ("Projected savings after one year, with interest, is", projected_savings)
