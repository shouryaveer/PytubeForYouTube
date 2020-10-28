from pytube import YouTube

url = 'your-youtube-video-url'
video = YouTube(url)

print(video.streams.all())

# You will get a list of streams available for your video
# Choose your favorable stream by their itag and mention the itag below

video.streams.get_by_itag('your-itag').download('your-download-path')
