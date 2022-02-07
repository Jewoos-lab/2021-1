# deque는 파이썬 collection 모듈에서 가지고 온다.
from collections import deque

queue = deque()

# 큐 맨끝에 데이터 삽입
queue.append("태호")
queue.append("현승")
queue.append("지웅")
queue.append("동욱")
queue.append("신의")

print(queue)

# 큐 맨앞 데이터 접근
print(queue[0])

# 큐 맨앞 데이터 삭제
print(queue.popleft())
print(queue)


"""이처럼 큐는 데이터간 순서 관계를 유지할 수 있다."""