
status = True
bit_dic = {'name':'',
           'amt':0}
while status:
    name = input("Enter your Name: ")
    amt = int(input("Enter you bit amount(Rs):"))
    if bit_dic['amt'] < amt:
        bit_dic['name'] = name
        bit_dic['amt'] = amt
    
    more_bit = input("Do you wants to Add more bit Amount Type ? Yes or No: ").lower()
    
    if more_bit == 'no' :
        status = False

print(f"{bit_dic['name']} has maximum bit Amount {bit_dic['amt']} Rs.")   
            