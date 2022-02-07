"""스택은 기본적으로 맨위(즉, 가장뒤)에서 추가되고 맨위(즉, 가장뒤)에서 삭제된다."""

from collections import deque

stack = deque()

stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

print(stack)

# 맨 끝 데이터 접근
print(stack[-1])

# 맨 끝 데이터 삭제
print(stack.pop())

print(stack)