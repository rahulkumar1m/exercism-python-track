from typing import NamedTuple


class Record(NamedTuple):
    record_id: int
    parent_id: int

    def __lt__(self, other):
        return self.record_id < other.record_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []
        self.add_child = self.children.append


def BuildTree(records):
    if not records:
        return None

    trees = []
    records.sort()
    for ii, record in enumerate(records):
        record_id, parent_id = record 
        if ii != record_id:
            raise ValueError('Tree must be continuous and start with id 0')
        if record_id < parent_id:
            raise ValueError('Parent id must be lower than child id')
        if record_id == parent_id != 0:
            raise ValueError('Tree is a cycle')

        node = Node(record_id)
        trees.append(node)
        if record_id != 0:
            parent = trees[parent_id]
            parent.add_child(node)

    return trees[0]