import math
from collections import Counter

# read the input
# input_file, N = "D8_input_test.txt", 10
input_file, N = "D8_input.txt", 1000


class Node:
    def __init__(self, x: str, y: str, z: str, node_id: int) -> None:
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.node_id = node_id

    @property
    def id(self) -> int:
        return self.node_id

    def dist(self, node: "Node") -> float:
        x2 = (self.x - node.x) ** 2
        y2 = (self.y - node.y) ** 2
        z2 = (self.z - node.z) ** 2
        return math.sqrt(x2 + y2 + z2)

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False

        if self.size[root_i] < self.size[root_j]:
            root_i, root_j = root_j, root_i

        self.parent[root_j] = root_i
        self.size[root_i] += self.size[root_j]
        return True


nodes: list[Node] = []
with open(input_file) as file:
    # read each line and store as node obj
    for line in file:
        x, y, z = line.split(",")
        nodes.append(Node(x, y, z, len(nodes)))

# calculate distance between all pairs of nodes
distances: list[tuple[float, Node, Node]] = []
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        dist = nodes[i].dist(nodes[j])
        distances.append((dist, nodes[i], nodes[j]))
distances.sort(key=lambda x: x[0])  # sort from closest to farthest


def product_of_three_largest(n_distances: list) -> int:
    # put each node in a group ("circuit") using union find technique
    uf = UnionFind(len(nodes))
    for _, node_a, node_b in n_distances:
        uf.union(node_a.id, node_b.id)

    # count how many items in each circuits
    group_ids = [uf.find(i) for i in range(len(nodes))]
    counts = list(Counter(group_ids).values())

    # sort to find largest 3 circuits and return product
    counts.sort(reverse=True)
    return math.prod(counts[:3])


def last_x_product(distances: list) -> int:
    # put each node in a group ("circuit") using union find technique
    uf = UnionFind(len(nodes))

    # initially, each item is in its own circuit
    count_groups = len(nodes)
    for _, node_a, node_b in distances:
        # returns true only when nodes were in different groups before join
        if uf.union(node_a.id, node_b.id):
            count_groups -= 1  # one less group
            if count_groups == 1:
                return node_a.x * node_b.x  # last x product

    return 0


print("Problem 1", product_of_three_largest(distances[:N]))
print("Problem 2", last_x_product(distances))
