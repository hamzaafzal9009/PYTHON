#   \n  => newLine
#   \t => tab
#   \; => single quote
#   \\ => Back slash


# In Python, escape sequences are used to represent special characters within strings that would otherwise be difficult or impossible to include directly. They are preceded by a backslash (`\`). Here are some common escape sequences in Python:

### Common Escape Sequences

# - **Newline:** `\n`  
#   Moves the cursor to the next line.  
print("Hello\nWorld")
# Output:
# Hello
# World

# - **Carriage Return:** `\r`  
#   Moves the cursor to the beginning of the line without advancing to the next line.  
print("Hello\rWorld")
# Output: World

# - **Tab:** `\t`  
#   Inserts a tab space.  
print("Hello\tWorld")
# Output: Hello   World

# - **Backslash:** `\\`  
#   Inserts a backslash character. 
print("Path: C:\\Program Files\\App")
# Output: Path: C:\Program Files\App

# - **Single Quote:** `\'`  
#   Inserts a single quote character in a single-quoted string.  
print('It\'s a test.')
# Output: It's a test.


# - **Double Quote:** `\"`  
#   Inserts a double quote character in a double-quoted string.  
print("He said, \"Hello!\"")
# Output: He said, "Hello!"


# - **Unicode Character:** `\uXXXX`  
# Inserts a Unicode character where `XXXX` is the four-digit hexadecimal code.  
print("\u00A9 2024")
# Output: © 2024

# - **Octal Value:** `\ooo`  
#   Represents a character based on its octal value (where `ooo` is up to three octal digits).  
print("\101")  # Octal for 'A'
# Output: A

# - **Hexadecimal Value:** `\xhh`  
#   Represents a character based on its hexadecimal value (where `hh` is a two-digit hexadecimal number).  
print("\x41")  # Hexadecimal for 'A'
# Output: A

# - **Raw Strings:** Prefixing a string with `r` or `R` tells Python to interpret backslashes as literal characters.  
print(r"C:\Program Files\App")
# Output: C:\Program Files\App

# Escape sequences are useful for formatting strings and including characters that would otherwise be difficult to enter directly.