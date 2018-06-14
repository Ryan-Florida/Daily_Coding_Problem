from itertools import chain
input_array  = [1, 2, 3, 4, 5]
output_array = []

max_index    = len(input_array)

for i in range(max_index):
    output_array.append(1)
    r = chain(range(i), range(i + 1, max_index))
    for j in r:
        output_array[i] *= input_array[j]

print(output_array)