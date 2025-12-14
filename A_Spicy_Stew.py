# A Spicy Stew

n = int(input())  # number of test cases

for i in range(n):
    c = int(input())  # number of chillies
    chillies_list = list(map(int, input().split()))

    if len(chillies_list) != len(set(chillies_list)):
        print("YES")
    else:
        print("NO")
