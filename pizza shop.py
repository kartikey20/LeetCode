def solve(pizzas, toppings, x):
    pizzas = set(pizzas)
    toppings = set(toppings)
    min_diff = float('inf')
    ans = 0
    for pizza in pizzas:
        cost = pizza
        diff = abs(cost - x)
        if diff <= min_diff:
            min_diff = diff
            ans = cost
        elif diff == min_diff:
            ans = min(ans, cost)
        for topping in toppings:
            cost += topping
            diff = abs(cost - x)
            if diff < min_diff:
                min_diff = diff
                ans = cost
            elif diff == min_diff:
                ans = min(ans, cost)
    return ans
    # Time Complexity: O(n^2)
    # Space Complexity: O(N)


print(solve([800, 850, 900], [100, 150], 1000))
