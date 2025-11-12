# 0/1 Knapsack Problem using Dynamic Programming

def knapsack_dp(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example run
print("=== 0/1 Knapsack using Dynamic Programming ===")
n = int(input("Enter number of items: "))
values = list(map(int, input("Enter values: ").split()))
weights = list(map(int, input("Enter weights: ").split()))
capacity = int(input("Enter knapsack capacity: "))

max_val_dp = knapsack_dp(values, weights, capacity)
print("Maximum value (DP):", max_val_dp)

"""
INPUT

=== 0/1 Knapsack using Dynamic Programming ===
Enter number of items: 4
Enter values: 60 100 120 80
Enter weights: 10 20 30 40
Enter knapsack capacity: 50

OUTPUT

Maximum value (DP): 220
"""