from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

in_loc = 'output.mp4'
out_loc = 'output_SpeedUp.mp4'

# Import video clip
clip = VideoFileClip(in_loc)
print("fps: {}".format(clip.fps))

# Modify the FPS
clip = clip.set_fps(clip.fps * 2)

# Apply speed up
final = clip.fx(vfx.speedx, 2)
print("fps: {}".format(final.fps))

# Save video clip
final.write_videofile(out_loc)
