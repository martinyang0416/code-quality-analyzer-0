


def isEqual(a, b):
	for i in range(0, len(a)):
		if (a[i] != b[i]):
			return False
	return True


def lexicographic_minimal_string(s):
	if (len(s) % 2 == 1):
		return s
	half = int(len(s) /2)
	s1 = lexicographic_minimal_string(s[:half])
	s2 = lexicographic_minimal_string(s[half:])
	if s1 < s2:
		return s1 + s2
	return s2 + s1

a = input()
b = input()
a = lexicographic_minimal_string(a)
b = lexicographic_minimal_string(b)
if(isEqual(a,b)):
	print("YES")
else:
	print("NO")




















