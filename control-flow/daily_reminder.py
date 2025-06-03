task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:

    case "high":
      if time_bound == "yes":
        print("Reminder: ", task, "is a high priotity task that requires immediate attention today!")

      else:
        print("Reminder: ", task, "is a high priotity task. Consider competing it when you have free time")

            
    case "medium":
         
        if time_bound == "yes":
             print("Reminder: ",task," is a medium priotity task that requires immediate attention today!")

        else:
             print("Reminder: ", task, "is a medium priotity task. Consider competing it when you have free time")
         

    case "low":
         
        if time_bound == "yes":
             print("Reminder: ", task, "is a low priotity task that requires immediate attention today!")

        else:
             print("Reminder: ", task, "is a low priotity task. Consider competing it when you have free time")
         
    
