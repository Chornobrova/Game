import random
from btree import BinaryGameTree
from btnode import BinaryTreeNode


class Board:
    EMPTY = ' '
    MARKERS = {'player': 'X', 'pc': '0'}

    def __init__(self):
        """
        Initialize the instance of Board
        """
        self.clear()
        self.rows = None
        self.available = None
        self.last = None

    def clear(self):
        """
        Clear the board from the marks
        defined on it earlier
        :return: None
        """
        self.rows = []
        for i in range(3):
            self.rows.append([self.EMPTY] * 3)
        self.available = {(i, j) for i in range(3)
                          for j in range(3)}
        self.last = None

    def __getitem__(self, indexes):
        """
        Get item from the game board
        :param indexes: list or tuple
        :return: str or None
        """
        assert 0 <= indexes[0] <= 2 and \
               0 <= indexes[1] <= 2, 'Bad position'
        inverted_markers = {val: key for key, val in self.MARKERS.items()}
        return inverted_markers.get(self.rows[indexes[0]][indexes[1]], None)

    def __setitem__(self, indexes, side):
        """
        Set an item on the game board
        :param indexes: list or tuple
        :param side: str
        :return: None
        """
        assert (indexes[0], indexes[1]) in self.available, \
            'Bad position'
        assert side in self.MARKERS, \
            'Side parameter must be in MARKERS keys'
        self.rows[indexes[0]][indexes[1]] = self.MARKERS[side]
        self.available.remove((indexes[0], indexes[1]))
        self.last = (indexes[0], indexes[1])

    def generate_moves(self):
        """
        Return a list of possible next
        moves for computer
        :return: list
        """
        try:
            return random.sample(self.available, 2)
        except ValueError:
            return list(self.available)

    def score(self):
        """
        Count a game score
        :return: int
        """
        winner = self.winner()
        if winner == 'pc':
            return 1
        elif winner == 'player':
            return -1
        else:
            return 0

    def winner(self):
        """
        Define a winner to calculate
        the results
        :return: str or None
        """
        variants = [[(i, j) for i in range(3)] for j in range(3)] \
                   + [[(j, i) for i in range(3)] for j in range(3)] \
                   + [[(i, i) for i in range(3)],
                      [(i, 2 - i) for i in range(3)]]
        for case in variants:
            if (self[case[0]]
                    == self[case[1]]
                    == self[case[2]]
                    and self[case[0]] is not None):
                return self[case[0]]
        return None

    def choose_next(self):
        """
        Identify the next player
        :return: str or None
        """
        game_tree = BinaryGameTree()
        game_tree.root = BinaryTreeNode(self)
        game_tree.generate_tree()
        left_tree = game_tree.root.left
        right_tree = game_tree.root.right
        if left_tree is None:
            return None
        elif right_tree is None:
            return left_tree.item.last
        else:
            game_tree.count_score()
            if left_tree.score >= right_tree.score:
                return left_tree.item.last
            else:
                return right_tree.item.last

    def __str__(self):
        """
        Represent a game bord
        in a string
        :return: str
        """
        string = ''
        for row in self.rows:
            string += f'[{"][".join(row)}]\n'
        return string[:-1]
