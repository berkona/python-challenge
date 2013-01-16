import re
from urllib.request import urlopen
from zipfile import ZipFile

BASE = '%d.txt'

# Alternatively, we could use '[0-9]+$', but that only takes into account things that are at the end, which isn't technically what they told us to look for
FIND_NEXT = re.compile('(?<=Next\snothing\sis\s)([0-9]+)')

URL = 'http://www.pythonchallenge.com/pc/def/channel.zip'
START = 90052


def follow(zipFile, this, comments=""):
	print('following to:', BASE % this)
	member = BASE % this
	info = zipFile.getinfo(member)
	comments += str(info.comment, encoding='utf-8')

	# Remember kids, always close your file-like objects
	with zipFile.open(info) as internalFile:
		contents = str(internalFile.read())

	try:
		next = int(FIND_NEXT.findall(contents)[0])
		return follow(zipFile, next, comments)
	except:
		# This is the base case BTW
		# Also, don't do this in production code kids
		# We're professionals and we know what we're doing (kinda)
		return this, comments

with urlopen(URL) as remoteFile:
	with open('06_data.zip', mode='wb') as localFile:
		localFile.write(remoteFile.read())

with ZipFile('06_data.zip') as zipFile:
	last, comments = follow(zipFile, START)
	print('last link:', BASE % last)
	with zipFile.open(BASE % last) as f:
		contents = str(f.read())
	print('last link contents:', contents)
	print(comments)
