import time
initial=time.time()
print("initial Time",initial)
k=0
while k<20:
    print("i am sandy")
    time.sleep(2)
    k+=1
print(f"while loop {time.time()-initial} time")
initial2=time.time()
for i in range(20):
    print("this is Sandy")
print(f"for loop {time.time()-initial2} time")
print(time.time()-initial2)



