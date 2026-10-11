# 130. Check Whether Two Strings Are Anagrams

text1 = "listen"
text2 = "silent"

if sorted(text1.lower()) == sorted(text2.lower()):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")