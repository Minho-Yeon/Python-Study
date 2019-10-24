
class NotCorrectInput(Exception):
    def __init__(self,message):
        self.message=message
def checkValue():
    data = {'a':'alpha',"b":'bravo',"c":'charlie'}
    input_str = input("체크할 문자 값을 입력해주세요.(Ex: a,b,c) : ")
    
    print(data[input_str])
#         raise NotCorrectInput('받아 들일 수 없는 문자 %s가 입력되었습니다.\n'%input_str)

def checkNum():
    input_num = int(input("양의 정수를 입력해주세요.(Ex: 10, 25) : "))
    if input_num<0:
       raise NotCorrectInput("음의 정수를 입력하지 마세요.")
    print("{:.3f}\n".format(1/input_num))

if __name__=='__main__':
    checkNum()
