def vowelCount(s):
    count=0
    
    for i in range(len(s)):
        if("a"==s[i] or "e"==s[i] or "i"==s[i] or "o"==s[i] or "u"==s[i]):
            count=count+1
    return count

print(vowelCount("aercious"))