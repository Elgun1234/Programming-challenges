def answer():
    while True :
        answer = int(input("YOU: select a number between 10 and 49 "))
        if answer > 10 and answer <49:
            break
    return answer

def factor():
    factor = 99 - answer
    return factor

def friend(factor_answer):
    while True:
        friend_inp = int(input("FRIEND: select a number between 50 and 99 "))
        if friend_inp >50 and friend_inp <99:
            break
    fri = friend_inp + factor_answer
    hundred_dig = fri // 100
    
    for i in range(0,8):
        
        if i == hundred_dig :
            hundred_to_one = hundred_dig * 100
            fri -= hundred_to_one
            fri += hundred_dig
            friend_inp -= fri
    return friend_inp
    
    
    

if __name__ == '__main__':
    
    answer = answer()
    factor_answer = factor()
    x = friend(factor_answer)
    print(f"I said the answer was {answer} and the calculation result is {x}")
    

