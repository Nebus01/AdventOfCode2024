from collections import defaultdict

file_path = "Your file path"

with open(file_path, "r") as file:
    initial_secrets = [int(line.strip()) for line in file]

def next_secret(secret):
    secret ^= (secret * 64)
    secret %= 16777216

    secret ^= (secret // 32)
    secret %= 16777216

    secret ^= (secret * 2048)
    secret %= 16777216

    return secret

def simulate_2000th_secret(initial_secret):
    secret = initial_secret
    for _ in range(2000):
        secret = next_secret(secret)
    return secret

def find_best_sequence(initial_secrets):
    part2_totals = defaultdict(int)

    for secret in initial_secrets:
        prices = []
        current_secret = secret

        for _ in range(2001):
            prices.append(current_secret % 10)
            current_secret = next_secret(current_secret)

        price_changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

        seen_seqs = set()
        for i in range(len(price_changes) - 3):
            seq = tuple(price_changes[i:i + 4])
            if seq not in seen_seqs:
                seen_seqs.add(seq)
                part2_totals[seq] += prices[i + 4]

    best_sequence = max(part2_totals, key=part2_totals.get)
    max_bananas = part2_totals[best_sequence]

    return max_bananas, best_sequence

#PART1:
total_sum = sum(simulate_2000th_secret(secret) for secret in initial_secrets)
print("Part 1: ", total_sum)

#PART2:
max_bananas = find_best_sequence(initial_secrets)
print("Part 2: ", max_bananas)