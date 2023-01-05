from pytube import YouTube
#YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=a35rNEBNiO4')
print(yt.title)
print(yt.thumbnail_url)


#yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()