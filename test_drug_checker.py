from drug_checker import drug_checker
import pytest

#sample prescription entry
prescription = "amlodipine,loratadine,diazepam"

def tester_list():
    #if the result of calling drug_checker passing in prescription as argument returns a value flagged
    #and the length of flagged is greater than zero then there is controlled
    assert len(drug_checker(prescription)[0]) >= 0

def tester_dict():
    #if the result of calling drug_checker passing in prescription as argument returns a value analysis
    if len(drug_checker(prescription)[0]) > 0:
        #as long as flagged is greater than zero assert "is_controlled" equals True else False
        assert drug_checker(prescription)[1]["is_controlled"] == True
    elif len(drug_checker(prescription)[0]) == 0:
        assert drug_checker(prescription)[1]["is_controlled"] == False

def tester_typeError():
    #raise a type error if invalid data type is passed into drug_checker as argument
    with pytest.raises(TypeError):
        drug_checker(4.4,True,6,[2,3,4,5])
