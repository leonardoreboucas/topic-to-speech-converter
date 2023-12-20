# topic-to-speech-converter
Topics to Speech Converter

### Requirements
apt-get install ffmpeg libavcodec-extra
pip install -r requirements.txt

export OPENAI_API_KEY={KEY obtained from OpenAI}

### How to run
- Update topics.txt
- Execute: `python3 converter.py`
- Execute: `docker compose up -d`
- Open: http://localhost:8080
