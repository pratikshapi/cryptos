p = 6

def ring_to_array_mapping(i):
    return (i % p) + ((i + 1) % (p - 1) if i < p - 1 else 0)

for i in range(p):
    # print(i)
    print(ring_to_array_mapping(i))