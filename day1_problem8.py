seconds = int(input("Enter the total seconds: "))

def seconds_converter(s):
    hours = s // 3600
    min = (s % 3600) // 60
    sec = s % 60

    print(f"{hours}hr {min}min {sec}sec")

seconds_converter(seconds)