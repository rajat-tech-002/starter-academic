# calculate the 698th number of fibonacci sequence

# [0, 1] - 0, 1, 1, 2, 3, 5....
# 

def get_fibonacci_n(index):
    temp = 2
    a = 0, b = 1
    while temp!=index:
         next_num = a+b
         a = b # old b
         b = next_num # new b
         temp+=1


