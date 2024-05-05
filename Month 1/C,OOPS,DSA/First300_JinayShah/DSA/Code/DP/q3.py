def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

coin_denominations = [1, 2, 5]
target_amount = 11

result = min_coins(coin_denominations, target_amount)
print(f"Minimum number of coins required to make {target_amount}: {result}")