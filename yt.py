from pytube import YouTube

video_link = input("Enter YouTube link: ")
yt = YouTube(video_link)
print(yt.streams.filter(subtype='mp4'))
# You will get a list of streams available for your video
# Choose your favorable stream by their itag and mention the itag below
itag = int(input('Enter itag: '))
yt.streams.get_by_itag(itag).download('D:\\')
