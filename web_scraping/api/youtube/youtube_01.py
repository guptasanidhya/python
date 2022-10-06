from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
"""
Scrape, Analyze & Visualize Video Detail
"""
#api key from google developers console
apikey='################################'

#channel ids of different youtubers
# channel_id='UCnz-ZXXER4jOvuED5trXfEA'
channel_Ids=['UCnz-ZXXER4jOvuED5trXfEA', # techTFQ,
            'UCLLw7jmFsvfIVaUFsLs8mlQ', # Luke Barousse ,
            'UCiT9RITQ9PW6BhXK0y2jaeg', # Ken Jee,
            'UC7cs8q-gJRlGwj4A8OmCmXg', # Alex the analyst,S
            'UC2UXDak6o7rBm23k3Vv5dww',# Tina Huang
            'UCeVMnSShP_Iviwkknt83cww'] #code with harry

#buliding the http client
youtube=build('youtube','v3',developerKey=apikey)

##Function to get channel statistics
all_data=[]
def get_channel_stats(youtube,channel_Ids):
    request=youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=','.join(channel_Ids))
    response=request.execute()
    print(response)
    for i in range(len(response['items'])):
        data=dict(Channel_name=response['items'][i]['snippet']['title'],
                  subscribers=response['items'][i]['statistics']['subscriberCount'],
                  Views=response['items'][i]['statistics']['viewCount'],
                  Total_videos=response['items'][i]['statistics']['videoCount'],
                  playlist_id=response['items'][i]['contentDetails']['relatedPlaylists']['uploads'],
                  channel_id=response['items'][i]['id']
                  )
        all_data.append(data)
        # print(data)
    # print(all_data)
    return all_data

#storing the return value in channel statistics
channel_statistics=get_channel_stats(youtube,channel_Ids)

#creating the dataframe
channel_data=pd.DataFrame(channel_statistics)
print(channel_data)
# print(channel_data.dtypes)

#replacing object type to integer type
channel_data['subscribers']=pd.to_numeric(channel_data['subscribers'])
channel_data['Views']=pd.to_numeric(channel_data['Views'])
channel_data['Total_videos']=pd.to_numeric(channel_data['Total_videos'])
# print(channel_data.dtypes)

"""Visualizing the bar plots"""
# subs=sns.barplot(x='Channel_name',y='subscribers',data=channel_data)
# view=sns.barplot(x='Channel_name',y='Views',data=channel_data)
# vc=sns.barplot(x='Channel_name',y='Total_videos',data=channel_data)
# plt.show()

"""Getting the playlist details"""
playlist_id = channel_data.loc[channel_data['Channel_name']=='Ken Jee', 'playlist_id'].iloc[0]
print(playlist_id)
#function for getting video ids of a particular channel
def get_video_ids(youtube,playlist_id):
    request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId = playlist_id,
                maxResults = 50
    )

    response=request.execute()
    
    """A page can show a maximum of 50 results in one go so developing a logic to catch all the video ids using 
    page token . If  next page have new video ids then there will be a new page token on the parent page"""
    video_ids=[]
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])

    next_page_token=response.get('nextPageToken')#using the get method so program does not get crashed at it returns none in case of null values
    more_pages=True

    while more_pages:
        if next_page_token is None:
            more_pages=False
        else:
            request=youtube.playlistItems().list(

                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
    
            response=request.execute()

            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])

            next_page_token=response.get('nextPageToken')

    return (video_ids)

#storing the return value in videoIDs
video_IDs=get_video_ids(youtube,playlist_id)
# print(video_IDs)

"""Getting personal video details like,comments,views, etc"""
def get_video_details(youtube,video_IDs):
    all_video_stats=[]

    for i in range(0,len(video_IDs),50):
        request=youtube.videos().list(
            part='snippet,statistics',
            id=','.join(video_IDs[i:i+50])
        )

        response=request.execute()


        for video in response['items']:
            video_stats=dict(
                Title=video['snippet']['title'],
                Published_date = video['snippet']['publishedAt'],
                Views = video['statistics']['viewCount'],
                Likes = video['statistics']['likeCount'],
                Comments = video['statistics']['commentCount']
            )
            all_video_stats.append(video_stats)

    return (all_video_stats)

video_details=get_video_details(youtube,video_IDs)
# print(video_details)
video_data=pd.DataFrame(video_details)
video_data['Published_date']=pd.to_datetime(video_data['Published_date']).dt.date
video_data['Views']=pd.to_numeric(video_data['Views'])
video_data['Likes']=pd.to_numeric(video_data['Likes'])
video_data['Comments']=pd.to_numeric(video_data['Comments'])
# print(video_data.dtypes)
# print(video_data)



top10_videos=video_data.sort_values(by="Views",ascending=False).head(10)
# print(top10_videos)
# top10=sns.barplot(x='Views',y='Title',data=top10_videos)
# plt.show()




"""
In which months it posted more videos
"""

video_data['Month']=pd.to_datetime(video_data['Published_date']).dt.strftime('%b')
# print(video_data)

videos_per_month=video_data.groupby('Month',as_index=False).size()
# print(videos_per_month)

sort_order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
videos_per_month.index=pd.CategoricalIndex(videos_per_month['Month'],categories=sort_order,ordered=True)
# print(videos_per_month.sort_index())

videos_per_month_visual=sns.barplot(x='Month',y='size',data=videos_per_month)
# plt.show()

"""getting playlist lists using channel id"""
playlist_details=[]
def get_playlist_details(youtube):
    request=youtube.playlists().list(
        part='snippet, contentDetails',
        channelId='UCeVMnSShP_Iviwkknt83cww',
        maxResults=20
    )

    response=request.execute()
    # print(response)
    playlists=[]
    for i in range(len(response['items'])):
       data=dict( playlist_name=response['items'][i]['snippet']['title'],
                video_count=response['items'][i]['contentDetails']['itemCount']
            )
       playlists.append(data)
    next_page_token=response.get('nextPageToken')
    more_pages=True
    while more_pages:
        if next_page_token is None:
            more_pages=False

        else:
            request = youtube.playlists().list(
                part='snippet, contentDetails',
                channelId='UCeVMnSShP_Iviwkknt83cww',
                maxResults=20,
                pageToken=next_page_token
            )

            response=request.execute()

            for i in range(len(response['items'])):
                data = dict(playlist_name=response['items'][i]['snippet']['title'],
                            video_count=response['items'][i]['contentDetails']['itemCount']
                            )
                playlists.append(data)

            next_page_token = response.get('nextPageToken')
    return playlists
playlist_data=get_playlist_details(youtube)
# print(playlist_data)

playlist_df=pd.DataFrame(playlist_data)
# print(playlist_df)