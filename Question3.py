def printknapSack(capacity, weight, val, n):
    K = [[0 for w in range(capacity + 1)]
         for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    result = K[n][capacity]
    print("The maximum value obtained for the knapsack algorithm is ", result)
    print("The combined weights: ")

    w = capacity
    for i in range(n, 0, -1):
        if result <= 0:
            break
        if result == K[i - 1][w]:
            continue
        else:

            print("%10s       %10s" % ("Weights", "Values"))
            print("%10d       %10d" % (weight[i - 1], val[i-1]))

            result = result - val[i - 1]
            w = w - weight[i - 1]


money = [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500]
weights = [5, 3, 1, 6, 8, 4, 11, 12]
W = 20
item = len(money)

printknapSack(W, weights, money, item)
