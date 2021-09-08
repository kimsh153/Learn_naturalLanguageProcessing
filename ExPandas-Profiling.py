import pandas as pd
import pandas_profiling

# 실습 파일 불러오기
data = pd.read_csv(r'C:\Users\user\Downloads\spam.csv', encoding='latin1')
print(data[:5])

# 리포트 생성하기
pr = data.profile_report()  # 프로파일링 결과 리포트를 pr에 저장
pr.to_file('./pr_report.html')  # pr_report.html 파일로 저장

# 리포트 살펴보기
print(pr)  # pr에 저장했던 리포트 출력
