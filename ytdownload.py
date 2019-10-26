from pytube import YouTube
link=input("Enter the video link")

yt=YouTube(link)

videos=yt.streams.all()

i=0

for stream in videos:
    print(str(i)+"::"+str(stream))
    i+=1

vidno=int(input("Enter the vid no"))

vid=videos[vidno-1]
print("Downloading....")
vid.download("F:\\")
print("Download Completed...")