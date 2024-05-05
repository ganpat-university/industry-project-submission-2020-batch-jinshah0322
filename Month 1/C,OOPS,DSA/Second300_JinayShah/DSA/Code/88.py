import math

class VanEmdeBoasTree:
    def __init__(self, universe_size):
        self.u = universe_size
        if self.u == 2:
            self.min_value = None
            self.max_value = None
        else:
            upper_bound = 2 ** (math.ceil(math.log2(self.u) / 2))
            lower_bound = 2 ** (math.floor(math.log2(self.u) / 2))
            self.cluster_size = upper_bound
            self.sqrt_u = int(math.sqrt(self.u))
            self.summary = VanEmdeBoasTree(self.sqrt_u)
            self.clusters = [VanEmdeBoasTree(lower_bound) for _ in range(self.sqrt_u)]

    def high(self, x):
        return x // self.cluster_size

    def low(self, x):
        return x % self.cluster_size

    def index(self, x, y):
        if x is not None and y is not None:
            return x * self.cluster_size + y
        else:
            return None

    def insert(self, x):
        if self.u == 2:
            if x == 0:
                self.min_value = 0
            elif x == 1:
                self.max_value = 1
        else:
            cluster_index = self.high(x)
            cluster_low = self.low(x)
            self.clusters[cluster_index].insert(cluster_low)
            self.summary.insert(cluster_index)

    def delete(self, x):
        if self.u == 2:
            if x == 0:
                self.min_value = None
            elif x == 1:
                self.max_value = None
        else:
            cluster_index = self.high(x)
            cluster_low = self.low(x)
            self.clusters[cluster_index].delete(cluster_low)

            if self.clusters[cluster_index].minimum() is None:
                self.summary.delete(cluster_index)

    def minimum(self):
        if self.u == 2:
            return self.min_value
        else:
            cluster_index = self.summary.minimum()
            if cluster_index is None:
                return None
            cluster_low = self.clusters[cluster_index].minimum()
            return self.index(cluster_index, cluster_low)

    def maximum(self):
        if self.u == 2:
            return self.max_value
        else:
            cluster_index = self.summary.maximum()
            if cluster_index is None:
                return None
            cluster_low = self.clusters[cluster_index].maximum()
            return self.index(cluster_index, cluster_low)

    def successor(self, x):
        if self.u == 2:
            if x == 0 and self.maximum() == 1:
                return 1
            else:
                return None
        else:
            cluster_index = self.high(x)
            cluster_low = self.low(x)
            max_low = self.clusters[cluster_index].maximum()

            if max_low is not None and cluster_low < max_low:
                offset = self.clusters[cluster_index].successor(cluster_low)
                return self.index(cluster_index, offset)
            else:
                succ_cluster = self.summary.successor(cluster_index)
                if succ_cluster is None:
                    return None
                succ_low = self.clusters[succ_cluster].minimum()
                return self.index(succ_cluster, succ_low)

    def predecessor(self, x):
        if self.u == 2:
            if x == 1 and self.minimum() == 0:
                return 0
            else:
                return None
        else:
            cluster_index = self.high(x)
            cluster_low = self.low(x)
            min_low = self.clusters[cluster_index].minimum()

            if min_low is not None and cluster_low > min_low:
                offset = self.clusters[cluster_index].predecessor(cluster_low)
                return self.index(cluster_index, offset)
            else:
                pred_cluster = self.summary.predecessor(cluster_index)
                if pred_cluster is None:
                    return None
                pred_low = self.clusters[pred_cluster].maximum()
                return self.index(pred_cluster, pred_low)



v = VanEmdeBoasTree(16)
v.insert(1)
v.insert(3)
v.insert(5)
v.insert(7)
v.insert(9)
v.insert(11)
v.insert(13)
v.insert(15)

print("Minimum:", v.minimum())  
print("Maximum:", v.maximum())  

v.delete(7)
print("Successor of 5:", v.successor(5))  
print("Predecessor of 13:", v.predecessor(13))  
