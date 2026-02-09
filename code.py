n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

even_a = sum(1 for num in a if num % 2 == 0)
odd_a = len(a) - even_a

even_b = sum(1 for num in b if num % 2 == 0)
odd_b = len(b) - even_b

result = min(even_a, odd_b) + min(odd_a, even_b)
print(result)