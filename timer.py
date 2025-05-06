import time  

seconds = int(input("Enter the time in seconds"))

while seconds>0:
    print(f"Time left:{seconds} seconds")
    time.sleep(1)
    seconds-=1
    
print("Time's up")
