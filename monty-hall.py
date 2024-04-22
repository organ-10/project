import random

stay = 0
change = 0

tri = int(input("시행 횟수를 입력해 주세요: "))

for i in range(tri):
    doors = [0, 0, 1]
    random.shuffle(doors)
    user_choice = doors.pop()
    doors.remove(0)
    if user_choice == 1:
        stay+=1
    else:
        change+=1

print(f"stay: {(stay/tri) * 100}%, change: {(change/tri) * 100}%")