import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('gamexoonline-firebase-adminsdk-ekhyl-0bf647ad55.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://gamexoonline-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
tictactie_ref = db.reference('tic_tac_toe')

table_ref = tictactie_ref.child('table')
table_ref.set({"name": "tictactore-table"})

table = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


def show_table():  # ตารางXO
    for column in table:
        print("|", end="")
        for row in column:
            print(str(row) + "|", end="")
        print("")
    return


def choosing_position(player_symbol):
    print('player:' + player_symbol)
    position = int(input('choose:'))
    if position <= 3:
        while type(table[0][position - 1]) is str:
            print('ช่องนี้มีผู้เล่นเลือกเเล้ว โปรดใส่เลขใหม่')
            position = int(input('position:'))
        table[0][position - 1] = player_symbol

    elif position <= 6:
        while type(table[1][position - 4]) is str:
            print('ช่องนี้มีผู้เล่นเลือกเเล้ว โปรดใส่เลขใหม่')
            position = int(input('position:'))
        table[1][position - 4] = player_symbol

    elif position <= 9:
        while type(table[2][position - 7]) is str:
            print('ช่องนี้มีผู้เล่นเลือกเเล้ว โปรดใส่เลขใหม่')
            position = int(input('position:'))
        table[2][position - 7] = player_symbol

    return


def check_winner(player_symbol):
    if table[0] == [player_symbol, player_symbol, player_symbol] or table[1] == [player_symbol, player_symbol,
                                                                                 player_symbol] or table[2] == [
        player_symbol, player_symbol, player_symbol]:  # ทั้งแถวเป็น x
        print(player_symbol + ' is winner!')
        return True
    elif table[0][0] == player_symbol and table[1][0] == player_symbol and table[2][0] == player_symbol or table[0][
        1] == player_symbol and table[1][1] == player_symbol and table[2][1] == player_symbol or table[0][
        2] == player_symbol and table[1][2] == player_symbol and table[2][2] == player_symbol:  # ทั้งหลักเป็น x
        print(player_symbol + ' is winner!')
        return True
    elif table[0][0] == player_symbol and table[1][1] == player_symbol and table[2][
        2] == player_symbol:  # แนวทะเเยงขวาเป็น x
        print(player_symbol + ' is winner!')
        return True
    elif table[0][2] == player_symbol and table[1][1] == player_symbol and table[2][
        0] == player_symbol:  # แนวทเเยงซ้ายเป็น x
        print(player_symbol + ' is winner!')
        return True
    elif i == 5:
        print('เสมอกันนะจ๊ะ')
        return True
    else:
        return False


i=0
print('choosing new game or join game.')
print('1 for new game')
print('2 for join game')
number = input('1 or 2:')
if number=='1':
    table_ref.set({"data": table})
    while True:
        i+=1

        show_table()
        choosing_position('X')
        if check_winner('X') is True:

            table_ref.set({"data": table})
            break
        elif check_winner('O') is True:

            table_ref.set({"data": table})
            break
        table_ref.set({"data": table})
        table = table_ref.get()['data']
        while True:
            if table != table_ref.get()['data']:
                table = table_ref.get()['data']
                break
        if check_winner('X'):

            break
        elif check_winner('O'):

            break
elif number=='2':

            while True:
                while True:
                    if table!=table_ref.get()['data']:
                        table=table_ref.get()['data']
                        break
                i += 1
                if check_winner('O') is True:

                    break
                elif check_winner('X') is True:

                    break
                show_table()
                choosing_position('O')
                table_ref.set({"data": table})
                table = table_ref.get()['data']

                if check_winner('X'):

                    break
                elif check_winner('O'):

                    break
show_table()