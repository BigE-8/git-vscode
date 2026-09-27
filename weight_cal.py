def main():
    height_square = pow(float(input("What is your height in meters: ")), 2)
    bmi = weight_calculator()/height_square
    print(bmi)

"""
OFFICIAL DOCUMENTATION of weight_calculator():
1. the function takes no parameter.
2. prompts user for a valid int or float input.
3. calculate weight of child based on age in years and then recommend ACT dosage regimen.
4. returns the weight of the child
5. Note: Traditional formula states weight = (Age(in years) + 4) *2
"""

#define the weight_calculator function
def weight_calculator():
    while True:
        #try to catch value error
        try:
            #request for user input "What's the child's age"
            age = int(input("What's the child's age: "))
            #check if a valid integer was entered
            if age > 0:
                # define weight
                weight = (age + 4) * 2

                #print the approximate weight 
                print(f"The weight of the child is approcimately {weight}kg")
                if weight <= 15:
                    print(f"Give 1 Tablet of 20/120mg ACT")
                elif weight <= 25:
                    print(f"Give 2 Tablets of 20/120mg ACT")
                elif weight < 35:
                    print(f"Give 3 Tablets of 120mg ACT")
                else:
                    print(f"Give Adult dose")
                break
            else:
                print("age must be greater than zero")
        except ValueError:
            print("INVALID ENTRY! ensure to type-in 'age' in figures")
    #return weight
    return weight

if __name__== "__main__":
    main()

