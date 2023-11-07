num = [10, 5, 89, 562, 22, 13, 17, 7, 155, 63, 89]

for x in num:
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                print(f"{x} is not a prime number")
                break
        else:
            print(f"{x} is a prime number")
