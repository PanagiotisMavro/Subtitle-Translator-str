# 🎬 SRT Translator - Auto Translate Subtitles

**SRT Translator** is a Python script that automatically translates `.srt` subtitle files into any language (e.g., Greek, French, Arabic, etc.) using Google Translate.

---

## 🛠 Features

- ✅ Translate any `.srt` subtitles to another language
- 🔁 Animated loading spinner + progress display
- 🌍 Supports over 100 languages
- 📁 Saves as a new `.srt` file (e.g., `movie_greek.srt`)
- 🖥 Works on Linux, Windows, Mac

---

## 📄 Usage
python3 str2.py -f <file.srt> -t <language>
python3 str2.py -f <file.srt> -translation <language>

---

## 🔍 Examples
python3 str2.py -f movie.srt -t greek
python3 str2.py -f /home/user/video.srt -translation french

---

## 📦 Requirements

```bash
pip install -r requirements.txt
