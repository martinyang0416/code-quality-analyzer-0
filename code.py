HPY, ATKY, DEFY = map(int, input().split())
HPM, ATKM, DEFM = map(int, input().split())
h_price, a_price, d_price = map(int, input().split())

min_cost = float('inf')

a_min = max(0, DEFM - ATKY + 1)
for a_add in range(a_min, a_min + 201):
    atky_new = ATKY + a_add
    dy = atky_new - DEFM
    if dy <= 0:
        continue
    t = (HPM + dy - 1) // dy
    d_max = max(0, ATKM - DEFY) + 200
    for d_add in range(0, d_max + 1):
        defy_new = DEFY + d_add
        dm = max(0, ATKM - defy_new)
