
def parseRegex(regex):
	output = []
	previous = None
	for n in regex:
		if n ==  '*' or n == '+':
			output.append(previous+n)
			previous = None
		else:
			if previous != None:
				output.append(previous)
			previous = n
	if previous != None:
		output.append(previous)
	return output

def constructFSM(regex):
	print regex
	current_state = root_state = {}
	for n in regex:
		if n[-1] == '*':
			current_state[n[0]] = current_state
		else:
			if n[-1] == '+':
				new_state = {}
				new_state[n[0]] = new_state
				current_state[n[0]] = new_state
				current_state = new_state
			else:
				new_state = {}
				current_state[n] = new_state
				current_state = new_state
	end_state = current_state
	return root_state

print constructFSM(parseRegex("a*a"))
