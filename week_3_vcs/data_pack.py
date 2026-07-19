def recharge_cost(gb, validity_days=30):
    if gb == 1:
        return 199
    elif gb == 2:
        return 349
    elif gb == 5:
        return 799
    elif gb == 10:
        return 1499
    else:
        return "Invalid data pack"
print(recharge_cost(1))
print(recharge_cost(2))
print(recharge_cost(5))
print(recharge_cost(10))
print(recharge_cost(2,60))