""" count = 0
int_count = 0
while  count < 10:
    while int_count < 10:
        print(count, int_count)
        int_count += 1

    count += 1
    int_count = 0 """

x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')