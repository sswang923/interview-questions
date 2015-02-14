def tokenize(p):
    tokens = []
    index = 0
    while index < len(p):
        if index + 1 < len(p):
            if p[index + 1] == "*":
                tokens.append(p[index] + p[index+1])
                index += 2
            else:
                tokens.append(p[index])
                index +=1
        else:
            tokens.append(p[index])
            index +=1   
    return tokens

def matchEmpty(tokens):
    for token in tokens:
        if token[-1] != '*':
            return False
    return True

# aa , a*b   -> a, a*b or a, b -> 
# ab, .*c -> b .*c or b, c ->  '', .*c -> '', c  ( false)
# aaa, ab*a -> aa b*a, 
# a, "ab*" -> '', b* -> '', ''
def findMatch(s, tokens):
    print vars(),
    if not tokens:
        print "Returned True"
        return not s
    if (len(s) > 0 and s[0] != tokens[0][0] or not s) and tokens[0][0] != '.' and tokens[0][-1] != "*":
        print "Returned False"
        return False
    else:
        if tokens[0][-1] == '*':
            if (len(s) > 0 and tokens[0][0] == s[0]) or tokens[0][0] == ".":
                return findMatch(s[1:], tokens[1:]) or findMatch(s[1:], tokens) or findMatch(s, tokens[1:])
            else:
                return findMatch(s, tokens[1:])
        else:
            return findMatch(s[1:], tokens[1:])

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        tokens = tokenize(p)
        return findMatch(s, tokens)
x = Solution().isMatch( "ab", ".*c")
print x
