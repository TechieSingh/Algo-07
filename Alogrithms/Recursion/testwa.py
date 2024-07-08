def getMaximumThroughput(throughput, scaling_cost, budget):
    n = len(throughput)
    dp = [0] * (budget + 1)
    
    for i in range(n):
        for b in range(budget, scaling_cost[i] - 1, -1):
            max_increase = b // scaling_cost[i]
            for x in range(1, max_increase + 1):
                dp[b] = max(dp[b], dp[b - x * scaling_cost[i]] + throughput[i] * x)
    
    max_throughput = float('inf')
    for b in range(budget + 1):
        min_throughput = float('inf')
        for i in range(n):
            current_throughput = throughput[i] * (1 + dp[b] // throughput[i])
            min_throughput = min(min_throughput, current_throughput)
        max_throughput = min(max_throughput, min_throughput)
    
    return int(max_throughput)

# Sample input
throughput = [4, 2, 7]
scaling_cost = [3, 5, 6]
budget = 32

result = getMaximumThroughput(throughput, scaling_cost, budget)
print(result)  # Expected output: 10
