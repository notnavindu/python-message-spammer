import pyautogui
import time

print("*********************")
print("Starting in 5 seconds")
print("*********************")


for i in range(5, 0, -1):
    time.sleep(1)
    print(str(i) + "... Click on a text box now!  CTRL+C to abort")

with open("bee-short.txt") as bee:
    for line in bee:
        if line.strip():
            line = line.replace("-", "").split(" ")
            for word in line:
                pyautogui.write(word, interval=0.1)
                pyautogui.press('enter')


bee.close()
