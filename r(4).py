import re
def find_capital_followed_by_lower(s):
    return re.findall(r'[A-Z][a-z]+', s)
print(find_capital_followed_by_lower("Hello World Test"))