def splitString(action = "", equation = ""):
    equation = equation.split()
    temp = []

    if action == "num":
        temp.append(int(equation[0]))
        temp.append(int(equation[2]))

        return temp
    else:
        return equation[1]

def power(num = []):
    temp = num[0]
    for x in range(num[1]):
        temp = temp * num[0]
    
    return temp

equation = input("Enter Equation: ")
num = splitString("num", equation)
action = splitString("action", equation)

def calculation(action):
    if action == "+":
        return num[0] + num[1]
    elif action == '-':
        return num[0] - num[1]
    elif action == '*':
        return num[0]*num[1]
    elif action == '/':
        return num[0]/num[1]
    elif action == '^':
        return power(num)

print("Your answer is: " + str(calculation(action)))
