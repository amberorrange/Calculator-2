"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)


while True: 

    problem = input("Enter an equation: ")
    problem = problem.split(" ")
    op = problem[0]

    if op == "q":
        print("goodbye")
        break

    if len(problem) < 2:
        print("Not enough inputs")
        continue



    num1 = problem[1]
    if not num1.isdigit(): 
            print("use all digits")
            continue
    num1 = int(num1)
    
    if len(problem) > 2:
        num2 = problem[2]
        if not num2.isdigit():
            print("use all digits")
            continue
        num2= int(num2)
       

    if op == "+": 
       print(float(add(num1, num2)))

    elif op == "-": 
       print(float(subtract(num1, num2)))
    
    elif op == "*": 
       print(float(multiply(num1, num2)))
    
    elif op == "/": 
       print(float(divide(num1, num2)))
    
    elif op == "mod": 
       print(float(mod(num1, num2)))

    elif op == "square": 
       print(float(square(num1)))
    
    elif op == "cube": 
       print(float(cube(num1)))
    

     