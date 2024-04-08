"""
Tic Tac Toe Player

Group Members:

╔═══════╦════════════════════════════╦════════════╗
║ Sr No ║            Name            ║ Student ID ║
╠═══════╬════════════════════════════╬════════════╣
║   1   ║ Tirth Shailesh Thoria      ║ 031149064  ║
║   2   ║ Avantika Singh             ║ 031376590  ║
║   3   ║ Laksh Chandrabhan Jadhwani ║ 032166249  ║
╚═══════╩════════════════════════════╩════════════╝

"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns the starting state of the tic-tac-toe board.

    The board is represented as a 3x3 matrix, where each element represents a cell on the board.
    The initial state of the board is empty, with all cells set to the value of EMPTY.

    Returns:
    - list: A 3x3 matrix representing the starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns the player who has the next turn on a board.

    Parameters:
    - board (list): The current state of the tic-tac-toe board.

    Returns:
    - str: The player symbol ('X' or 'O') who has the next turn.

    """
    _x = sum(r.count(X) for r in board)
    _o = sum(r.count(O) for r in board)
    return O if _x > _o else X


def actions(board):
    """
    Returns a set of all possible actions (i, j) available on the board.

    Parameters:
    - board (list): The current state of the tic-tac-toe board.

    Returns:
    - set: A set of tuples representing the available actions on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    Parameters:
    - board: The current state of the tic-tac-toe board.
    - action: The move to be made on the board, represented as a tuple (i, j).

    Returns:
    - _board: The updated board after making the move.

    Raises:
    - Exception: If an invalid action is performed.

    """
    if action not in actions(board):
        raise Exception("Invalid action was performed!.")
    _board = copy.deepcopy(board)
    _board[action[0]][action[1]] = player(board)
    return _board


def winner(board):
    """
    Returns the winner of the game, if there is one.

    Parameters:
    - board (list): The game board represented as a 3x3 list of characters.

    Returns:
    - str or None: The winner of the game. Returns 'O' if player O wins, 'X' if player X wins, or None if there is no winner.
    """
    lines = (
        [list(row) for row in board]
        + [list(col) for col in zip(*board)]
        + [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    )
    for l in lines:
        if l == ["O", "O", "O"]:
            return "O"
        if l == ["X", "X", "X"]:
            return "X"
    return None


def terminal(board):
    """
    Returns True if the game is over, False otherwise.

    Parameters:
    - board (list): The current state of the tic-tac-toe board.

    Returns:
    - bool: True if the game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns the utility value of the current game state.

    Parameters:
    - board (list): The current game board.

    Returns:
    - int: The utility value of the game state. Returns 1 if X has won the game,
           -1 if O has won, and 0 otherwise.
    """
    if winner(board) == O:
        return -1
    if winner(board) == X:
        return 1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    Parameters:
    - board: The current state of the tic-tac-toe board.

    Returns:
    - move: The optimal action to be taken by the current player.

    The minimax algorithm is used to determine the best move for the current player on the given board.
    It recursively evaluates all possible moves and their resulting board states to find the move that
    maximizes the current player's chances of winning or minimizes the opponent's chances of winning.

    The algorithm works by assuming that both players play optimally and make the best move at each step.
    It evaluates each possible move by recursively calling the `value` function, which returns a score
    for the current board state. The move with the highest score is chosen if the current player is 'X',
    and the move with the lowest score is chosen if the current player is 'O'.

    The `value` function is a helper function that recursively evaluates the board states and returns
    the score and the corresponding move. It uses the `terminal` function to check if the game has ended,
    and the `utility` function to assign a score to the terminal board states.

    Note: This implementation assumes that the `terminal`, `player`, `actions`, `result`, and `utility`
    functions are defined elsewhere in the code.

    Example usage:
    >>> board = [['X', 'O', 'X'],
                 ['O', 'X', 'O'],
                 [' ', ' ', ' ']]
    >>> minimax(board)
    (2, (2, 0))

    In the above example, the optimal move for the current player ('X') on the given board is to place
    their symbol at position (2, 0), which results in a score of 2.

    """
    if terminal(board):
        return None

    def value(board):
        if terminal(board):
            return utility(board), None

        if player(board) == X:
            best_score = float("-inf")
            best_move = None
            for action in actions(board):
                score, _ = value(result(board, action))
                if score > best_score:
                    best_score = score
                    best_move = action
            return best_score, best_move
        else:
            best_score = float("inf")
            best_move = None
            for action in actions(board):
                score, _ = value(result(board, action))
                if score < best_score:
                    best_score = score
                    best_move = action
            return best_score, best_move

    _, move = value(board)
    return move
