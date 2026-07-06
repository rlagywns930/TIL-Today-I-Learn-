def remove_vowels(s):
    word = ""
    for i in s:
        if i not in ("a","e","i","o","u"):
            word = word +i
    return word
remove_vowels("codeit")
