import re
with open('/mnt/c/Users/user/Downloads/LordoftheRings1-FOTR.txt', 'r', encoding = 'utf-8') as text:
    script = text.read()
    script_parts = re.split(r'CUT TO:', script)
    for part in script_parts:
        l=set(re.findall(r'\s{22}([A-Z]+)\n\s{10}', part))
