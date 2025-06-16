def safe_divide(numerator, denominator):
    try:
        division= float(numerator)/ float(denominator)
        print("The result of the division is", division)
        return division
        
    except ZeroDivisionError:
       print("Error: Cannot divide by zero.")

    except ValueEror:
       ("Error: Please enter numeric values only.")
    
