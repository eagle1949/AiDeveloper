import os
import openai

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("请设置环境变量 OPENAI_API_KEY")
        return
    openai.api_key = api_key
    audio_file = open("sample_audio.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print("转录结果：")
    print(transcript.text)

if __name__ == "__main__":
    main()
