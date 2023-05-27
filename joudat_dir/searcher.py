import re

str = "there is a needle in the haystack"

x = re.findall(r'needle', str, re.IGNORECASE)[0]

print("FOUND:", x)