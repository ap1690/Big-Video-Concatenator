import pytube
from moviepy.editor import VideoFileClip, concatenate_videoclips
# We can add more links in below array which we want to get it concatinated
link=["https://www.youtube.com/watch?v=C","https://www.youtube.com/fdvdfbvs"]
for i in link:
  yt = pytube.YouTube(i)
  stream = yt.streams.first()
  stream.download()
#Put audio=False in VideoFileClip if dont want to process audio
clip_1 = VideoFileClip("video1.mp4")
clip_2 = VideoFileClip("video2.mp4")
final_clip = concatenate_videoclips([clip_1,clip_2])
final_clip.write_videofile("final.mp4")



