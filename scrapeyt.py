import scrapetube
import json
import requests

title = str(input("title:"))
#channel=f"https://yt.lemnoslife.com/channels?handle=@{title}"
#channelid = json.loads(str(requests.get(channel).text))
#channel_id=channelid["items"][0]["id"]
        
videos = scrapetube.get_channel(channel_username=title)
x = 0
smr = []
videos_list = list(videos)
for i in range(len(videos_list)-1,-1,-1):
    x+=1
    str1=f"{videos_list[i]['title']['runs'][0]['text']}"
        
    str2="https://www.youtube.com/watch?v="+str(videos_list[i]['videoId'])
           
    smr.append(f"{x}. {str1} : {str2}")
smr2 = '\n\n'.join(smr)
with open(f"{title}.txt", "w", encoding="utf-8") as f:
    f.write(f"{smr2}")
    f.close()