import re

cc1 = [
    "4123456789123456",
    "5123-4567-8912-3456",
    "61234-567-8912-3456",
    "4123356789123456",
    "5133-3367-8912-3456",
    "5123 - 3567 - 8912 - 3456"
]

cc = [
    "7165863385679329",
    "6175824393389297",
    "5252248277877418",
    "9563584181869815",
    "5179123424576876"
]

def check_cc(c):
    if (bool(re.match(r"^[456]", c)) == False):
        return "Invalid"
    if ( bool(re.match(r"^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$", c)) == False and bool(re.match(r"^[0-9]{16}$",c) ) == False):
        return "Invalid"

    remove_dash = re.sub(r'\D', '', c)
    #print(remove_dash)
    if (bool(re.findall(r"(\d)\1{3}", remove_dash)) >= 1):
        return "Invalid"
    return "Valid"

for c in cc:
    #print(c)
    print(check_cc(c))