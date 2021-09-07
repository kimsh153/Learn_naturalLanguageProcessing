import numpy as np

# np.array()
# numpy의 핵심은 ndarray입니다 np.array()는 리스트, 튜플,배열로 부터 ndarray를 생성합니다.
# 또한 인덱스가 항상 0으로 시작한다는 특징이 있습니다.

# pycharm이므로 변수이름을 알파벳순으로 하겠습니다.

a = np.array([1, 2, 3, 4, 5])
print(type(a))
print(a)
# np.array() 2차원 배열
b = np.array([[10, 20, 30], [60, 70, 80]])
print(b)
print(b.ndim)  # 차원 출력
print(b.shape)  # 크기 출력
print(a.ndim)  # 차원 출력
print(a.shape)  # 크기 출력

# ndarray 초기화
# 리스트를 가지고 ndarray를 생성했지만, ndarry를 만드는 방법은 다양합니다.
# zeros()는 해당 배열을 모두 0을 삽입하고, ones()는 모두 1을 삽입합니다.
# full()은 배열에 사용자가 지정한 값을 넣는데 사용하고, eye()는 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성합니다.
c = np.zeros((2, 3))
print(c)
d = np.ones((2, 3))
print(d)
e = np.full((2, 2), 7)
print(e)
f = np.eye(3)
print(e)
g = np.random.random((2, 2))
print(g)

# np.arange()
h = np.arange(10)
print(h)
i = np.arange(1, 10, 2)
print(i)

# reshape()
j = np.array(np.arange(30)).reshape((5, 6))
print(j)

# Numpy 슬라이싱
k = np.array([[1, 2, 3], [4, 5, 6]])
L = k[0:2, 0:2]
print(L)
L = k[0, :]  # 첫번째 행 출력
print(L)
L = k[:, 1]  # 두번째 열 출력
print(L)

# Numpy 정수 인덱싱(integer indexing)
m = np.array([[1, 2], [4, 5], [7, 8]])
n = m[[2, 1], [1, 0]]  # a[[row2, row1], [col1, col0]]을 의미함.
print(n)

# Numpy 연산
# Numpy를 사용하면 배열간 연산을 손쉽게 수행할 수 있습니다. +, -, *, /의 연산자를 사용할 수 있으며, 또는 add(), subtract(), mutilply(),
# divide() 함수를 사용할 수도 있습니다.
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = x + y  # 각 요소에 대해서 더함
# z = np.add(x, y)와 동일함
print(z)
z = x - y  # 각 요소에 대해서 빼기
# b = np.subtract(x, y)와 동일함
print(z)
z = z * x  # 각 요소에 대해서 곱셈
# z = np.multiply(z, x)와 동일함
print(z)
z = z / x  # 각 요소에 대해서 나눗셈
# z = np.divide(z, x)와 동일함
print(z)

o = np.array([[1, 2], [3, 4]])
p = np.array([[5, 6], [7, 8]])

q = np.dot(o, p)
print(q)
