print('******************Tip Calculator************************')
total_amt = float(input('Enter the total bill amount: '))
tip_perc = float(input('How much tip in percent you have to give eg. 12, 10, etc : '))
total_person = float(input('Total how many peoples are spliting for bill: '))
pay_amt = ((total_amt/100) * (100 + tip_perc)) / total_person
print(f'Each person have to pay {pay_amt} after adding the {tip_perc}% tip')
