# Print out all of the numbers in the following array that are divisible by 3:
# [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42

a = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

l = [x for x in a if x % 3 == 0]

for i in l:
    print(i)