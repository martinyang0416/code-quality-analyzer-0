n = int(input())

numbers = list(map(int, input().split()))

evens = list()
odds = list()


def fill_evens():
    for k in numbers:
        if k % 2 == 0:
            evens.append(k)
        else:
            odds.append(k)
fill_evens()
distinct = evens[0] if len(evens) == 1 else odds[0]
print(numbers.index(distinct) + 1)
