year = int(input("Enter the year: "))

if year % 400 == 0: ## we used it hear because the raseon is realted to physics
    print("It's a leap year")
elif year % 100 == 0:
    print("It's not a leap year")
elif year % 4 == 0: ## we use 4 because 400 is too strict and most leap years are missed but stii we do it 
                    ## 4 actually calculates the missed years basically
    print("It's a leap year")
else:
    print("It's not a leap year")