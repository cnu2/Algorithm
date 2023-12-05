p, m = map(int, input().split()) #플레이어의 수, 방 한개의 정원
_queue = []
for _ in range(p):
    # player = list(map(str, input().split())) #[레벨, 닉네임]
    l, n = input().split()
    if not _queue:
        # _queue.append([player])
        _queue.append([[int(l),n]])
        continue

    enter = False    

    for q in _queue:
        if len(q) < m and q[0][0]-10 <= int(l) <= q[0][0]+10:
            q.append([int(l),n])
            enter = True
            break
    
    if enter == False:
        # _queue.append([player])
        rooms.append([[int(l),n]])


for q in _queue:
    q.sort(key=lambda x: x[1])
breakpoint()
for q in _queue:
    if len(q) == m:
        print("Started!")
    else:
        print("Waiting!")
    for p in q:
        print(p[0], p[1])
    