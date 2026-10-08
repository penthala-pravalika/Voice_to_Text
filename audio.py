from gtts import gTTS

text = """
Education is one of the most important parts of our life.
It gives us knowledge, develops our skills, and helps us understand the world around us.

Education teaches us how to think, solve problems, and make better decisions.
It also helps us build confidence and become independent.

For students, education creates opportunities for a better career and a brighter future.
Education is not only about getting good marks. It is about learning new things,
developing our personality, and becoming a better person.

Therefore, education is a powerful tool that can transform individuals, families, and society.
Everyone should have the opportunity to receive quality education.
"""

tts = gTTS(text=text, lang="en")
tts.save("importance_of_education.mp3")

print("Audio created successfully!")