# Section12-2
# 파이썬 데이터베이스 연동
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/Django/python/resource/database.db')  # 내 DB 경로

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
c.execute('select * from users where id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())  # 데이터 없음

# where Retrieve2
param2 = 4
c.execute('select * from users where id="%s"' % param2)  # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall())  # 데이터 없음

# where Retrieve3
c.execute('select * from users where id=:Id', {"Id": 5})  # %s, %f, %d
print('param3', c.fetchone())
print('param3', c.fetchall())  # 데이터 없음

# Where Retrieve4
param4 = (3, 5)
c.execute("select * from users where id IN(?,?)", param4)
print('param4', c.fetchall())

# Where Retrieve5
c.execute("select * from users where id IN('%d','%d')" % (3, 4))
print('param5', c.fetchall())

# Where Retrieve6
c.execute("select * from users where id =:id1 OR id=:id2",
          {"id1": 2, "id2": 5})
print('param5', c.fetchall())

# Dump 출력
with conn:
    with open('C:/Django/python/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

# f.close(), conn.close()
