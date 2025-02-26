import re
def ali(string):
    pattern = r'^ab{2,3}$'
    return bool(re.fullmatch(pattern,string))
print(ali("abba"))
      