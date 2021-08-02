#AlI_MaHdIyAnJoO

print("wellcome to BMI calculator")
name = input("what is your name? ")
type_of_calculation = input("standard or metric? ")

stan = "standard"

if type_of_calculation == stan:

    weight = float(input("what is your weight(lb)? "))
    hight = float(input("how tall are you(in)? "))
    BMI = weight / hight ** 2 * 703 
    BmI = round(BMI, 2)

    print(f"Hi {name} your BMI is {BmI}") 

    if BmI < 18.5:
       print("your state is underweight")
    elif BmI < 25:
        print("your state is normal")
    elif BmI < 30:
        print("your state is overweight")
    else:
        print("your state is Obese")

elif type_of_calculation == "metric":

    weight = int(input("what is your weight(kg)? "))
    hight = float(input("how tall are you(m)? "))
    BMI = weight / hight ** 2  
    BmI = round(BMI, 2)

    print(f"Hi {name} your BMI is {BmI}") 

    if BmI < 18.5:
       print("your state is underweight")
    elif BmI < 25:
        print("your state is normal")
    elif BmI < 30:
        print("your state is overweight")
    else:
        print("your state is Obese")
