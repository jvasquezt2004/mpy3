from pytube import YouTube
import os

HOME_DIR = os.environ['HOME']
DESTINY_AUDIO = os.path.join(HOME_DIR, 'Audio')
DESTINY_VIDEO = os.path.join(HOME_DIR, 'Video')

def process_link_audio(link: str):
    audio = YouTube(link)
    audio_stream = audio.streams.filter(only_audio=True).first()

    if not os.path.exists(DESTINY_AUDIO):
        os.makedirs(DESTINY_AUDIO)
    
    out_file = audio_stream.download(output_path=DESTINY_AUDIO)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

def process_link_video(link: str):
    video = YouTube(link)
    if not os.path.exists(DESTINY_VIDEO):
        os.makedirs(DESTINY_VIDEO)

    video_stream = video.streams.get_highest_resolution()
    out_file = video_stream.download(output_path=DESTINY_VIDEO)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)

if __name__ == "__main__":
    test = input("Ingresa el link: ")
    process_link_video(test)
