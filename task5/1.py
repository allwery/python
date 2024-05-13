#1
def max_r(N, K, heights):
    pref_sums = [0] * N
    pref_sums[0] = heights[0]
    for i in range(1, N):
        pref_sums[i] = pref_sums[i - 1] + heights[i]

    max_score = -float('inf')
    

    for start in range(N - K + 1):
        end = start + K - 1
        score = pref_sums[end]
        if start > 0:
            score -= pref_sums[start - 1]
        if score > max_score:
            max_score = score
            best_start = start + 1
            best_end = end + 1
    return max_score

with open('C:/Users/s0172066/Downloads/27-170a.txt', 'r') as f:
    N, K = map(int, f.readline().split())
    heights = [int(line) for line in f]

max_a = max_r(N, K, heights)

with open('C:/Users/s0172066/Downloads/27-170b.txt', 'r') as f:
    N, K = map(int, f.readline().split())
    heights = [int(line) for line in f]

max_b = max_r(N, K, heights)
print(max_a, max_b)

#2
import random

with open("f.txt", "w") as f:
    for i in range(100):
        f.write(str(random.randint(1, 100)) + "\n")

with open("f.txt", "r") as f, open("g.txt", "w") as g:
    numbers = set()
    for line in f:
        number = int(line.strip())
        if number not in numbers:
            g.write(str(number) + "\n")
            numbers.add(number)
            
with open("g.txt", "r") as g:
    print(g.read())
