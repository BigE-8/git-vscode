import sys
import re
from wordsegment import load, segment
from drug_checkers import drug_checker
from processors import file_processor
from logins import login

print("="*25+"OPENING PROGRAM"+"="*25)
print()
def main():
    while True:
        try:
            file = sys.argv[1]
            break
        except IndexError:
            print(f"Too few arguments on the command-line")
    login()        
    print("-"*15,"OPENING OFFICE FILE","-"*15, end="\n")
    print()
    file_processor(file)
    print("-"*15,"CLOSING OFFICE FILE","-"*15, end="\n")
    print()
    print("-"*15,"VETTING PRESCRIPTIONS","-"*15, end="\n")
    drugs = input("enter the prescription: ")
    drug_checker(drugs)
    
print("="*25+"CLOSING PROGRAM"+"="*25)

if __name__=="__main__":
    main()


