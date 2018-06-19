from itertools import chain, combinations
# Define alphabet mapping.
alphabet = {}
for i in range(1, 27):
    alphabet[str(i)] = chr(i + 96)

# Message to decode.
msg = '262'

# Create pool of allowable combinations.
pool = []
for i in range(len(msg)):
    for j in range(1, len(msg) + 1):
        if msg[i:j] in alphabet.keys():
            pool.append(msg[i:j])

# Create set of combinations of all pool values.
msgs = set(chain.from_iterable(combinations(pool, r) for r in range(len(pool) + 1)))

# Count how many ways we can combine the pool values to get the original message.
count = 0
print("Possible interpretations: ")
for m in msgs:
    temp = ''
    for m_i in m:
        temp += m_i
    if temp == msg:
        print(m)
        count += 1

print("Possible ways to interpret the message: %d" %count)