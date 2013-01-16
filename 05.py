import pickle
from urllib.request import urlopen

# We could prolly use sys.argv, but meh
URL = 'http://www.pythonchallenge.com/pc/def/banner.p'

# Remember kids, always close your file-like objects
with urlopen(URL) as response:
	obj = pickle.load(response)

# I had to look what wtf kinda object this was... Python you assume too much
for line in obj:
	# Use Python's native understanding of tuples for this comprehension
	print(''.join( ch * count for ch, count in line))
