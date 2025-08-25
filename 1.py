from gtts import gTTS

# Lista de tons
words = {
    "ma1_mā": "妈 mā",   # mãe
    "ma2_má": "麻 má",   # cânhamo
    "ma3_mǎ": "马 mǎ",   # cavalo
    "ma4_mà": "骂 mà",   # xingar
    "ma_neutral": "吗 ma" # partícula de pergunta
}

for name, text in words.items():
    tts = gTTS(text=text, lang='zh-cn')
    tts.save(f"{name}.mp3")

print("Arquivos de áudio salvos!")
