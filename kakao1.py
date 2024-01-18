# 카카오 인턴 코테 1번 문제
'''
friends 리스트와 gift리스트가 들어온다.
friends = [m, r, f, n]
gift = ["m f", "m, f"...]

gift_table = [[-1,0,2,0],[3,-1,0,0],[1,1,-1,0],[1,0,0,-1]]
gift_value = for문을 돌면서 준것과 받은걸 합친다.
예를 들어 index 0번을 돌고 있다면 index0에 해당하는걸 sum()+1해주고
    다시 for문을 돌려 index 0 에 해당하는걸 더해준다.
    그리고 이 두값을 더해준다.

for friend in gift_table:
    gift_talbe에서 -1을 만난다면 continue

    else: gift_table에서 숫자를 만난다면 
        if value가 0이다.
            해당하는 gift_talbe에서 그도 0인지 확인하다.
            만약 그렇다면 
            gift_value로가서 해당 index의 giftvalue랑 비교한다.
        else:
            상대방이랑 비교한다.


'''