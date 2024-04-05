def check_p_in_s(s, p):
    while p:
        if p[1] == '*':
            p = p[2:]


def isMatch(s: str, p: str) -> bool:
    if p == s or p == ".*" or (len(s) == len(p) and all(el == '.' for el in p)):
        return True
    elif "." not in p and "*" not in p:
        return False
    else:
        while p or s:
            if len(p) > 1 and len(s) > 0 and p[0] in [s[0], '.'] and p[1] != "*":
                s, p = s[1:], p[1:]

            elif len(p) > 2 and p[:2] == '.*':
                p = p[2:]
                while p:
                    p

                temp = p[2:]
                new_p = ''
                for i in range(len(temp)-1):
                    if temp[i+1] != '*' or temp[i] != '.' or temp != '*':
                        new_p += temp[i]

                return check_p_in_s(s, p[2:])

            elif len(p) > 1 and p[-2:] == '.*':
                return isMatch(s, p[:-2])

            elif len(p) > 1 and p[-1] == '*':
                while s and p[-2] in [s[-1], '.']:
                    s = s[:-1]
                p = p[:-2]

            elif p and s and p[-1] in [s[-1], '.']:
                s, p = s[:-1], p[:-1]

            else:
                return False
            print(s, p)

        return True


# s, p = "aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*"  # true test

s, p = "aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"  # true
# s, p = "aaa", "a.a"  # true
# s, p = "bbbba", ".*a*a"  # true
# s, p = "aaa", "ab*a*c*a"  # true
# s, p = "abcd", "d*"  # false
# s, p = "aaa", "a*a"  # true
# s, p = "aa", "a"  # false
# s, p = "aa", "a*"  # true
# s, p = "aaaab", "a*b"  # true
# s, p = "aaa", "a*b"  # false
# s, p = "ab", ".*"  # true
# s, p = "aab", "c*a*b"  # true
# s, p = "mississippi", "mis*is*ip*."  # true
# s, p = "mississippi", "mis*is*p*."  # false
text = 'a'
print(text[1:])
print(bool(text))
# print(isMatch(s, p))
