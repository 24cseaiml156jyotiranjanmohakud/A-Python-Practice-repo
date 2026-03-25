#1 Find the largest element in a list.
nums = [10, 25, 5, 40, 15]
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print("Largest:", largest)

#2 Check if a number is even or odd.
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3 Reverse a string (without slicing).
s = "hello"
rev = ""

for ch in s:
    rev = ch + rev

print("Reversed:", rev)

#4 Count vowels in a string.
s = "education"
count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Vowels:", count)

#5 Find the sum of digits of a number.
num = 1234
total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Sum:", total)

#6 Check if a string is a palindrome.
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#7 Print Fibonacci series up to N terms.
n = 6
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#8 Swap two variables without a third variable. 
a = 5
b = 10

a, b = b, a
print(a, b)

#9 Count words in a sentence.
s = "I love Python programming"
words = s.split()

print("Word count:", len(words))

#10 Find minimum and maximum in a list.
nums = [4, 2, 9, 1]

print("Min:", min(nums))
print("Max:", max(nums))

#11 Find the second largest number in a list. 
nums = [10, 20, 4, 45, 99]
nums.sort()

print("Second Largest:", nums[-2])

#12 Remove duplicates from a list (without set). 
nums = [1, 2, 2, 3, 4, 4]
unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print(unique)

#13 Count frequency of elements in a list. 
nums = [1, 2, 2, 3, 1]

freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)

#14 Merge two sorted lists.
a = [1, 3, 5]
b = [2, 4, 6]

merged = sorted(a + b)
print(merged)

#15 Find the intersection of two lists.
a = [1, 2, 3]
b = [2, 3, 4]

print(list(set(a) & set(b)))

#16 Rotate a list by k positions.
nums = [1, 2, 3, 4, 5]
k = 2

k = k % len(nums)
rotated = nums[-k:] + nums[:-k]

print(rotated)

#17 Check if two strings are anagrams.
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

#18 Find the first non-repeating character. 
s = "aabbcde"

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating:", ch)
        break

#19 Flatten a nested list.
nested = [[1, 2], [3, 4], [5]]
flat = []

for sub in nested:
    for item in sub:
        flat.append(item)

print(flat)

#20 Find all pairs with a given sum.
nums = [1, 2, 3, 4, 5]
target = 5

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])

#21 Print a right triangle pattern.
n = 5
for i in range(1, n+1):
    print("*" * i)

#22 Print a pyramid pattern.
n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))

#23 Print all prime numbers in a range.
start, end = 10, 30

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#24 Check if a number is Armstrong.
num = 153
temp = num
power = len(str(num))
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** power
    temp //= 10

if sum_val == num:
    print("Armstrong")
else:
    print("Not Armstrong")