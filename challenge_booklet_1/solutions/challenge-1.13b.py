import random, time

endTime = time.time() + 30
while time.time() <= endTime:
    print(random.randint(1,100))
    time.sleep(3)
    
