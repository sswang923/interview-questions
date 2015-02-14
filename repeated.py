class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        # for every 10 letters from 0 to size-10, try to match it against the entire string
        answer = {}
        match_strings = {}
        for index in xrange(0, len(s) - 9):
            match_string = s[index:index+10]
            if match_string in match_strings and match_string not in answer:
                answer[match_string] = True
            else:
                match_strings[match_string] = True
        return answer.keys()

s = "AAAAAAAAAAAAAAA"


x = Solution().findRepeatedDnaSequences(s)

print x