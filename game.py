from board import Board


class GameRunner:
    def __init__(self):
        """Initialize the instance of GameRunner"""
        self._board = Board()

    def get_move(self):
        """
        Provides player choice processing
        by the game program
        :return: None
        """
        while True:
            try:
                row, col = map(int, input('Enter the position: ').split())
                self._board[row, col] = 'player'
                break
            except (ValueError, AssertionError):
                print('Error!')

    def draw_board(self):
        """Print the game board"""
        print(self._board)

    def run(self):
        """
        Provides program execution
        :return: None
        """
        self._board.clear()
        print('Start:')
        self.draw_board()
        for move in range(9):
            if self._board.winner() is None:
                if move % 2:
                    self.get_move()
                else:
                    self._board[self._board.choose_next()] = 'pc'
                print(f'Move {move + 1}:')
                self.draw_board()
            else:
                break

        winner = self._board.winner()
        if winner is None:
            print('No winner')
        else:
            print(f'{winner.upper()} wins!')


def main():
    """
    Present a message to the player about
    the development of the game and provide
    a choice to continue or to end the game
    :return: None
    """
    runner = GameRunner()
    while True:
        runner.run()
        while True:
            print('Would you like to play again?')
            res = input('Yes or No: ')
            if res.lower() in ('yes', 'no'):
                break
            else:
                print('Error!')
        if res.lower() == 'no':
            break


if __name__ == '__main__':
    main()
