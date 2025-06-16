def safe_divide(numerator, denominator):
    try:
        result = float(numerator)/ float(denominator)
        return "The result of the division is", division
        
    except ZeroDivisionError:
       print("Error: Cannot divide by zero.")

    except ValueEror:
       ("Error: Please enter numeric values only.")
    
