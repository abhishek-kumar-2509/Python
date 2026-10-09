string = input("Enter String: ")
count = 0

for ch in string.lower():
    if ch in 'aeiou':
        count+=1

print("Vowel = ", count)
