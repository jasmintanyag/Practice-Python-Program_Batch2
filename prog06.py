#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

total_dif = 0
for i in range(10):
    num = float(input(f"Enter a number ({i+1}): "))
    if i == 0:
        total_dif += num
    else:
        total_dif -= num
print(total_dif)