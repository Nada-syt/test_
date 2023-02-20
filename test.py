from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time 

url='https://www.youtube.com/@JohnWatsonRooney/videos'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
time.sleep(5)


#videos = driver.find_elements_by_class_name('style-scope ytd-rich-grid-media')
videos = driver.find_elements(By.CLASS_NAME, "style-scope ytd-rich-grid-media")
print(len(videos))
video_list= []

for video in videos:
    title = video.find_element(By.XPATH, './/*[@id="video-title"]').text
    views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
    time_vid = video.find_element(By.XPATH, './/ytd-thumbnail-overlay-time-status-renderer[@overlay-style="DEFAULT"]/span[1]').text
    when = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
    

    element = driver.find_element(By.XPATH,".//*[@id='thumbnail']/yt-image/img")
    print(element)
    link = element.get_attribute('src')
    

    print("title: ", title, "views: ", views,"when: ", when, "time_vid: ", time_vid,"img: ", link, "\n")

    vid_item={
        'title': title,
        'views': views,
        'posted': when,
        'time_vid': time_vid,
        'img': link
        
    }


    video_list.append(vid_item)

df= pd.DataFrame(video_list)
print(df)
df.to_csv('./data.csv', index=False)





