# Count the Vowels from accepting from user
user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in user_input:
    if char in vowels:
        count += 1

print("Total number of vowels:", count)
