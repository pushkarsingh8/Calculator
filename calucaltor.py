#Simple caluclator :-

def simple_calculator(result,a,b):
    #Print the available arithmetic operations
    print(f"\nChoose a Arithmetic operation:-\n{"~"*10}\n1.Addition (+)\n2.Subtraction (-)\n3.Division (/)\n4.Multiplaction (*)\n")
    while True:
        #Prompt the user to enter an operation
        user = (input("> "))
        
        
        #Perform the user to enter an operation
        if user == '+':
            return f"{result} {a+b}" 
        
        elif user == '-':
            return f"{result} {a-b}"
        
        elif user == '/':
            if b != 0:
                return f"{result} {a/b}"
            #handle error of divisible by zero
            else:
                print("can't divide by 0")
            
        elif user == '*':
            return f"{result} {a*b}"
        else:
            print("Invalid Operation")
            user = int(input("> "))    
    
    
    
num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))
        
print(simple_calculator("Result: ", num1,num2))