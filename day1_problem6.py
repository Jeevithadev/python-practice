p = float(input("Enter Principle: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

def simpleInterest(p, r, t):
    si = (p * r * t) / 100
    print(f"Simple Interest of principle {p}, rate {r}%, time {t} Year = {si}")

simpleInterest(p, r, t)