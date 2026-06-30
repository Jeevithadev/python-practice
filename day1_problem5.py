import ast

v1 = input("Enter variable1: ")
v2 = input("Enter variable2: ")

try:
    v1 = ast.literal_eval(v1)
    v2 = ast.literal_eval(v2)
except:
    pass

def swap2Variable(v1, v2):
    v1, v2 = v2, v1
    print (f"Variable1 = {v1} \n Variable2 = {v2}")

swap2Variable(v1, v2)