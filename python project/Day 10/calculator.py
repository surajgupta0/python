print('******************Calculator**********************')

def add(a,b):
    return a+b

def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b

def div(a,b):
    return a/b

fnum = int(input('Enter First number: '))
status = True
while status == True:
    print(f"\nOperation with {fnum}:")
    print("1. Type '+' for Addition")
    print("2. Type '-' for Substraction")
    print("3. Type '*' for Multiplication")
    print("4. Type '/' for Division")
    opration = input("\nSelect Operation: ")
    op = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    snum = int(input('Enter Second number: '))
    result = op[opration](fnum,snum)
    print(f"Result: {fnum} {opration} {snum} = {result}")
    more_operation = input(f"\nDo you want to do opration with {result}?(Y/N): ")
    if more_operation.lower() == 'y':
        fnum = result
    else:
        status = False
              
