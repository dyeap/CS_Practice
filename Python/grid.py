# this is correct way of generating empty buckets
bucket = [[] for _ in range(3)]
bucket[0].append(0)
print(bucket)

# this is incorrect way of generating 2D grid
bucket = [[]] * 3
bucket[0].append(0)
print(bucket)


#[0 for _ in range(3)]

# one way or making 3x3 grid
print([[0 for col in range(4)] for row in range(3)])

# another way of making a grid
dp = [[] for _ in range(3)]
for row in range(3):
    dp[row] = [0 for _ in range(3)]

print(dp)

bucket = ["" for _ in range(3)]
print(int("007"))

from random import shuffle

# how to check if li is []
p = []
if p ==[]: print("yes")

num = [1,2,3,4,5]

print(shuffle(num))
print(num)

d = {1:1}
print(d.get(None))