
allowance = 2000
allowance -= 400
print(f"remaining allowance:{allowance}")
allowance = allowance + 100
print(allowance)
allowance -=250
print(f"allowance: {allowance}")
print("discount: 25%")
percent = 25 / 100
percent *= allowance
allowance -= percent
print(f"allowance: {allowance}")
allowance -= (1/3) * (allowance)
allowance //= 2
print(f"allowance: {allowance}")
allowance %= 100
print(f"balance: {allowance}")
