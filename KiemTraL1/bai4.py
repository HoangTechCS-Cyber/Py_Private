import sys
import math

MOD = 998244353

def compute_answers(max_m):
    # Precompute combinations up to m=1e5
    comb3 = [0] * (max_m + 1)
    for m in range(3, max_m +1):
        comb3[m] = (m * (m-1) * (m-2) // 6) % MOD
    answers = [0] * (max_m +1)
    for m in range(1, max_m +1):
        term1 = m % MOD
        term2 = (m * (m-1)) % MOD if m >=2 else 0
        term3 = comb3[m] if m >=3 else 0
        answers[m] = (term1 + term2 + term3) % MOD
    return answers

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    ms = list(map(int, data[1:t+1]))
    max_m = max(ms)
    answers = compute_answers(max_m)
    for m in ms:
        print(answers[m])

if __name__ == "__main__":
    main()
