# 🎬 SRT Translator - Auto Translate Subtitles

**SRT Translator** is a Python script that automatically translates `.srt` subtitle files into any language (e.g., Greek, French, Arabic, etc.) using Google Translate.

---

![image alt](https://github.com/PanagiotisMavro/Subtitle-Translator-str/blob/c14632483980be613ea195f4ffb41d0da71844ba/Screenshot%202025-05-03%2003%3A42%3A46.png)

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

## If Problem for pip? Can help you (Working) Linux

 - sudo apt install python3-venv
 - python3 -m venv ~/myenv
 - source ~/myenv/bin/activate

## 📦 Requirements

```bash
pip install -r requirements.txt
