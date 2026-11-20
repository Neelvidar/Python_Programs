# Q1: Read a file and count how many vowels are present in its content
with open("sample.txt", "r") as f:
    content = f.read()
 
vowels = "aeiouAEIOU"
count = 0
for ch in content:
    if ch in vowels:
        count += 1
 
print("Total vowels in file:", count)
