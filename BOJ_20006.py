p, m = map(int, input().split()) #플레이어의 수, 방 한개의 정원
_queue = []
for _ in range(p):
    player = list(map(str, input().split())) #[레벨, 닉네임]
    if not _queue:
        _queue.append([player])
        continue

    enter = False    

    for q in _queue:
        if len(q) < m and int(q[0][0])-10 <= int(player[0]) <= int(q[0][0])+10:
            q.append(player)
            enter = True
            break
    
    if enter == False:
        _queue.append([player])

for q in _queue:
    q.sort(key=lambda x: x[1])
# breakpoint()
for q in _queue:
    if len(q) == m:
        print("Started!")
    else:
        print("Waiting!")
    for p in q:
        print(p[0], p[1])