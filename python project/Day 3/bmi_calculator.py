print('******************BMI Calculator ************************')
weight = float(input('Enter your weight in KG: '))
height = int(input('Enter your height in Centimers : ')) / 100
bmi = weight / height ** 2
if bmi < 18.5:
    print(f'You are underweight with BMI = {bmi}') 
elif bmi > 18.5 and bmi < 24.9:
    print(f'You are Normal weigh with BMI = {bmi}') 
elif bmi > 25 and bmi < 29.9:
    print(f'You are Overweight with BMI = {bmi}') 
elif bmi > 30 and bmi < 35:
    print(f'You are Obese with BMI = {bmi}') 
elif bmi > 35:
    print(f'You are Morbid obesity with BMI = {bmi}') 