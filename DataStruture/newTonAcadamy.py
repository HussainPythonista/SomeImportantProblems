
def TicTokToe(players):
    if players[0]=="J" or players[1]=="J":
        if players[0]=="J":
            return players[0]
        elif players[1]=="J":
            return players[0]
    elif players[0]=="R" or players[1]=="R":
        return "R"
    else:
        return "D"
players=input().split(" ")
print(TicTokToe(players))
