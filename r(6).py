import re

def replace_special_chars(s):
    return re.sub(r'[ ,.]', ':', s)
print(replace_special_chars("Hello, world. How are you?"))