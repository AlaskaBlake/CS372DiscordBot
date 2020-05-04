import discord
from discord.ext import commands


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


async def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("Whats your move")
        await TikTakToe.move
        move = TikTakToe.move
    return int(move)


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if board.isSpaceFree(board, i):
            return False
    return True


class TikTakToe(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def move(self, ctx, move):
        await ctx.send("What's your move?")
        return move

    @commands.command()
    async def tictactoe(self, ctx):
        while True:
            # Reset the board
            theBoard = [' '] * 10
            player1, player2 = ['X', 'O']
            turn = 'player_x'
            await ctx.send('The "X" will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player_x':
                    # Player's turn.

                    await ctx.send('~' + theBoard[7] + '~|~' + theBoard[8] + '~|~' + theBoard[9] + '~')
                    await ctx.send('----------')
                    await ctx.send('~' + theBoard[4] + '~|~' + theBoard[5] + '~|~' + theBoard[6] + '~')
                    await ctx.send('----------')
                    await ctx.send('~' + theBoard[1] + '~|~' + theBoard[2] + '~|~' + theBoard[3] + '~')

                    move = getPlayerMove(theBoard)
                    makeMove(theBoard, player1, move)

                    if isWinner(theBoard, player1):
                        # drawBoard(theBoard)
                        await ctx.send('Hooray! X has won the game!')
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            # drawBoard(theBoard)
                            await ctx.send('The game is a tie!')
                            break
                        else:
                            turn = 'player_o'

                else:
                    # Player's turn.
                    # drawBoard(theBoard)
                    move = getPlayerMove(theBoard)
                    makeMove(theBoard, player2, move)

                    if isWinner(theBoard, player2):
                        # drawBoard(theBoard)
                        await ctx.send('Hooray! O has won the game!')
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            # drawBoard(theBoard)
                            await ctx.send('The game is a tie!')
                            break
                        else:
                            turn = 'player_x'

            if not playAgain():
                break


def setup(client):
    client.add_cog(TikTakToe(client))
