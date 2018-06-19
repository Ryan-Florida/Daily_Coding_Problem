from sys import maxsize
array = [-1, -2, -3]

low = maxsize
for a in array:
    if 0 < a < low:
        low = a

if low == maxsize:
    print(1)

else:
    if low != 1:
        temp = low - 1
        while temp in array and temp > 0:
            temp -= 1

    else:
        temp = low + 1
        while temp in array:
            temp += 1

    print(temp)
