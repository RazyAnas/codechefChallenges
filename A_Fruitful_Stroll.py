# A Fruitful Stroll

n = int(input()) # number of test cases

for i in range(n):
    total_trees = int(input()) # how many trees are there in the farm
    lst = list(map(int, input().split())) # create an 

    count = {}
    left = 0
    ans = 0
    # sliding window technique
    for right in range(total_trees):
        t_type = lst[right]
        count[t_type] = count.get(t_type, 0) + 1 # get the prev no. of fruits from that tree type or else get 0 and add 1
        while len(count) > 2: # keep shrinking the window until the count is legal again
            left_val = lst[left]
            count[left_val] -= 1 # remove from left
            if count[left_val] == 0: # when left count is 0 delete it
                del count[left_val]
            left += 1 # move from the left
        ans = max(ans, right - left + 1) # count the max 

    print(ans)
