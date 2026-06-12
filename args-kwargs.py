def soma(*args):
    total = 0
    for num in args:
        print(f'Total: {total}', num)
        total += num
        print(total)

soma(1,2,3,4,5,6,7,8,9,)