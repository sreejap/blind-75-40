# 1. Build graph
# 2. Visit each node
# 3. DFS to collect component
# 4. Sort + return

from collections import defaultdict
class Solution:
    def __init__(self):
        self.visited = set()
        self.adjacent = defaultdict(list) # this returns and empty list when key doesn't exists

    def dfs(self, merged_account, email):
        self.visited.add(email)
        merged_account.append(email)

        if email not in self.adjacent:
            return

        for neighbor in self.adjacent[email]:
            if neighbor not in self.visited:
                self.dfs(merged_account, neighbor)
                
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Step 1: Build adjacency list
        for account in accounts:
            first_email = account[1]

            for j in range(2, len(account)):
                email = account[j]

                self.adjacent[first_email].append(email)
                self.adjacent[email].append(first_email)

        # Step 2: DFS to find connected components
        merged_accounts = []

        for account in accounts:
            name = account[0]
            first_email = account[1]

            if first_email not in self.visited:
                merged_account = [name]

                self.dfs(merged_account, first_email)

                # Sort only emails (skip name at index 0)
                merged_account[1:] = sorted(merged_account[1:])
                merged_accounts.append(merged_account)

        return merged_accounts
