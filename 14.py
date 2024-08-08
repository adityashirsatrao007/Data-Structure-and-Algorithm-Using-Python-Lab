# Coin Change Problem using Greedy Approach
def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

coins = [1, 5, 10, 25]
amount = 63
print("Coins for Amount (Greedy):", coin_change(coins, amount))
