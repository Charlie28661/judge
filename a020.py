loc = {
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
    "G" : 16,
    "H" : 17,
    "I" : 34,
    "J" : 18,
    "K" : 19,
    "L" : 20,
    "M" : 21,
    "N" : 22,
    "O" : 35,
    "P" : 23,
    "Q" : 24,
    "R" : 25,
    "S" : 26,
    "T" : 27,
    "U" : 28,
    "V" : 29,
    "W" : 32,
    "X" : 30,
    "Y" : 31,
    "Z" : 33
}

a = list(input())
convert = loc.get(a[0])

num1 = convert // 10 #十位數
num2 = convert % 10 #個位數

r = num2 * 9 + num1

j = 0
for i in range(1, 9):
    j = j + int(a[9-i]) * (i)

f = r + j + int(a[9])

if (f % 10 == 0):
    print("real")
else:
    print("fake")