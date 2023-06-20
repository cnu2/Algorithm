"""
https://www.acmicpc.net/problem/1475
3/3
1. 23/05/11
2. 23/05/18
3. 23/06/20
"""

"""
[문제]
다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. 

(6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.

"""

"""
[sudo code]
- num을 입력
- num_list = str(num)
- num_arr = [0] * 10 
- num_list의 숫자 하나씩 본다
    - 6 또는 9 이면
        - num[6] 또는 num[9] 에서 적은쪽에 넣어준다. 
    - 그렇지 않으면 num_arr에 넣어준다.
- num_arr중에 max를 출력한다.

"""
num_list = list(map(int, input()))
num_arr = [0] * 10
for i in num_list:
    if i == 6 or i == 9:
        if num_arr[6] >= num_arr[9]:
            num_arr[9] += 1
        else:
            num_arr[6] += 1
    else:
        num_arr[i] += 1

print(max(num_arr))