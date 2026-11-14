x = int(input("輸入年齡:"))
y = input("是否有票? ").upper()
if x >= 18 and y == "Y":
    print("可進入")
else:
    print("不可進入")