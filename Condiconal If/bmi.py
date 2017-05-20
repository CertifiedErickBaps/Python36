def bmi(weight, height):
    index = weight / height ** 2
    if index < 20:
        return "underweight"
    elif index < 25:
        return "normal"
        
    elif index < 30:
        return "obesel"
        
    elif index < 40:
        return "obese2"
        
    else:
        return "obese3"
        
def main():
    print(bmi(56, 1.90))
    print(bmi(60, 1.60))
    print(bmi(80, 1.65))
    print(bmi(150, 1.40))
    print(bmi(200, 1.20))
    
main()