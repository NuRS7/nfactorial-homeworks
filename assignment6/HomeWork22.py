def check_anagrams(a, b, c):
    a = a.lower()
    b = b.lower()
    c = c.lower()
    if sorted(a) == sorted(b) and  sorted(c):
        return "Yes"
    else:
        return "No"

# Пример использования

a = "aBa"
b = "aab"
c = "baa"

result = check_anagrams(a, b, c)
print(result)
