import re
import sys
import urllib.request

BASE = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d'

# Alternatively, we could use '[0-9]+$', but that only takes into account things that are at the end, which isn't technically what they told us to look for
FIND_NEXT = re.compile('(?<=and\sthe\snext\snothing\sis\s)([0-9]+)')


def follow(url, this):
	print('following to:', url % this)
	contents = ""
	# Remember kids, always close your file-like objects
	with urllib.request.urlopen(url % this) as response:
		contents = str(response.read())

	try:
		next = int(FIND_NEXT.findall(contents)[0])
		return follow(url, next)
	except:
		# This is the base case BTW
		# Also, don't do this in production code kids
		# We're professionals and we know what we're doing (kinda)
		return this

last = follow(BASE, int(sys.argv[1]))
print('last link:', BASE % last)
