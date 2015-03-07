import string
alphabet = string.ascii_lowercase

with open('02_data.txt') as f:
        kruft = ''.join(f.readlines())
        print ''.join([ c for c in kruft if c.isalpha() ])
