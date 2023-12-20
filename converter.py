import os
from gtts import gTTS
from openai import OpenAI
from pydub import AudioSegment
from pydub.effects import speedup

files_path = "pages/audio/"

def getTopics():
  topics_file = open('topics.txt', 'r')
  return topics_file.readlines()

def convertTextToSpeech(title, text):
  language = 'pt-br'
  speech = gTTS(text, lang=language, slow=False)
  speech.save(files_path+title+".mp3")

def generateText(topic):
  client = OpenAI()
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Você ´é um professor de pós-graduação brasileiro dando uma aula abrangente sobre "+topic+""},
      {"role": "user", "content": "Explique os principais conceitos e aspectos desse assunto e de assuntos corretatos."}
  ]
  )
  return completion.choices[0].message.content

def speedupAudio(audio_file):
  audio = AudioSegment.from_file(files_path+audio_file+".mp3", format="mp3")
  audio = AudioSegment.from_mp3(files_path+audio_file+".mp3")
  fast_audio = speedup(audio, 1.5, 150)
  fast_audio.export(files_path+audio_file+"_fast.mp3", format="mp3")

def main():
  for topic in getTopics():
    topic = topic.strip()
    if topic:
      print("Generating "+topic+"...")  
      text = generateText(topic)
      convertTextToSpeech(topic, text)
      speedupAudio(topic)
    
main()
