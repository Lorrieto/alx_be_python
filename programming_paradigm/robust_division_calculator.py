
    
def safe_divide(float(numerator), float(denominator)):
    division_= float(numerator/denominator)
    print("The result of the division is", division_)

try:
    print(" ")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueEror:
    ("Error: Please enter numeric values only.")
    
    
