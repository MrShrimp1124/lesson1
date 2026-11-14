user = input("輸入用戶:")
num = input("輸入密碼:")
if user == "admin" and num == "123456":
    print("登入成功")
elif user == "admin":
    print("登入失敗，密碼不符")
else:
    print("帳號不存在")