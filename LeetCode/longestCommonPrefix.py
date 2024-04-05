from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    # res = ""
    # min_len = min([len(el) for el in strs])
    # for i in range(min_len):
    #     sym = strs[0][i]
    #     if all(sym in el[i] for el in strs):
    #         res += sym
    #     else:
    #         break
    # return res

    ans = ""
    sort_strs = sorted(strs)
    first, last = sort_strs[0], sort_strs[-1]
    for i in range(len(first)):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


# strs = ["flower", "flow", "flight"]  # "fl"
# strs = ["dog", "racecar", "car"]  # ""
strs = ["cir","car"]  # "c"

print(longestCommonPrefix(strs))
