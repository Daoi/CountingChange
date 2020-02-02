def count_change(money, coins):
    m = len(coins)

    return count(money, coins, m)


def count(money, coins, m):
    table = [0 for k in range(money + 1)]

    table[0] = 1

    for i in range(0, m):
        for j in range(coins[i], money + 1):
            table[j] += table[j - coins[i]]

    return table[money]



