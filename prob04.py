# 문제4
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.


for num in range(1,100):
    numStr = str(num)
    count = numStr.count('3')+numStr.count('6')+numStr.count('9')
    if count != 0:
            print(numStr ,'짝'*count)