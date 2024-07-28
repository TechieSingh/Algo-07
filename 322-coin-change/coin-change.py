class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Handle the special case where the amount is 0
        if amount == 0:
            return 0
        
        class CoinChange:
            def __init__(self, coins, amount, changes, work, show=False):
                self.calculate_changes(coins, amount, changes, work, show)
                
            def calculate_changes(self, coins, amount, changes, work, show):
                dp = [float('inf')] * (amount + 1)  
                dp[0] = 0  
                work[0] = 0  

                for i in range(1, amount + 1):
                    for coin in coins:
                        work[0] += 1  
                        if i - coin >= 0:
                            dp[i] = min(dp[i], dp[i - coin] + 1)
                            if show:
                                print(f"dp[{i}] updated to {dp[i]} using coin {coin}")

                if dp[amount] == float('inf'):
                    changes.append(-1)
                    return

                current_amount = amount
                while current_amount > 0:
                    for coin in coins:
                        if current_amount - coin >= 0 and dp[current_amount] == dp[current_amount - coin] + 1:
                            changes.append(coin)
                            current_amount -= coin
                            break

        changes = []
        work = [0]
        CoinChange(coins, amount, changes, work, show=False)
        
        return len(changes) if changes and changes[0] != -1 else -1
