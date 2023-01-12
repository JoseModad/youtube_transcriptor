# Transcribe YouTube video with Whisper and Artificial Intelligence

# Requirements:

    -You need to have Python 3.9 installed and install the dependency for Whisper and PyTube:

    pip install git+https://github.com/openai/whisper.git
    pip install pytube

    -You will also need to have googletranslate installed to translate into Spanish:

    pip install googletrans


    -You also need to have ffmpeg installed in your system:

    # Ubuntu

    sudo apt update && sudo apt install ffmpeg

# How to run the program:

    # you can also indicate the AI ​​model that Whisper will use
    # the bigger, the longer it will take to download it the first time

    python3 transcript.py --video "https://www.youtube.com/watch?v=oHrjAbDanpw" --model "large"


