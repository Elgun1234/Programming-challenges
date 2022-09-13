
def factor():
    while True :
        answer = int(input("YOU: select a number between 10 and 49 "))
        if answer > 10 and answer <49:
            break
    factor = 99 - answer
    return factor

def friend():
    while True:
        friend = int(input("FRIEND: select a number between 50 and 99 "))
        if friend >50 and friend <99:
            break
    return friend

def remove_hundred(friend):
    str(friend)
    friend[0,1]
    print(friend)
            

if __name__ == '__main__':
    unittest.main()

factor = factor()
friend = friend()
