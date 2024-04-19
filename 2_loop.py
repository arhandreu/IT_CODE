# 1___________________________
n = int(input())
sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum += i

print(sum)

sum = 0
i = 0
while i <= n:
    if i % 2 == 0:
        sum += i
    i+=1

print(sum)


# 2_________________________________
words = ["123456", "1235", "1234"]
longest_word = []
long_word = 0

for word in words:
    if len(word) > long_word:
        long_word = len(word)
        longest_word.clear()
        longest_word.append(word)
    elif len(word) == long_word:
        longest_word.append(word)

print(longest_word)

i = 0
longest_word = []
while i <= len(words) - 1:
    word = words[i]
    if len(words) > long_word:
        long_word = len(words)
        longest_word.clear()
        longest_word.append(word)
    elif len(word) == long_word:
        longest_word.append(word)
    i+=1

print(longest_word)

# 3_________________________________________________________
n = int(input())

fact = 1

for i in range(2, n+1):
    fact *= i
    print(fact)

fact = 1
while n > 1:
    fact *= n
    print(fact)
    n -= 1


# 4__________________________________________
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, value in enumerate(numbers):
    if (index + 1) % 3 == 0:
        print(index, value)

# 5______________________________________________
n = int(input())
for i in range(1, 11):
    print(f"{n}*{i}={i*n}")

# 6_______________________________________________
number = int(input())

n = number
count = 0
while n > 0:
    count += 1
    n//=10

print(count)

count = 0
for i in str(number):
    count += 1
    
print(count)

# 7____________________________________________________________
string_palindrom = input().replace(" ", "")
len_pal = len(string_palindrom)//2 + 1
palindrom = True

for i in range(0, len_pal):
    if string_palindrom[i] != string_palindrom[-i-1]:
        palindrom = False
        break

print(palindrom)

# 8________________________________________________________
words = ["asd", "asf", "ast"]
unique_words = []
duplicate = "Дубликатов нет"

for word in words:
    if word in unique_words:
       duplicate = "Есть дубликаты"
       break
    else:
        unique_words.append(word)

print(duplicate)

# 9______________________________________________________
words = ["asd", "asd", "ast", "ast"]
for word_ in words:
    word_n = 0
    for index, word in enumerate(words):
        if word_ == word:
            word_n += 1
            if word_n > 1:
                words.pop(index)

print(words)

count_words = len(words)

j = 0
while j < count_words:
    k = 0
    while k < count_words:
        if words[j] == words[k] and k != j:
            words.pop(k)
            count_words -= 1
        k +=1
    j +=1

print(words)

# 10________________________________________________
string = "afhbsauhfuy"
len_string = len(string) - 1

while len_string >= 0:
    print(string[len_string])
    len_string -=1

# 11_______________________________________________________
print("Пн Вт Ср Чт Пт Сб Вс")
for day in range(1, 32):
    if day % 7 == 0:
        print(str(day).rjust(2))
    else:
        print(str(day).rjust(2), end=" ")
