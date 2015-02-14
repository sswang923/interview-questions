
words = ["SEGMENT","AM","I"]
def is_path(segment):
	print vars()
	if segment == '':
		return True
	for i in words:
		if segment[0:len(i)] == i:
			if is_path(segment[len(i):]):
				return True
	return False

def is_path2(segment):
	print vars()
	if segment == '':
		return True
	for index, value in enumerate(segment):
		if segment[0:index+1] in words:
			if is_path2(segment[index+1:]):
				return True
	return False
print is_path("IAMSEGMENTIT")
print is_path2("IAMSEGMENTIT")