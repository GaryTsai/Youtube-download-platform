import youtube_dl
import requests
import re
from bs4 import BeautifulSoup
def find_search_content(search):
    request = requests.get('https://www.youtube.com/results?search_query={}'.format(search))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    return soup
def find_page_content(search):
    request = requests.get('https://www.youtube.com/results?{}'.format(search))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    return soup
def find_video(soup, all_item ,i=1):
    for element in soup.find_all('a', {"rel":"spf-prefetch"}):
        video_title = element.get('title')
        video_link = element.get('href')
        img_value = element.get('href').split("=",)[1]
        all_img = soup.find_all('img', {"alt":True,"width":True,"height":True,"onload":True,"data-ytimg":True})
        img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value), str(all_img))).strip("[\"\']")
        video_img=img.replace("&", "&amp;")
        all_item['{}'.format(i)] = {"title":video_title,"link":"https://www.youtube.com/{}".format(video_link),"img":video_img}
        i=i+1
    return all_item
def video_time(soup,all_item,i=1):
    for time in soup.find_all('span',{"class":"video-time"}):
        all_item.get('{}'.format(i))['time'] = time.text
        i=i+1
    return  all_item
def every_video(soup):
    all_item = {}
    find_video(soup,all_item,i=1)
    video_time(soup,all_item,i=1)
    return all_item
def page_bar(soup):
    page = {}
#抓取下一頁連結
    for page_value in soup.find_all('a', {'aria-label':True , "class":True,"data-sessionlink":True ,"data-visibility-tracking":True,"href":True }):
        page['{}'.format(page_value.text)] = page_value.get('href')
    return page
def download_mp3(url):
    ydl_opts ={ 'format': 'bestaudio/best','outtmpl':'/media/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
                }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
def download_mp4(url):
    ydl_opts ={'format': 'best','outtmpl':'/media/%(title)s.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



# import youtube_dl
# #影片下載
# ydl_opts ={'outtmpl':'/media/%(title)s.%(ext)s'}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(["https://www.youtube.com/watch?v=MT2Qng_euzo"])
# import requests
# import re
# from bs4 import BeautifulSoup
# request = requests.get('https://www.youtube.com/results?search_query=pitbull')
# content = request.content
# soup = BeautifulSoup(content, "html.parser")
# page = {}
# #抓取下一頁連結
# for page_value in soup.find_all('a', {'aria-label':True , "class":True,"data-sessionlink":True ,"data-visibility-tracking":True,"href":True }):
#     page['{}'.format(page_value.text)] = page_value.get('href')
# print(page)
# for page_value in soup.find_all('ytd-video-renderer',{"class":True}):
#     print(page_value)
    # print(page_value('href'))

# #影片時間
# for video_time in soup.find_all('span', {"class":"video-time"}):
#     print(video_time.text)
##圖片
# for element in soup.find_all('a', {"rel":"spf-prefetch"}):
#     img_value = element.get('href').split("=",)[1]
#     all_img = soup.find_all('img', {"alt":True,"width":True,"height":True,"onload":True,"data-ytimg":True})
#     img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value), str(all_img))).strip("[\"\']")
#     video_img=img.replace("&", "&amp;")
#     print(img)
    # print(img_value)
    # print(all_img)



# vedio_title=element.get('title')
# vedio_link=element.get('href')
# print(vedio_title)
# print("https://www.youtube.com/{}".format(vedio_link))
