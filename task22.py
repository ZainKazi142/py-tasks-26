#Aim: WAP to create a function to add numbers passed to it and return Sum. the user may call the function with 2,3,4... arguments the function should do addition for any number of arguments passed.
#Coder: Zain Mohamed Saeed Kazi

sum = 0
def calcAdd(n):
    global sum
    for i in n:
        sum = sum + i


numbers = list(map(int, input("Enter the numbers to be added: ").split()))
calcAdd(numbers)
print(f"The sum of the numbers entered is {sum}")
