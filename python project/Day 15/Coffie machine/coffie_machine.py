from coffie_menu import menu

# List of Ingredients 
ingredients = {
    "water" : {"quontity": 500, "unit" : "ml"},
    "coffee" : {"quontity": 500, "unit" : "grams"},
    "milk" : {"quontity": 400, "unit" : "ml"},
    "foam" : {"quontity": 200, "unit" : "ml"},
    "chocolate" : {"quontity": 250, "unit" : "grams"}
}

# List of currency 
currency = {
    "rupees" : 1,
    "dollar" : 83.54,
    "pound" : 106.28,
    "kuwaity dinar": 272.47,
    "euro": 90.26
}

total_amt = 0.0
status = True
select_coff = ''
coff_amount = ''
coff_ingredints = {}

# Used to get the report of the coffie 
def print_report():
    
    print("\nReport:")
    
    for ingred in ingredients:
        print(f"{ingred} = {ingredients[ingred]['quontity']} {ingredients[ingred]['unit']}")
        
    print(f"Total Amount = {total_amt} Rs")
    
    want_more = input('Do you want to purchase coffie? Type Y for yes otherwise N for No: ')
    if want_more.lower() == 'n':
        status = False

# Used to Serve the coffie 
def make_coffie(select_coff, user_amt):
    global total_amt , status, coff_amount, coff_ingredients
    
    # Decrement quontity from the Ingredient list as coffie is serverd to user and increase the amount of the machine balance
    for i in coff_ingredients:
        ingredients[i]['quontity'] -= coff_ingredients[i]
    total_amt += coff_amount
    
    #if user have balace the return it
    if user_amt > coff_amount:
        print(f"Please Collect your remaining amount {user_amt -  coff_amount} Rs..")
    
    #Print successfull message as coffie is served
    print(f"Here is your {select_coff}, Enjoy your Coffie sir.")
    
    #Wants more coffie
    want_more = input('Do you want to purchase more ? Type Y for yes otherwise N for No: ')
    if want_more.lower() == 'n':
        status = False

# Used to get amount from user and convert that amount in rupees  
def get_amount():
    print("\nSelect you currency")
    curr_count = 1
    for curr in currency:
        print(f"{curr_count}. Type {curr}")
        curr_count += 1
    select_curr = input("\nType Here: ")
    
    if select_curr not in currency:
        print("Incorrect Currency")
        while select_curr not in currency:
            select_curr = float(input("\nType Here: "))
            print("Incorrect Currency")
    else:
        user_amt = float(input("Enter Amount: "))
        return user_amt * currency[select_curr]
        
# Used for Selecting Coffie from user 
def select_coffie():
    print("\nPlease Select any of the Coffie from below Menu")
    coff_count = 1
    for coffie in menu:
        print(f"{coff_count}. Type {coffie} for {menu[coffie]['cost']} Rs.")
        coff_count += 1
    print(f"{coff_count}. Type Report")
    print(f"{coff_count + 1}. Type Exit")
    
    select_coff = input("\nType Here: ")
    return select_coff


#Used to know wheter Ingredients are available or not
def can_have(coffie):
    coffie_ingredients = menu[coffie]['ingredients']
    for ingred in coffie_ingredients:
        if coffie_ingredients[ingred] > ingredients[ingred]['quontity']:
            return f"There is {coffie_ingredients[ingred] - ingredients[ingred]['quontity']} {ingredients[ingred]['unit']} less amount of {ingred}"
    return True
        
        
while status:    
    
    # selecting a coffie 
    select_coff = select_coffie()
    
    #if coffie name is correct
    if select_coff in menu:
        
        coff_amount = menu[select_coff]['cost']
        coff_ingredients = menu[select_coff]['ingredients']
        
        #check wheter ingredients are available
        can_have_coffie = can_have(select_coff)
        
        #if true then get the amount
        if can_have_coffie == True:
            user_amt = get_amount()
            
            #check amount enter is less the cost or not
            if user_amt < coff_amount:
                
                #Loop for getting sufficience from user 
                while user_amt < coff_amount:
                    print(f"You have entered {coff_amount - user_amt} Rs. less, Please Select Currency again.")
                    user_amt = get_amount()
            make_coffie(select_coff, user_amt)
        else:
            print(can_have_coffie)
            
    #Print the report
    elif select_coff == 'report':
        print_report()
    
    #Exit the program
    elif select_coff == 'exit':
        status = False
    #Print no availability message if coffie not found 
    else:
        print("This item is not available here, please select ")
            
    
        
            
        