def flag(arr,equ):
    #print(arr,equ)
    if arr[0][0]==arr[0][1]==arr[0][2]==equ:
        return True
    if arr[1][0]==arr[1][1]==arr[1][2]==equ:
        return True
    if arr[2][0]==arr[2][1]==arr[2][2]==equ:
        return True
    if arr[0][0]==arr[1][0]==arr[2][0]==equ:
        return True
    if arr[0][1]==arr[1][1]==arr[2][1]==equ:
        return True
    if arr[0][2]==arr[1][2]==arr[2][2]==equ:
        return True
    if arr[0][0]==arr[1][1]==arr[2][2]==equ:
        return True
    if arr[2][0]==arr[1][1]==arr[0][2]==equ:
        return True
    return False
    
 
while True:
    string=input()
    if string=="end":
        break
    else:
        xcnt=0
        ocnt=0
        index=0
        arr=[[0]*3 for _ in range(3)]
        # X와 O의 갯수 COUNT
        for i in range(3):
            for j in range(3):
                arr[i][j]=string[index]
                if string[index]=="X":
                    xcnt+=1
                if string[index]=="O":
                    ocnt+=1
                index+=1
        # x의 개수가 O과 1이상 차이가 난다면 invalid
        if xcnt>ocnt+1:
            print("invalid")
            continue
        # O의 개수가 X의 개수보다 많다면 invalid
        if ocnt>xcnt:
            print("invalid")
            continue
        # O의 개수와 X의 개수가 같고 O가 우승이라면 valid
        if ocnt==xcnt:
            if flag(arr,"O") and not flag(arr,"X"):
                print("valid")
                continue
        # X의 개수가 O개수보다 한개 더 많고 X가 우승이라면 valid
        if ocnt+1==xcnt:
            if flag(arr,"X") and not flag(arr,"O"):
                print("valid")
                continue
        # 게임이 끝나고 O가 우승이 아니라면 valid
        if xcnt==5 and ocnt==4:
            if not flag(arr,"O"):
                print("valid")
                continue
        print("invalid")