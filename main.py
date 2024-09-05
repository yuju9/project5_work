from plus import add
from subtration import sub

ipt1 = float(input("첫 번째 숫자 입력: "))
ipt2 = float(input("두 번째 숫자 입력: "))
print("\n")
print("------------------파이썬 계산기------------------")
print("다음 중 하나를 선택하세요.")
print("1. 덧셈")
print("2. 뺄셈")

opt = input("")
result = 0

if opt == '1':
    result = add(ipt1, ipt2)
elif opt == '2':
    result = sub(ipt1, ipt2)
else:
    print("잘못된 입력입니다.")
    exit()

print("결과: ", result)
