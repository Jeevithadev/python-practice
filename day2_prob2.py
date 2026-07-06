s = input("Enter a string to check it is a palindrome or not: ")

def palindrome(s):
    rev = s[::-1]
    print("Normal palindrome: ")
    if rev == s:
        print(f"Entered string {s} is a Palindrome.")
    else:
        print(f"Entered string {s} is not a Palindrome.")

def palindromeCaseinsensitive(s):
    cleaned = s.casefold()
    rev = cleaned[::-1]
    print("Palindrome Case-insensitive:")
    if rev == cleaned:
        print(f"Entered string {s} is a Palindrome.")
    else:
        print(f"Entered string {s} is not a Palindrome.")

palindrome(s)
palindromeCaseinsensitive(s)