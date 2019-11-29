import pyautogui
print(pyautogui.size())
width, height  = pyautogui.size()

print(width)

# pyautogui.moveTo(100,   1400 , duration=5)
# print(pyautogui.position())


pyautogui.click()
distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance , 0 ,duration = 1)
    distance = distance - 25
    print(0 , distance)
    pyautogui.dragRel(0 , distance , duration=1)
    print(-distance,  0)
    pyautogui.dragRel(-distance,0,duration=1)
    distance = distance - 25
    print(0  ,-distance)
    pyautogui.dragRel(0 , -distance,duration = 1)
