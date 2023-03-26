a = int(input())
s1 = set(map(int, input().split()))

n = int(input())

for i in range(n):
    s = input().split()
    one = s[0]
    two = int(s[1])
    
    s2 = set(map(int, input().split()))
    
    if one == 'update':
        s1.update(s2)
    elif one == 'intersection_update':
        s1.intersection_update(s2)
    elif one == 'difference_update':
        s1.difference_update(s2)
    elif one == 'symmetric_difference_update':
        s1.symmetric_difference_update(s2)
    else:
        print("Wrong input")

sum = 0
for i in s1:
    sum = sum + i

print(sum)
