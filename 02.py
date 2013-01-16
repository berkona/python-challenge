
occurences = {}


def countChars(line):
	for char in line:
		occurences[char] = occurences.get(char, 0) + 1

# Don't let the procedure call fool you, this is n^2 complexity, but meh it's challenge 2
with open('02_data.txt') as kruft:
	for line in kruft:
		countChars(line)

# 10 or less is rare, right?
print(''.join(i for i in occurences if occurences[i] < 10))
