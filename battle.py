battle1 = [1,2,3,4,5,6,7,8,9]

battle2 = (1,2,3,4,5,6,7,8,9)

battle3 = { '이름' : '진성원',
            '학교' : '보물섬학교'}

for i in battle1:
    print (i, "번째 리스트 친구입니다.")
    
for i in battle2:
    print (i, "번째 튜플 친구입니다.")

for key, value in battle3.items():
    print (key,"는 이거", value, "는 이것인 딕셔너리 친구입니다.")

