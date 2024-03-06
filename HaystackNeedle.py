def haystackNeedle(haystack,needle):
    if needle == "":
        return 0
    for i in range(len(needle)+1-len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
