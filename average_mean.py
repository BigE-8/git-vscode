def main():
    x = input("Enter the list of numbers: ")
    y = my_mean(x)
    print(y)

"""
OFFICIAL DOCUMENTATION of my_mean():
1. the function takes a named parameter called "prompt".
2. validates the type of argument that was passed in.
3. if the value of the argument is valid the function formats the argument into a list.
3. iterates over the list, convert elements to floats and sum up elements
4. sum is divided by the length of the list and returned. returned value is "Mean"
"""

#define my_mean function that take prompt as sole parameter
def my_mean(prompt):
    try:
        #validate user's input
        if type(prompt) is int or float:
            #format the user's input
            formatted_prompt = [number.strip() for number in prompt.split(",")]    
            #create a variable to sum up the individual items of the formatted list
            total = 0
            #loop through the formatted list
            for score in formatted_prompt:
                #add the items up and store in the total variable
                total += float(score)
            #return the value of mean converted to two decimal places
            #where mean is the value from dividing total with the number of item in the formatted list
            return total/len(formatted_prompt)
        
    #handle exceptions like ValueError that may occur if invalid value is inputed by user
    except ValueError:
       print("INVALID DATA TYPE: prompt entered was not integer or float.")
       #return the invalid data back to the caller
       
    
#only call main if __name__ is __main 
if __name__=="__main__":
    main() 