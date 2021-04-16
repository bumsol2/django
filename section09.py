# Section 09
# 파일 읽기, 쓰기
# 읽기 모드 :r , 쓰기 모드(기존 파일 삭제) : w, 추가모드(파일 생성 또는 추가) : a
# .. : 상대 경로, . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()

print("--------------------------------------------")
print("--------------------------------------------")

# 예제2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print("--------------------------------------------")
print("--------------------------------------------")


# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print("--------------------------------------------")
print("--------------------------------------------")

# 예제 4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()  # 내용 없음
    print(">", content)

print("--------------------------------------------")
print("--------------------------------------------")

# 예제 5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end='##### ')
        line = f.readline()
