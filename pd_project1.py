import pandas as pd 

#讀取資料
data=pd.read_csv('googleplaystore.csv') #把csv格式的檔案讀取成一個DataFrame

#觀察資料
print("資料數量:", data.shape) #先rows再columns
print("資料欄位", data.columns)
print("=======================================================")

#分析資料: Rating column
print("分析資料: Rating column")
condition = data["Rating"]<=5 #回傳Ture、False的Series，>5會是False
data =data[condition] 
print(data["Rating"]) #了解資料型態
print("平均數", data["Rating"].mean())
print("中位數", data["Rating"].median())
print("前一百筆資料平均", data["Rating"].nlargest(1000).mean())
print("=======================================================")

#分析資料: 安裝數量的各種統計數據
data["Installs"]=data["Installs"].str.replace("[,+]", "", regex=True) #因為使用[,x]這種寫法(這是正規表達)，所以後方的regex要是True
data["Installs"]=data["Installs"].str.replace("Free", "", regex=False)
data["Installs"]=pd.to_numeric(data["Installs"])
print("平均數", data["Installs"].mean())
condition = data["Installs"]>100000
print("安裝數量大於100,000的應用程式有多少個", data[condition].shape[0]) #因為shape是一個tuple，包含(row, column)，我們只取row的資料
print("=======================================================")

#基於資料的應用: 關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字: ")
condition = data["App"].str.contains(keyword, case=False) #case=False忽略大小寫
print("包含關鍵字的應用程式列表", data[condition]["App"])
print("包含關鍵字的應用程式數量", data[condition].shape[0])
