def isValid(s: str) -> bool:
    # fm = {"(", "[", "{"}
    # lm = {")", "]", "}"}
    fm = {"(": ")", "[": "]", "{": "}"}
    bk = []

    for sym in s:
        if sym in fm:
            bk.append(fm[sym])
            # if sym == "(":
            #     bk.append(")")
            # elif sym == "[":
            #     bk.append("]")
            # else:
            #     bk.append("}")

        elif sym in fm.values():
            if bk == [] or sym != bk[-1]:
                return False
            bk.pop()
            # else:
            #     bk = bk[:-1]
    return bk == []


# s = "()"  # true
# s = "()[]{}"  # true
# s = "(]"  # false
# s = "([{}])"  # true
# s = "["  # false
print(isValid(s))
