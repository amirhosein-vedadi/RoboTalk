from tts.tts import Text2Speech
from llm.llm import LLM

if __name__ == "__main__":
    llm = LLM()
    tts = Text2Speech()
    while True:
        user_input = input("what is your question? (q for exit): ")
        if user_input=="q":
            break
        response = llm.talk(user_input)
        tts.convert_text_to_speech(response)
        tts.play_audio("output.wav")
