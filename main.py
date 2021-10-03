rows = 4
input_str = "DIGITALHIRINGISEASY"
length = len(input_str)
zigzag_str = ""
print(zigzag_str)
interval = 2*rows - 2
count = 0
for i in range(rows):
    step = interval - (2 * i)
    for j in range(i,length,interval):
        zigzag_str += input_str[j]
        if 0 < step < interval and j+step < length:
            zigzag_str += input_str[j+step]

print(zigzag_str)
