def getMyscore(data):
    total=0
    for grade in data:
        if grade[0]=='A':
            total+=4
        elif grade[0]=='B':
            total+=3
        elif grade[0]=='C':
            total+=2.5
        elif grade[0]=='D':
            total+=2.0
        else:
            print("제대로 된 성적이 아닙니다. 다시 입력해주세요")
            return None;
        if '-' in grade:
            total-=0.25
        elif '+' in grade:
            total+=0.25
    avg=total/len(data)
    return avg
def checkPopulation(year,chinaPop=1.37,indiaPop=1.26,chinaRate=1.0051,indiaRate=1.0135):
    add_year=year+1
    while True:
        chinaPop*=chinaRate
        indiaPop*=indiaRate
        if chinaPop<indiaPop:
            break
        add_year+=1
    
    print("중국 인구 %2f, 인도인구 %2f %d년도에 인도 인구가 더 많습니다" %(chinaPop,indiaPop,add_year))
