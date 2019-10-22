#키보드로부터 값을 다음과 같은 형태(양의정수)로 받는다...5,3,8,2,10,
#입력받은 문자열을 리스트로 변환하여 함수의 인자값으로 받아 다음 함수를 구현한다.
#getTotal(data) : 결과값 리턴
#getMean(data) : 평균 -> 결과값 리턴
#getMax(data): 최대값 리턴
#getMin(data) : 최소값 리턴
#getTwoSum(num1,num2): 입력된 두개의 값 포함 두값 사이의 숫자의 합을 구하는 함수


def getTotal(data):
    total=0
    for i in data:
        total+=i
    return total
def getMean(data):
    avg=getTotal(data)/len(data)
    return avg
def getMax(data):
    max=0
    for i in data:
        if max<i:
            max=i
    return max
def getMin(data):
    min=1000
    for i in data:
        if min>i:
            min=i
    return min
def getTwoSum(num1,num2):
    if num1>num2:
        num1,num2=num2,num1
    total=0
    for i in range(num1,num2+1):
        total+=i
    return total
print("__name__" + __name__)
