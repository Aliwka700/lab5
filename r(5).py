import re
def match_a_any_b(s):
    return re.fullmatch(r'a.*b', s) is not None
print(match_a_any_b("axb"))  # True
print(match_a_any_b("abc"))  # False