import re
def ali(string):
    pattern = r'^a*b*'
    return bool(re.fullmatch(pattern,string))

print(ali("abb"))