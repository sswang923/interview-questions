
from collections import defaultdict
def removeDuplicates(list):
	x = defaultdict(int)
	for l in list:
		x[l] += 1
	return [key for key in x if x[key]==1]

print removeDuplicates([1,2,3,2,1,2,3,2,5])