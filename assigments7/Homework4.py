def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello"))
print(count_vowels("World"))

