testcase = open('22/22.txt', 'r').read().split('\n')

def mix(number: int, secret: int) -> int:
    return secret ^ number

def prune(secret: int) -> int:
    return secret % 16777216

def parts() -> int:
    ans = 0
    prices = {}
    for line in testcase:
        secret = int(line)
        two_hundredth = None
        last_digit = line[-1]
        sequences = [int(last_digit)]
        first_sequences = set()
        for _ in range(2000):
            result = secret * 64
            secret = mix(result, secret)
            secret = prune(secret)
            result = secret // 32
            secret = mix(result, secret)
            secret = prune(secret)
            result = secret * 2048
            secret = mix(result, secret)
            secret = prune(secret)
            two_hundredth = secret
            next_last_digit = str(two_hundredth)[-1]
            sequences.append(int(next_last_digit))
            if len(sequences) > 4:
                a, b, c, d, price = sequences[-5], sequences[-4], sequences[-3], sequences[-2], sequences[-1]
                sequence = (b - a, c - b, d - c, price - d)
                if sequence in first_sequences:
                    continue
                first_sequences.add(sequence)
                prices[sequence] = prices.get(sequence, 0) + price
        ans += two_hundredth
    ans2 = 0
    for key in prices:
        ans2 = max(ans2, prices[key])
    return ans, ans2

print(parts()) # (14622549304, 1735)