n = int(input())
set1 = set(map(int, input().split()))

m = int(input())
set2 = set(map(int, input().split()))

set3 = set1 ^ set2
count = 0

for i in set3:
    count += 1
    
print(count)
