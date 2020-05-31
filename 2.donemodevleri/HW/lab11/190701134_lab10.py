import re
text= "+1945.4 1453 %20 2.3$ -2.3 -245 "

match = re.findall("(pass)",text)
print(match)