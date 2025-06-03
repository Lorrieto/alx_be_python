pattern = int(input("Enter the size of the pattern: "))

row = 1 
column = range(1,pattern)
while row <= pattern:   
       
        for i in range(pattern):
            print("*", end="")
        print()
     

        row = row + 1
