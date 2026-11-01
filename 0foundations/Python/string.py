#  
marks = {
    "utkarsh": 98,
    "harsh": 99,
    "rohan": 97,
    8 : "sohil"
}
# print(marks["utkarsh"])# ans will come now as utkarsh is key in marks dictionary
# # print(marks[99]) #key error as 99 is not key in marks dictionary
# print(marks[8])
# print(marks.keys())
# print(marks.values())   
# print(marks.items())
# marks["utkarsh"]=100 #updating value of key utkarsh
marks.update({"harsh": 100,"mom" : 44}) #updating value of key harsh
print(marks)

print(marks.get("rohan")) #99
print(marks.get("rahul")) #none as rahul is not present in marks dictionary





