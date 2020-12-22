import pytube
from moviepy.editor import VideoFileClip, concatenate_videoclips
# We can add more links in below array which we want to get it concatinated
link=["https://www.youtube.com/watch?v=COJroHpBjl4&feature=youtu.be&ab_channel=PulkitMidha","https://www.youtube.com/watch?v=ZyeY5rqCRz4&feature=youtu.be&ab_channel=PulkitMidha"]
for i in link:
  yt = pytube.YouTube(i)
  stream = yt.streams.first()
  stream.download()
clip_1 = VideoFileClip("dhcv.mp4")
clip_2 = VideoFileClip("DHCV2.mp4")
final_clip = concatenate_videoclips([clip_1,clip_2])
final_clip.write_videofile("final.mp4")



