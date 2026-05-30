# === Day 2 變數與型別練習 ===

# 題 1：宣告變數
# 建立 name(字串)、age(整數)、height(浮點)、is_student(布林)，並用 print 印出
# 提示：用 f-string，例如 print(f"名字：{name}")

# name = "Oliver"
# age = 25
# height = 1.80
# is_student = True

# print(f"名字:{name}")
# print(f"年齡:{age}")
# print(f"身高:{height}")
# print(f"是否學生:{is_student}")



# 題 2：字串切片
# 給定 s = "Hello, Python!"，印出：
# (a) 前 5 個字元
# (b) 最後 6 個字元
# (c) 反轉整個字串
# s = "Hi, there! Python!"

# print(f"前 5 個字元:{s[:5]}")
# print(f"最後6個字元:{s[-6:]}")
# print(f"反轉整個字串:{s[::-1]}")
# message1 =" GGGG"
# print(message1.lstrip())
# print(message1)
# message2 ='GGG '
# print(f"{message2.rstrip()}{message1}")
# print(message2)
# message3 = "12345"
# print(f"{message3.removeprefix('1')}")
# print(f"{message3.removeprefix('123')}")
# name1 = "oliver" 
# print(f"Hello {name1.title()}, would you like to learn some Python today?")
# print(f"{name1.upper()}")
# print(f"{name1.lower()}")
# famous_name = "Dr.House"
# print('Dr.House says"Everybody lies!"')
# print(f"{famous_name} says'Everybody lies!'")
# famous_name = "\n Dr.House "
# famous_name2 = "eeeee"
# print(f"{famous_name}")
# print(f"去掉前面空白{famous_name.lstrip()}")
# print(f"去掉前面空白{famous_name.lstrip()}{famous_name2}你看中間還有一個空白")
# print(f"{famous_name.rstrip()}")
# print(f"去掉後面空白{famous_name.rstrip()}{famous_name2}")
# filename = "python_notes.txt"
# print(f"{filename}")
# print(f"去掉副檔名{filename.removesuffix(".txt")}")
# print(f"去掉副檔名{filename.removeprefix(".txt")}")
# print(f"\t{message}\n\t{message}")

# 題 3：字串方法
# 給定 text = "  Learning Python is Fun  "
# (a) 去掉前後空白
# (b) 全轉小寫
# (c) 把 "Fun" 換成 "Awesome"
# (d) 用空白切成 list
# text ="  Learning Python is Fun  "
# print(f"去掉前後空白={text.strip()}")
# print(f"全轉小寫={text.lower().strip()}")
# print(f"把'Fun'換成'Awesome'={text.replace("Fun", "Aswome")}")
# print(f"用空白切成 list={text.split()}")



# 題 4：數字運算
# 計算 2 的 10 次方、17 除以 5 的商與餘數、圓周率 * 半徑平方（半徑=7）
# print(2 ** 10)
# print(17 // 5)
# print(17 % 5)
int1 = 3 + 2
int2 = 3 * 2
int3 = 3 / 2
print(f"3+2={int1}\n3X2={int2}\n3/2={int3}") 
# 題 5：型別轉換
# 使用者輸入一個數字字串，轉成 int 後加 100 再印出
# num_str = input("請輸入數字：")


# 題 6：type() 練習
# 對以下 5 個值用 type() 檢查型別並印出
# values = [42, 3.14, "hello", True, None]


# 題 7：布林運算
# 判斷一個數字是否在 1~100 之間（包含）


# 題 8：字串格式化比較
# 同樣一句「我叫 XX，今年 YY 歲」用三種方式印出：
# (a) + 號串接  (b) .format()  (c) f-string


# 題 9：轉型陷阱
# 執行 int("3.14") 會發生什麼？改成什麼才會成功？把答案寫成註解


# 題 10：綜合題
# 寫一個小程式：詢問使用者的名字與出生年，計算並印出：
# 「你好 XXX，你今年 YY 歲」（用 datetime 取得今年年份）