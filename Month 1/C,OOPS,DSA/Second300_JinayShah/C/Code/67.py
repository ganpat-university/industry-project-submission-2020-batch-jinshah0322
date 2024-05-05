def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    value_per_weight = [(v / w, w) for v, w in zip(values, weights)]
    value_per_weight.sort(reverse=True)

    total_value = 0
    remaining_capacity = capacity

    for value_per_unit, weight in value_per_weight:
        if remaining_capacity >= weight:
            total_value += value_per_unit * weight
            remaining_capacity -= weight
        else:
            total_value += value_per_unit * remaining_capacity
            break

    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
result = fractional_knapsack(weights, values, capacity)
print(f"Maximum value for knapsack with fractional weights: {result}")
