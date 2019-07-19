from __future__ import annotations

"""Class to calculate the average value of the nodes in a tree"""


class Node:
    """Represents a single node in a tree structure"""

    def __init__(self, value: int):
        self.value = value
        self.children = []

    def get_value(self) -> int:
        """
        :return int value of the node
        """
        return self.value

    def get_children(self) -> list:
        """
        :return list of children this node has
        """
        return self.children

    def add_child(self, node: Node) -> None:
        self.children.append(node)


def get_average(root: Node) -> float:
    """
    Please implement this method to return the average of all node values (Node.getValue()) in the tree.

    :param root the root node of a tree from which to determine the average value
    :return the average of all node values in the tree
    """

    # todo
    return -1
