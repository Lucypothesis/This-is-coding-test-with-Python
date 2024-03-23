# N = int(input())
# hour = N - (N // 3) + 1
# answer = (N+1) * 60 * 60 - 45 * 45 * hour
# print(answer) 

N = int(input())
count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count += 1
print(count)