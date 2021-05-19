# Section12-2
# 파이썬 데이터베이스 연동
# 테이블 조회

import sqlite3

#DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/Django/python/resource/database.db') # 내 DB 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택
# print("Three -> \n", c.fetchmany(size=3))

# 전체 로우 선택
# print('All -> \n', c.fetchall())

print()

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 > ', row) 

# 순회2
# for row in c.fetchall():
#     print('retrieve2 > ', row)

# 순회3
# for row in c.execute('select * from users order by id desc'):
#     print('retrieve3 > ', row)

print()

# where Retrieve1
param1 = (3,)
c.execute('select * from users where id=?',param1)
print('param1',c.fetchone())
print('param1',c.fetchall()) # 데이터 없음

# where Retrieve2


