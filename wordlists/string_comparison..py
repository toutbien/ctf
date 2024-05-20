# Take a function using string_letter_check that takes two strings, str1 and str2, as arguments.
#str1 and str2 can be used as locations for files with strings
#case insensitive
def string_letter_check(str1, str2):
    # Check if all characters in 2 are present in 1 (lowercasing standardization): 
    # Can use upper() if needed
    return all([char in str1.lower() for char in str2.lower()])

# Test the function with different pairs of strings and print the results.
print(string_letter_check("python", "ypth"))    # Expecting True (all characters in str2 are in str1)
print(string_letter_check("python", "ypths"))   # Expecting False (not all characters in str2 are in str1)
print(string_letter_check("python", "ypthon"))  # Expecting True (all characters in str2 are in str1)
print(string_letter_check("123456", "01234"))   # Expecting False (not all characters in str2 are in str1)
print(string_letter_check("123456", "1234"))    # Expecting True (all characters in str2 are in str1)
