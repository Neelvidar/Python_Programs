def replace_vowels_with_z(text):
  # Define vowels (both lowercase and uppercase)
  vowels = "aeiouAEIOU"

  # Replace each vowel with 'Z' (preserving case if needed, or just 'Z')
  # Here we replace any vowel character with 'Z'
  result = "".join("Z" if char in vowels else char for char in text)
  return result


# Take input from the user
user_input = input("Enter a string: ")

# Process the string
modified_string = replace_vowels_with_z(user_input)

# Output the result
print("Modified string:", modified_string)