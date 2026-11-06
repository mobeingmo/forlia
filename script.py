import time

n = 1
while True:
    n += 1
    try:
        print("I love you", n, "times <3")
    except OSError:
        time.sleep(0.05)
    time.sleep(0.000001) 
