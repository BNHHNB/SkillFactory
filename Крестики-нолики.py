# Выбор
gamer = input("За кого вы играете за X или O?: ")
player1 = "X"
player2 = "O"
if gamer == "x":
    gamer = player1
    print(f"Вы Игрок 1 это - {player1} и Игрок 2 это - {player2}")
else:
    gamer = player2
    print(f"Игрок 1 это - {player1} и вы Игрок 2 это - {player2}")

board = [" " for x in range(9)]


# Приветствие и начало игры
def startGame():
    print("Добро пожаловать в крестики-нолики!")
    printBoard()
    playerTurn("1")


# Создание игровой доски
def printBoard():
    print("     |     |     ")
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  ")
    print("     |     |     ")


# Какой игрок сейчас ходит и сделан ли уже такой ход
def playerTurn(turn):
    position = input(f"Игрок {turn}, твой ход выбери клетку от 1-9: ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Такой клетки нет, выбери клетку от 1-9: ")
    position = int(position)
    symbol = player1 if turn == "1" else player2
    if board[position - 1] == " ":
        board[position - 1] = symbol
        printBoard()
        if checkWin():
            return
        turn = "2" if turn == "1" else "1"
        playerTurn(turn)
    else:
        print("Прости такой ход уже сделан, попробуй еще раз")
        playerTurn(turn)


def checkWin():
    # Проверка вертикальных линий
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            if board[i] == player1:
                print("Поздравляю игрок 1 ты победил по вертикальной линии!")
            elif board[i] == player2:
                print("Поздравляю игрок 2 ты победил по вертикальной линии!")
            return True
    # Проверка горизонтальных линии
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            if board[i] == player1:
                print("Поздравляю Игрок 1 ты победил по горизонтальной линии!")
            elif board[i] == player2:
                print("Поздравляю Игрок 2 ты победил по горизонтальной линии!")
            return True
    #  Проверка косых линий
    if board[0] == board[4] == board[8] != " ":
        if board[0] == player1:
            print("Поздравляю Игрок 1 ты победил по диагонали!")
        elif board[0] == player2:
            print("Поздравляю Игрок 2 ты победил по диагонали!")
        return True
    if board[2] == board[4] == board[6] != " ":
        if board[2] == player1:
            print("Поздравляю Игрок 1 ты победил по диагонали!")
        elif board[2] == player2:
            print("Поздравляю Игрок 2 ты победил по диагонали!")
        return True
    if " " not in board:
        print("Невероятно это ничья!")
        return True


startGame()
