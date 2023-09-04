import time
import threading

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing,args=("我要唱歌hhh",))
    dance_thread = threading.Thread(target=dance,kwargs={"msg":"我要跳舞lll"})

    sing_thread.start()
    dance_thread.start()