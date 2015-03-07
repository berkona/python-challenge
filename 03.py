import re

regex = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
# Remember kids, always close your file-like objects
with open('03_data.txt') as kruft:
	contents = kruft.read().replace('\n', '')
print ''.join(regex.findall(contents))
