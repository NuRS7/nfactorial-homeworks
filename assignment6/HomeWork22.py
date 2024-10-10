def check_anagrams(a, b, c):
    if sorted(a) == sorted(c) and sorted(b) == sorted(c):
        return "Yes"
    else:
        return "No"
    a = "aba"
    b = "baa"
    c = "aab"
    result = check_anagrams(a, b, c)
    print(result)