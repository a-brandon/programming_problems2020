def happy_algorithm(num):
    if num == 1:
        return 'HAAPY 1'

    happy_nums = set()
    happy_nums.add(num)
    count = 0
    while num > 1:
        digits = list(map(int, str(num)))
        total = sum(x ** 2 for x in digits)
        num = total
        if num in happy_nums:
            return 'SAD ' + str(count + 1)
        happy_nums.add(num)
        count += 1
    return 'HAPPY ' + str(count)
