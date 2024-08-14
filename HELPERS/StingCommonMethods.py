
### Most Commonly Used String Methods

# 1. **`str.upper()`**  
# Converts all characters in the string to uppercase.
text = "hello"
print(text.upper())  # Output: HELLO

# 2. **`str.lower()`**  
# Converts all characters in the string to lowercase.
text = "HELLO"
print(text.lower())  # Output: hello

# 3. **`str.title()`**  
# Converts the first character of each word to uppercase and the rest to lowercase.
text = "hello world"
print(text.title())  # Output: Hello World

# 4. **`str.capitalize()`**  
#    Converts the first character of the string to uppercase and the rest to lowercase.
text = "hello world"
print(text.capitalize())  # Output: Hello world

# 5. **`str.strip()`**  
# Removes leading and trailing whitespace (or specified characters).
text = "  hello  "
print(text.strip())  # Output: hello

# 6. **`str.lstrip()`**  
# Removes leading whitespace (or specified characters).
text = "  hello"
print(text.lstrip())  # Output: hello

# 7. **`str.rstrip()`**  
# Removes trailing whitespace (or specified characters).
text = "hello  "
print(text.rstrip())  # Output: hello

# 8. **`str.replace(old, new)`**  
# Replaces occurrences of a substring with another substring.
text = "hello world"
print(text.replace("world", "Python"))  # Output: hello Python

# 9. **`str.find(sub)`**  
#    Returns the lowest index of the substring if found; otherwise, returns -1.
text = "hello world"
print(text.find("world"))  # Output: 6
print(text.find("Python"))  # Output: -1

# 10. **`str.rfind(sub)`**  
# Returns the highest index of the substring if found; otherwise, returns -1.
text = "hello world world"
print(text.rfind("world"))  # Output: 12

# 11. **`str.split(separator)`**  
# Splits the string into a list of substrings based on a separator.
text = "hello world"
print(text.split())  # Output: ['hello', 'world']

# 12. **`str.join(iterable)`**  
# Joins elements of an iterable (e.g., list) into a single string, separated by the string.
words = ["hello", "world"]
print(" ".join(words))  # Output: hello world

# 13. **`str.startswith(prefix)`**  
# Checks if the string starts with the specified prefix.
text = "hello world"
print(text.startswith("hello"))  # Output: True

# 14. **`str.endswith(suffix)`**  
# Checks if the string ends with the specified suffix.
text = "hello world"
print(text.endswith("world"))  # Output: True

# 15. **`str.zfill(width)`**  
# Pads the string on the left with zeros to make the string of the specified width.
text = "42"
print(text.zfill(5))  # Output: 00042

# 16. **`str.isdigit()`**  
# Returns `True` if all characters in the string are digits.
text = "1234"
print(text.isdigit())  # Output: True

# 17. **`str.isalpha()`**  
# Returns `True` if all characters in the string are alphabetic.
text = "hello"
print(text.isalpha())  # Output: True

# 18. **`str.isspace()`**  
# Returns `True` if all characters in the string are whitespace.
text = "   "
print(text.isspace())  # Output: True

# 19. **`str.islower()`**  
# Returns `True` if all characters in the string are lowercase.
text = "hello"
print(text.islower())  # Output: True

# 20. **`str.isupper()`**  
# Returns `True` if all characters in the string are uppercase.
text = "HELLO"
print(text.isupper())  # Output: True

# These methods are essential for manipulating and analyzing strings in Python and are widely used in various programming tasks.