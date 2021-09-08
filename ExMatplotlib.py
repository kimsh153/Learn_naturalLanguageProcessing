import matplotlib.pyplot as plt

# 라인 플롯 그리기
# plot()은 라인 플롯을 그리는 기능을 수행합니다. plot() X축과 Y축의 값을 기재하고
# 그림을 표시하는 show()를 통해서 시각화 합니다.
plt.title('test')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.show()

# 축 레이블 삽입하기
# x축과 y축 각각에 축이름을 삽입하고 싶다면 xlabel('넣고 싶은 축이름')과
# ylabel('넣고 싶은 축이름')을 사용하면 됩니다.
plt.title('test')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.xlabel('hours')
plt.ylabel('score')
plt.show()

# 라인 추가와 범례 삽입하기
# 하나의 plot()뿐만 아니라 여러개의 plot()을 사용하여 하나의 그래프를 나타낼 수 있습니다.
# 여러개의 라인 플롯을 동시에 사용할 경우에는 각 선이 어떤 데이터 인지를 보여주는 범례(legend)를 사용합니다.
plt.title('students')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.plot([1.5, 2.5, 3.5, 4.5], [3, 5, 8, 10])  # 라인 새로 추가
plt.xlabel('hours')
plt.ylabel('score')
plt.legend(['A student', 'B student'])  # 범례 삽입
plt.show()
