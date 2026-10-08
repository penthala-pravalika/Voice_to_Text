# 🎙️ Voice to Text – Speech Recognition App

A **local Speech-to-Text application** built with **Python, Streamlit, and Faster-Whisper**.
The application converts uploaded audio files or live microphone recordings into text using OpenAI's Whisper model through `faster-whisper`.

It supports **90+ languages**, automatic language detection, translation to English, and subtitle export in `.srt` format.

No API key is required.

---

## ✨ Features

* 🎙️ **Live microphone recording**
* 📁 **Upload audio files**
* 📝 **Speech-to-text transcription**
* 🌍 **Multiple language support**
* 🔍 **Automatic language detection**
* 🇬🇧 **Translate speech to English**
* ⏱️ **Timestamped transcription**
* 🎬 **SRT subtitle generation**
* ⬇️ **Download transcript as `.txt`**
* ⬇️ **Download subtitles as `.srt`**
* 💻 **Runs locally**
* 🔐 **No API key required**
* ⚡ Uses `faster-whisper` for efficient transcription

---

## 🛠️ Technologies Used

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| Python         | Programming language          |
| Streamlit      | Web application interface     |
| Faster-Whisper | Speech recognition            |
| OpenAI Whisper | Speech recognition model      |
| FFmpeg         | Audio processing              |
| tempfile       | Temporary audio file handling |

---

## 🌍 Supported Languages

The application provides options for:

* Auto Detect
* English
* Hindi
* Telugu
* Tamil
* Bengali
* Marathi
* Kannada
* Malayalam
* Gujarati
* Urdu
* French
* Spanish
* German
* Japanese

Whisper itself supports many more languages.

---

## 📂 Project Structure

```text
voice-to-text
```
