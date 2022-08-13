# import function
# print(function.add(1,2))

# from function import *
# print(add(1,2))

import function as func
print(func.add(1,2))



print(__name__)

# module에 실행되는 부분이 있으면,
# if __name__ == "__main__"
# 을 해주자.
# 모듈의 __name__ 은 모듈의 이름을 가짐.
# 내가 실행한 곳의 __name__은 __main__을 가짐.

'''
def add(a,b) :
    return a + b


if __name__ == "__main__" :
    print(func(1,2))
    print(add(1,2))
'''