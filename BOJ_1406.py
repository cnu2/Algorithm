# def order(word, command, cursor):
#     c = command.split()
#     if len(c) == 2: # P일 떄
#         if cursor == len(word): # 커서가 맨 뒤에 있을 때
#             word.append(c[1])
#             cursor += 1
#         elif cursor == 0:
#             word = [c[1]] + word
#         else:
#             word = word[0:cursor] + [c[1]] + word[cursor:]
#             cursor += 1
#     else:
#         if c[0] == 'L':
#             if cursor != 0:
#                 cursor -= 1
#         elif c[0] == 'D':
#             if cursor < len(word): # 커서가 맨 뒤가 아니면
#                 cursor += 1
#         else: # B일때
#             if cursor > 0: # 커서가 맨 앞이 아니면
#                 word = word[0:cursor] + word[cursor+1:]
#                 cursor -= 1
#     return word,cursor

# word = list(input())
# cursor = len(word)
# M = int(input())
# for _ in range(M):
#     command = input()
#     word, cursor = order(word,command,cursor)
# print(''.join(word))

from sys import stdin

left = list(input())
right = []

for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))