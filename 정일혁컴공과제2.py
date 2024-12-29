#(문제) 교재, 게임 아이템 3개 입력받아 딕셔너리 자료형으로 코드를 작성하시오.
items=dict() #빈 딕셔너리
print("+++딕셔너리를 이용해 게임 아이템 입력받기+++")
for i in range(3):
    item=input("게임 아이템 입력하기>>>")
    count=int(input("구매할 개수는 몇 개입니까? "))
    items[item]=count
print("="*50)
result=input("당신이 확인하고 싶은 아이템은 무엇입니까? ")
test=items.get(result)
if result in items:
    print(f'당신이 찾는 {result}은/는 {test}개 있습니다')
else:
    print(f'당신이 찾는 {result}은/는 없습니다. ')