from typing import List
from collections import defaultdict

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    parent  = {}
    parentToName = {}

    def find(email:str)->str:
        if parent[email] == email:
            return email
        parent[email] = find(parent[email])
        return parent[email]
    
    def union(email1: int, email2:str):
        root1 = find(email1)
        root2 = find(email2)

        if root1 != root2:
            parent[root1] = root2
            return True
        
        return False

    # initialize x -> x (equivalent to array with index position same as the value)
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            parent[email] = email
            parentToName[email] = name
    
    for account in accounts:
        firstEmail = account[1]
        for email in account[1:]:
            union(firstEmail, email)


    result_groups = defaultdict(list)
    for email, parentEmail in parent.items():
        root_email = find(parentEmail)
        result_groups[root_email].append(email)

    final_accounts = []
    for rootEmail, emails in result_groups.items():
        name = parentToName[rootEmail] # Get name from representative email
        final_accounts.append([name] + sorted(emails))
        
    return final_accounts


accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

print(accountsMerge(accounts))
