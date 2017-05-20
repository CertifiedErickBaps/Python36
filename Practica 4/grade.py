# Authors: 
#         A01379896 Erick Bautista Pérez
# Write a program called grade.py. Define in this program a function called grade(score) 
#that returns a string with the corresponding letter grade for a given numerical score. 
#Use the values from the following table:
#
# September 23, 2016.
def grade(score):
       
    if 0 <= score <= 49:
        return "F"
    elif 50 <= score <= 69:
        return "D"
    elif 70 <= score <= 84:
        return "C"
    elif 85 <= score <= 94:
        return "B"
    elif 95 <= score <= 100:
        return "A"
    else:
        return "Error"
        
def main():
    score = int(input("Give me a score between 0 and 100: "))
    x = grade(score)
    print("The grade is: ", x)
   
main()