#python 이별은 화성 과정 1-1
#파이썬 5조 김동현
#2023/10/20

try:
    f = open("mission_computer_main.log", "r")
except IOError as err:
    print("FileNotFoundError: No such file or directory")
except Exception as e:
    print(f"Unexpected Error occurred:\n{e}")
    # 예측하지 못한 에러를 처리하기 위해 그냥 except를 썻더니 아래와 같이 PEP8 형식에 어긋난다는 메시지를 받음.
    # [Python] PEP 8: E722 do not use bare 'except'
    # except: 는 except:BaseException과 동일한 기능을 한다. 따라서 모든 파이썬 내장 예외 발생을 잡아내게 된다.
    # 여기까지는 의도한 바이지만 문제가 있었다. KeyboardInterrupt가 예외처리될 때 만약 해당 예외처리구간에서 루프를 돌고 있다면 프로그램을 Ctrl+C로 종료할 수 없게 된다.
    # 또한 어떤 종류의 에러든 다 처리하고 넘어가기 때문에 사후에 어떤 종류의 에러가 발생했는지 파악하기 어려워진다는 단점도 있다. 따라서 except 뒤에 예외 종류별로 따로 처리구문을 작성하는것이 좋다.
    # 그럼에도 예외 종류에 관계없이 예외처리를 하고 싶다면 위와 같은 방법으로 예외처리 할 수 있다.
else:
    lines = f.readlines()
    for line in lines:
        print(line[:-1])  # 개행문자를 제외하고 출력
    f.close()


