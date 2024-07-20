from pathlib import Path
from openai import OpenAI
import os

client = OpenAI()

print(os.getenv("OPENAI_API_KEY"))
speech_file_path = Path(__file__).parent / "kannada.mp3"
#response = client.audio.speech.create(
 # model="tts-1",
  #voice="shimmer",
  #input="Hi Anvit.. ninage nanna namaskaaragalu.. ninu tumbaa cute kid.. naanu mattu ninu.. unoo.. adonvaa..ninna akkana hesaru prachi. anvit ninna hosa chikka car chennagide. enjoy maadu."
#)

#response.stream_to_file(speech_file_path)



audio_file= open(speech_file_path, "rb")
translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(translation.text)