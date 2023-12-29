from pytube import YouTube
import os

HOME_DIR = os.environ['HOME']
DESTINY = os.path.join(HOME_DIR, 'Audio')

def process_link_audio(link: str):
    video = YouTube(link)
    audio_stream = video.streams.filter(only_audio=True).first()

    if not os.path.exists(DESTINY):
        os.makedirs(DESTINY)
    
    out_file = audio_stream.download(output_path=DESTINY)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

if __name__ == "__main__":
    test = input("Ingresa el link: ")
    process_link(test)
