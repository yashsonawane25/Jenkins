from itertools import permutations

# Generate all permutations of digits 1-9
all_permutations = [''.join(p) for p in permutations('123456789')]

# Save to a file
with open('all_combinations_1_to_9.txt', 'w') as file:
    for perm in all_permutations:
        file.write(perm + '\n')

print(f"{len(all_permutations)} combinations written to all_combinations_1_to_9.txt")
