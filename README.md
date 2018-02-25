
# Youtube-download-platform  
* 這是一個簡單的音樂下載平台，可註冊帳號  
* 功能(我的最愛、下載MP3、MP4)  
* 後端採用mongoDB作為資料庫

1.由於上傳時的static呈現有誤
static包含有資料夾css、js、img三個，並且css有檔案style.css  
2.需要新增原本有的media資料夾，避免下載檔案下載時的路徑不存在  
3.尚需更正Youtube的下載API，並使之運行。
## 使用mongoDB作為資料庫  

1.於官網下載檔案並安裝(https://www.mongodb.com/download-center?jmp=nav)   
2.在與mongoDB同一路徑下新增一個data資料夾  

## 建立<b>Python-flask</b>專案
1.首先創建一個<b>init.py</b>檔案，內容如下:  
<code>from flask import Flask   
app = Flask(__name__)  

@app.route("/")  
def hello():  
     return "Hello World!"  
if __name__ == "__main__"  
    app.run()  

</code> 

2.可執行並成功第一個網頁回傳Hello World!  

## 需再加入建立python-flask過程與各個檔案說明** 

#git init  
#git add README.md  
#git add .  
#git commit -m "version statement"  
#git remote add origin url($ git remote add origin git@github.com:GaryTsai/Youtube-download-platform.git)  
#git push -u origin master
