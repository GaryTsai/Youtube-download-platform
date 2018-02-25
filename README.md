
# Youtube-download-platform  
============================  
*這是一個簡單的音樂下載平台，可註冊帳號  
*功能(我的最愛、下載MP3、MP4)  
*後端採用mongoDB作為資料庫  

1.由於上傳時的static呈現有誤
static包含有資料夾css、js、img三個，並且css有檔案style.css  
2.需要新增原本有的media資料夾，避免下載檔案下載時的路徑不存在  
3.尚需更正Youtube的下載API，並使之運行。
  

### 安裝後端資料庫，於MongoDB 官網 https://www.mongodb.com/download-center?jmp=nav#atlas 下載 
## 安裝
(1) 與同在mongoDB路徑下，新增data資料夾  
(2) 使用cmd cd路徑到D:MongoDB/bin所在路徑下，輸入mongod.exe，進行連結。  
(3) 打開MogDB主程式，mongo.exe  
(4) show dbs，可看到底下的collection  

## 新增資料庫(範例插入資料與刪除)  
> show dbs  
> use test  //新增資料庫test  
> db.student.insert({"Name":"gary","Age":"25","Height":"170"})    
> db .student.find.pretty()  //呈現資訊  
> db.student.remove({"Name":"gary"}) //刪除指定資料  
> show collection //目前的資料庫  
> db.student.drop() //刪除資料表  
> db.drop //刪除資料庫   
   
  
> 建立User資料表於後面會說明

### python-flask專案  

## 檔案run.py，內容如下:  #
<code>  
  `from flask import Flask   
app = Flask(__name__)  

@app.route("/")  
def hello(): 
    return "Hello World!" 
`  
 </code>
##  各個資料夾
1.新增template、static(css、js、img)、modles、function，common資料夾  
templates 放置網頁模板  
static   放置網頁渲染文件(css、js、img)  
function 放置各個網站功能(使用request抓取資料的小功能，於實作中創作，並不會使用)  
modles   放置之後的模組   
common   放置資料庫設定  

**需再加入建立python-flask過程與各個檔案說明** 

#git init  
#git add README.md  
#git add .  
#git commit -m "version statement"  
#git remote add origin url($ git remote add origin git@github.com:GaryTsai/Youtube-download-platform.git)  
#git push -u origin master
