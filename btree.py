import copy
from btnode import BinaryTreeNode


class BinaryGameTree:
    def __init__(self):
        """
        Initialize the instance
        of BinaryGameTree
        """
        self.root = None

    def count_score(self):
        """
        Count the score for for the left
        and right branches of the binary tree
        :return: None
        """
        def count(root):
            if root.left is not None:
                count(root.left)
                root.score += root.left.score
            if root.right is not None:
                count(root.right)
                root.score += root.right.score

        count(self.root)

    @staticmethod
    def add(root):
        """
        Add an element to one of the branches
        of a binary tree depending on its current state
        :param root: BinaryTreeNode
        :return: None
        """
        variants = root.item.generate_moves()
        if len(variants) == 0 or root.item.winner() is not None:
            root.score = root.item.score()
        else:
            last = root.item.last
            if last is None:
                marker = 'pc'
            else:
                marker = 'pc' if root.item[last] == 'player' else 'player'
            root.left = BinaryTreeNode(copy.deepcopy(root.item))
            root.left.item[variants[0]] = marker
            if len(variants) == 2:
                root.right = BinaryTreeNode(copy.deepcopy(root.item))
                root.right.item[variants[1]] = marker

    def generate_tree(self):
        """
        Generate a binary tree
        by recursive addition
        :return: None
        """
        def create_children(root):
            BinaryGameTree.add(root)
            if root.left is not None:
                create_children(root.left)

            if root.right is not None:
                create_children(root.right)

        create_children(self.root)
