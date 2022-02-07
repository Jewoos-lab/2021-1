"""수강 신청이 완료되었습니다. 이제 각 과목을 수강하는 학생수에 따라 크기가 다른 강의실을 배치하려고 합니다.

강의실은 규모에 따라 “Auditorium”, “Large room”, “Medium room”, “Small room” 총 4가지 종류가 있습니다.

아래 조건에 따라 강의실 종류를 지정해 주세요.

1. 80명 이상의 학생이 수강하는 과목은 “Auditorium”에서 진행됩니다.
2. 40명 이상, 80명 미만의 학생이 수강하는 과목은 “Large room”에서 진행됩니다.
3. 15명 이상, 40명 미만의 학생이 수강하는 과목은 “Medium room”에서 진행됩니다.
4. 5명 이상, 15명 미만의 학생이 수강하는 과목은 “Small room”에서 진행됩니다.
5. 폐강 등의 이유로 status가 “not allowed”인 수강생은 room assignment 또한 “not assigned”가 되어야 합니다."""

import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

# 코드를 작성하세요.
df["room assignment"] = "not assigned"
student_counts = df["course name"].value_counts()

# 첫번째 조건
Auditorium = list(student_counts[student_counts >= 80].index)
for course in Auditorium:
    df.loc[df["course name"] == course, "room assignment"] = "Auditorium"

# 두번째 조건
Large_room = list(student_counts[(40 <= student_counts) & (80 > student_counts)].index)
for course in Large_room:
    df.loc[df["course name"] == course, "room assignment"] = "Large room"

# 세번째 조건
Medium_room = list(student_counts[(15 <= student_counts) & (40 > student_counts)].index)
for course in Medium_room:
    df.loc[df["course name"] == course, "room assignment"] = "Medium room"

# 네번째 조건
Small_room = list(student_counts[(5 <= student_counts) & (15 > student_counts)].index)
for course in Small_room:
    df.loc[df["course name"] == course, "room assignment"] = "Small room"

# 폐강 조건
df.loc[df["status"] == "not allowed", "room assignment"] = "not assigned"

# 정답 출력
df