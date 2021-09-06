import pandas as pd

# 시리즈
# 시리즈 클래스는 1차원 배열의 값(values)에 각 값에 대응되는 인덱스(index)를 부여할 수 있는 구조를 갖고 있습니다.
sr = pd.Series([17000, 18000, 1000, 5000],
               index=["피자", "치킨", "콜라", "맥주"])
print(sr)
print()
print(sr.values)  # 값 출력
print()
print(sr.index)  # 인덱스 출력
print()

# 데이터프레임(DataFrame)
# 데이터프레임은 2차원 리스트를 매개변수로 전달합니다. 2차원이므로 행방향 인덱스(index)와 열방향(column)이 존재합니다.
# 데이터프레임은 인덱스(index), 값(values), 열(columns)으로 구성됩니다
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)
print(df)
print()
print(df.index)  # 인덱스(행) 출력
print()
print(df.columns)  # 열 출력
print()
print(df.values)  # 값 출력
print()

# 데이터프레임의 생성
# 데이터프레임은 리스트(List), 시리즈(Series), 딕셔너리(dict), Numpy의 ndarrys, 또 다른 데이터프레임으로 생성할 수 있습니다.
# 리스트로 데이터프레임 생성하기
data = [
    ['1000', 'Steve', 90.72],
    ['1001', 'James', 78.09],
    ['1002', 'Doyeon', 98.43],
    ['1003', 'Jane', 64.19],
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]
df = pd.DataFrame(data)
print(df)
print()
# 생성된 데이터프레임에 열(columns)을 지정해줄 수 있습니다.
df = pd.DataFrame(data, columns=['학번', '이름', '점수'])
print(df)
print()

# 딕셔너리로 데이터프레임 생성하기
data = {'학번': ['1000', '1001', '1002', '1003', '1004', '1005'],
        '이름': ['Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
        '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]}

df = pd.DataFrame(data)
print(df)
print()

# 데이터프레임 조회하기
# df.head(n) - 앞 부분을 n개만 보기
# df.tail(n) - 뒷 부분을 n개만 보기
# df['열이름'] - 해당되는 열을 확인

print(df.head(3))
print()
print(df.tail(3))
print()
print(df['학번'])

# 외부 데이터 읽기
# pandas는 CSV, 텍스트,Excel,SQL,HTML,JSON 등 다양한 데이터 파일을 읽고 데이터 프레임을 생성할 수 있습니다.
# csv 파일을 읽을 때는 pandas.read_csv()를 통해 읽을 수 있습니다.
print()
df = pd.read_csv(r'C:\Users\user\Desktop\example.csv')
print(df)
print(df.index)
