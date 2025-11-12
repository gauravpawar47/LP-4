# 0/1 Knapsack Problem using Branch and Bound

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # value-to-weight ratio


class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level      # index of current item
        self.profit = profit    # total value so far
        self.weight = weight    # total weight so far
        self.bound = bound      # upper bound on max profit from this node


def bound(node, n, capacity, items):
    """Calculate upper bound (maximum possible profit) for the given node"""
    if node.weight >= capacity:
        return 0

    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight

    # include items while within capacity
    while j < n and total_weight + items[j].weight <= capacity:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # include fraction of next item (for bound estimation only)
    if j < n:
        profit_bound += (capacity - total_weight) * items[j].ratio

    return profit_bound


def knapsack_bb(values, weights, capacity):
    n = len(values)
    items = [Item(values[i], weights[i]) for i in range(n)]
    items.sort(key=lambda x: x.ratio, reverse=True)  # sort by ratio

    queue = []
    u = Node(-1, 0, 0, 0)
    queue.append(u)
    max_profit = 0

    while queue:
        u = queue.pop(0)

        if u.level == n - 1:
            continue

        v_level = u.level + 1

        # Include next item
        v_weight = u.weight + items[v_level].weight
        v_profit = u.profit + items[v_level].value
        v_bound = bound(Node(v_level, v_profit, v_weight, 0), n, capacity, items)

        if v_weight <= capacity and v_profit > max_profit:
            max_profit = v_profit

        if v_bound > max_profit:
            queue.append(Node(v_level, v_profit, v_weight, v_bound))

        # Exclude next item
        v_weight = u.weight
        v_profit = u.profit
        v_bound = bound(Node(v_level, v_profit, v_weight, 0), n, capacity, items)

        if v_bound > max_profit:
            queue.append(Node(v_level, v_profit, v_weight, v_bound))

    return max_profit


# ====== DRIVER CODE ======

print("\n=== 0/1 Knapsack using Branch and Bound ===")
n = int(input("Enter number of items: "))
values = list(map(int, input("Enter values: ").split()))
weights = list(map(int, input("Enter weights: ").split()))
capacity = int(input("Enter knapsack capacity: "))

max_val_bb = knapsack_bb(values, weights, capacity)
print("\nMaximum value (Branch and Bound):", max_val_bb)

"""
INPUT

=== 0/1 Knapsack using Branch and Bound ===
Enter number of items: 4
Enter values: 60 100 120 80
Enter weights: 10 20 30 15
Enter knapsack capacity: 50

OUTPUT

Maximum value (Branch and Bound): 260
"""