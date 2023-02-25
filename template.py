# 수행 시간 측정 소스코드 

import time 

start_time = time.time() # 측정 시작

# 프로그램 소스코드 

end_time = time.time() # 측정 종료 

print("time :", end_time - start_time) # 수행 시간 출력


# 
f = open('./input.txt', 'r')
for line in f:
    print(line, end='')