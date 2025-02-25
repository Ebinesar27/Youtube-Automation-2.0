from moviepy import VideoFileClip, TextClip, CompositeVideoClip,AudioFileClip,AudioClip,CompositeAudioClip

class Movie():
    def to_video(self,video,par,voice):
        clip = (
        VideoFileClip(video).subclipped(00,25)
        .with_volume_scaled(0.8)
        )
        clip_a = AudioFileClip(voice)

        # audclip = AudioFileClip(audio)
        # CompositeAudioClip(audclip)
        # video_with_audio = clip.set_audio(audio.subclip(0, video.duration))
        # aud = AudioClip(frame_function=audio,duration = 5)
        # au = AudioFileClip(voice)
        # add = clip.with_audio(au)
        new = CompositeAudioClip([clip_a])
        





# tx = []
# text =  "For God so loved the world that he gave"
# for i in text:
#     # tx.append()
#     print(i.split())



        txt = TextClip(
        font="C:\Windows\Fonts\ALGER.TTF",
        text= par,
    

        font_size=40,
        color="white",
        size=(850,None),
        method='caption'
        ).with_duration(25).with_position('center')

        final = CompositeVideoClip([clip,txt])
        final.audio = new
        final.write_videofile("result1.mp4")
        
# mov = Movie()
# mov.to_video("input.mp4","hello with audio","output.mp3")


