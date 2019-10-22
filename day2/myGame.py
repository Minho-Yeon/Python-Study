import random
def makeLotto(num):
    lotto=[]
    for i in range(num):
        lotto.append([])
        for j in range(6):
            lotto[i].append(random.randint(1,45))
        print("게임 %d"%(i+1),lotto[i])

def option1(day,salary):
    dolar=day*salary
    
    go = list(str(dolar))
    num=-3
    while True:
        if num<=-1*len(go):
            break;
        go.insert(num,",")
        num-=4
    go="".join(go)+".00"
    print("Option 1 pay : $%s"%go)
    return dolar
def option2(day,salary=1):
    dolar=0
    for i in range(day):
        dolar+=2**i
    go = list(str(dolar))
    num=-3
    while True:
        if num<=-1*len(go):
            break;
        go.insert(num,",")
        num-=4
    go="".join(go)+".00"
    print("Option 2 pay : $%s"%go)
    return dolar
