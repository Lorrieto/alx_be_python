def safe_divide(self,numerator, denominator):
    self.division= float(numerator)/ float(denominator)
   

try:
     print("The result of the division is", self.division)
    

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueEror:
    ("Error: Please enter numeric values only.")
    
