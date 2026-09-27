def main():
    drugs = input("enter the list of prescription: ")
    drug_checker(drugs)

"""
OFFICIAL DOCUMENTATION of drug_checker(): 
1. the function takes just a named parameter called "medication".
2. formats the users input into a list iterates over the list, 
generates a dictionary called "analysis" from the analyzing the list to find matches that's in controlled.
3. it looks for matches in controlled medication set stores the flagged medications in a "flagged" variable.
4. it prints the analysis results but also returns two values "flagged" and "analysis" 
"""
#define #drug_checker
def drug_checker(medication):
    #use list comprehension to create a list from users input
    prescription = [med.strip().title() for med in medication.split(",")]
    #a set of controlled medications
    controlled = {"Misoprostol", "Diazepam", "Digoxin", "Codeine", "Pregabalin", "Amytriptillin", "Co-codamol"}
    #create an empty list which you will uses to house flagged medications
    flagged = []
    #create a key value pair
    analysis = {"count": len(prescription), "is_controlled": False, "flag": flagged}
    #iterate over prescription list
    for c in prescription:
        #if an item in prescription list happens to be among the set of controlled medications?
        if c in controlled:
            #update the value of the key "is_controlled" to True
            analysis["is_controlled"] = True
            #add that very controlled medication to flagged list
            flagged.append(c)
    print(f"Total drugs in prescription: {analysis["count"]}")
    #if there is at least one controlled med do this
    if len(flagged) < 2 and analysis["is_controlled"]:
        print(f"Warning!!! This prescription contains a controlled substance {flagged}")
    #if multiple controlled do this
    elif len(flagged) > 1 and analysis["is_controlled"]:
        print(f"Warning!!! This prescription contains the following controlled substances:")
        print("_"*20)
        #iterate over flagged then print each flagged medication in a new line
        for i in flagged:
            print(i)
        print("_"*20)
    print(f"Total number of flagged medication: {len(analysis["flag"])}")
    print()
    #return a list of values which can be used whenever the function is called
    return flagged, analysis  
     
if __name__=="__main__":
    main()     
    
