number = []

for i in range(3):
    num = float(input(f"Enter number {i+1}: "))
    number.append(num)

def average(number):
    sum = 0
    for i in number:
        sum = sum + i
    avg = sum / 3
    print(f"Average of 3 number = {avg}")

average(number)