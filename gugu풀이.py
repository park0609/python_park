import sys
args = sys.argv

aa, bb = int(args[1][:-1]), int(args[2])
#슬라이싱으로 2단에서 단을 없앨수있다. args[1]은 2단을 출력 args[1][:-1]는 2단을 2와 단으로 분리하고
# -1 즉 뒤에서 한글자를 빼겠다는 소리 그래서 2가 출력이 된다. 진짜 빡세네


def gugu(a,b):
    for i in range(a,a+b):
        print(f"====={i}단=====")
        for j in range(1,10):
            print(f"{i}x{j}={i*j}")
gugu(2,2)