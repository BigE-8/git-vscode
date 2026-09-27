import sys
import csv

def main():
    try:
        file = sys.argv[1]
        file_processor(file)
    except IndexError:
        sys.exit(f"Too few arguments on the command-line")
"""
OFFICIAL DOCUMENTATION of file_processor():
1. the function takes a named parameter called "filename".
2. validates the number of argument passed at the command_line. if more than one.
   it validates if the filename(second argument at CLI) ends with "txt" or "csv"
a- if it's a "txt" file it processes and returns a value called "summation"(total weekly sales)
b- if it's a "csv" file it processes and returns a list of dictionaries called "drugs"
c- if it's neither then it raises an exception valueError
3. if file is "txt or csv" but doesnt exist, it raises an exception FileNotFound
"""

#define the function
def file_processor(filename):    
    try:
        #confirm if more than one arguments was passed in at the Command-line interface
        if len(sys.argv) > 1:
            #verify if file is text format
            if filename.lower().endswith(".txt"):
                #create two lists to store upper limit entry and every entry respectively
                file_count = []
                upper_limit = []
                #open the file in read mode
                with open(filename) as file:
                    #iterate over the lines in the file
                    for i in file:
                        line = int(i)
                        #if entry is over $120 add to upper limit list
                        if line >= 120:
                            upper_limit.append(line)
                            print(f"Daily Target Achieved. ${line} is above target $120")
                        #enter ever entry irrespective of amount in the file_count list
                        file_count.append(line)
                        #once there are 7 file_count entries close the ledger for the week and return total sales
                        if len(file_count) == 7:
                            print(f"ledger for the week is closed please enter in ${line} in a new ledger")
                            print(f"the number of the entries in {filename}: {len(file_count)}")
                            print(f"the number of the entries above $120: {len(upper_limit)}")
                            sumation = sum(file_count)
                            print(f"The weekly sales total = ${sumation}")
                            print()
                            #return total weekly sales
                            return sumation
                        
            #else if file is csv create a list called drugs
            elif filename.lower().endswith(".csv"):
                drugs = []
                #open the file in read mode
                with open(filename) as file:
                    #use a csv dictreader to parse the csv 
                    reader = csv.DictReader(file)
                    #iterate over reader, each row is a column of dictionary
                    for row in reader:
                        #add each row to the "drugs" list creating a "list of dictionaries"
                        drugs.append({"name": row["name"], "classification": row["classification"], "price": row["price"]})
                #iterate over the list of dictionaries
                for drug in drugs:
                    print(f"{drug["name"]} is classified as {drug["classification"]} and it costs ${drug["price"]}")
                print()
                #return a list of the drugs
                return drugs
            else:
                #raise a valueError
                raise ValueError
            
    #handle the exception
    except FileNotFoundError:
        print("INVALID FILE: enter a file that exists")
    except ValueError:
        print(f"Unsupported file extention ({filename}): only '.txt' and '.csv' are allowed.")
        
    
if __name__=="__main__":
    main()