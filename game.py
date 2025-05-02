import time

t0 = time.time()

text = "Hallo wie geht es dir"
print(text)

# input("")

totalCorrectLetters = 0
for word in text.split():
    print(word)
    a = input("")
    for i in range(len(word)):
        if word[i] == a[i]:
            totalCorrectLetters += 1

print(totalCorrectLetters)

# t1 = time.time()

# total = t1-t0

# print("Du hast " + str((len(text)/total)/5*60) + "Wörter pro Minute")
