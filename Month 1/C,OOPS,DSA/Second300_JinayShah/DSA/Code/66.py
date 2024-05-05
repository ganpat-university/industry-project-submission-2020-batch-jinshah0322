N = 1024


tree = [[-1] * N for _ in range(N)]


class TreeNode:
    def __init__(self):
        self.par = 0          
        self.depth = 0        
        self.size = 0         
        self.pos_segbase = 0  
        self.chain = 0        


class Edge:
    def __init__(self):
        self.weight = 0      
        self.deeper_end = 0  


class SegmentTree:
    def __init__(self):
        self.base_array = [0] * N
        self.tree = [0] * (6 * N)

node = [TreeNode() for _ in range(N)]
edge = [Edge() for _ in range(N)]
s = SegmentTree()


def add_edge(e, u, v, w):
    global tree
    tree[u-1][v-1] = e-1
    tree[v-1][u-1] = e-1
    edge[e-1].weight = w


def dfs(curr, prev, dep, n):
    global tree
    node[curr].par = prev
    node[curr].depth = dep
    node[curr].size = 1

    for j in range(n):
        if j != curr and j != node[curr].par and tree[curr][j] != -1:
            edge[tree[curr][j]].deeper_end = j
            dfs(j, curr, dep+1, n)
            node[curr].size += node[j].size


def hld(curr_node, id, edge_counted, curr_chain, n, chain_heads):
    if chain_heads[curr_chain[0]] == -1:
        chain_heads[curr_chain[0]] = curr_node

    node[curr_node].chain = curr_chain[0]
    node[curr_node].pos_segbase = edge_counted[0]
    s.base_array[edge_counted[0]] = edge[id].weight
    edge_counted[0] += 1

    spcl_chld = -1
    spcl_edg_id = 0

    for j in range(n):
        if j != curr_node and j != node[curr_node].par and tree[curr_node][j] != -1:
            if spcl_chld == -1 or node[spcl_chld].size < node[j].size:
                spcl_chld = j
                spcl_edg_id = tree[curr_node][j]

    if spcl_chld != -1:
        hld(spcl_chld, spcl_edg_id, edge_counted, curr_chain, n, chain_heads)

    for j in range(n):
        if j != curr_node and j != node[curr_node].par and j != spcl_chld and tree[curr_node][j] != -1:
            curr_chain[0] += 1
            hld(j, tree[curr_node][j], edge_counted, curr_chain, n, chain_heads)


def construct_st(ss, se, si):
    if ss == se - 1:
        s.tree[si] = s.base_array[ss]
        return s.base_array[ss]

    mid = (ss + se) // 2
    s.tree[si] = max(construct_st(ss, mid, si*2), construct_st(mid, se, si*2+1))
    return s.tree[si]


def update_st(ss, se, si, x, val):
    if ss > x or se <= x:
        pass
    elif ss == x and ss == se-1:
        s.tree[si] = val
    else:
        mid = (ss + se) // 2
        s.tree[si] = max(update_st(ss, mid, si*2, x, val), update_st(mid, se, si*2+1, x, val))
    return s.tree[si]


def change(e, val, n):
    update_st(0, n, 1, node[edge[e].deeper_end].pos_segbase, val)


def lca(u, v, n):
    lca_aux = [-1] * (n + 5)

    if node[u].depth < node[v].depth:
        u, v = v, u

    while u != -1:
        lca_aux[u] = 1
        u = node[u].par

    while v:
        if lca_aux[v] == 1:
            break
        v = node[v].par

    return v


def rmq_util(ss, se, qs, qe, index):
    if qs <= ss and qe >= se-1:
        return s.tree[index]

    if se-1 < qs or ss > qe:
        return -1

    mid = (ss + se) // 2
    return max(rmq_util(ss, mid, qs, qe, 2*index), rmq_util(mid, se, qs, qe, 2*index+1))


def rmq(qs, qe, n):
    if qs < 0 or qe > n-1 or qs > qe:
        print("Invalid Input")
        return -1

    return rmq_util(0, n, qs, qe, 1)


def crawl_tree(u, v, n, chain_heads):
    chain_u = 0
    chain_v = node[v].chain
    ans = 0

    while True:
        chain_u = node[u].chain

        if chain_u == chain_v:
            if u == v:
                pass  
            else:
                ans = max(rmq(node[v].pos_segbase+1, node[u].pos_segbase, n), ans)
            break
        else:
            ans = max(ans, rmq(node[chain_heads[chain_u]].pos_segbase, node[u].pos_segbase, n))
            u = node[chain_heads[chain_u]].par

    return ans


def max_edge(u, v, n, chain_heads):
    lca_node = lca(u, v, n)
    ans = max(crawl_tree(u, lca_node, n, chain_heads), crawl_tree(v, lca_node, n, chain_heads))
    print(f"Max edge between {u + 1} and {v + 1} is {ans}")


def main():
    global tree, s, node, edge
    
    tree = [[-1] * N for _ in range(N)]

    n = 11

    
    add_edge(1, 1, 2, 13)
    add_edge(2, 1, 3, 9)
    add_edge(3, 1, 4, 23)
    add_edge(4, 2, 5, 4)
    add_edge(5, 2, 6, 25)
    add_edge(6, 3, 7, 29)
    add_edge(7, 6, 8, 5)
    add_edge(8, 7, 9, 30)
    add_edge(9, 8, 10, 1)
    add_edge(10, 8, 11, 6)

    
    root = 0
    parent_of_root = -1
    depth_of_root = 0

    
    
    
    dfs(root, parent_of_root, depth_of_root, n)

    chain_heads = [-1] * N
    edge_counted = [0]
    curr_chain = [0]

    
    hld(root, n-1, edge_counted, curr_chain, n, chain_heads)

    
    construct_st(0, edge_counted[0], 1)

    
    
    u, v = 11, 9
    print(f"Max edge between {u + 1} and {v + 1} is ", end="")
    max_edge(u-1, v-1, n, chain_heads)

    
    change(8-1, 28, n)

    print(f"After Change: max edge between {u + 1} and {v + 1} is ", end="")
    max_edge(u-1, v-1, n, chain_heads)

    v = 4
    print(f"Max edge between {u + 1} and {v + 1} is ", end="")
    max_edge(u-1, v-1, n, chain_heads)

    
    change(5-1, 22, n)
    print(f"After Change: max edge between {u + 1} and {v + 1} is ", end="")
    max_edge(u-1, v-1, n, chain_heads)

if __name__ == "__main__":
    main()
