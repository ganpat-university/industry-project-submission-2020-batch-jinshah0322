class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        self.parent[parent_u] = parent_v

def job_sequencing_with_disjoint_set(jobs):
    
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    disjoint_set = DisjointSet(max_deadline)

    result = [0] * max_deadline
    total_profit = 0

    
    for job in jobs:
        deadline = job[1]
        slot = disjoint_set.find(deadline)

        
        if slot > 0:
            result[slot - 1] = job[0]
            disjoint_set.union(slot, slot - 1)
            total_profit += job[2]

    return result, total_profit


jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
sequence, profit = job_sequencing_with_disjoint_set(jobs)
print("Job Sequence:", sequence)
print("Total Profit:", profit)
