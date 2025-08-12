'''users_name = input("Enter your name: ")
print("Hello", users_name)'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
opt = input("Enter mathematical operator (only: -,+,/, or *): ")
if opt == '-':
    ans = num1 - num2
elif opt == '+':
    ans = num1 + num2
elif opt == '*':
    ans = num1 * num2
elif opt == '/':
    ans = num1 / num2
    
print(num1, opt, num2,"=", ans)