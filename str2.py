import sys
import time
import threading
from deep_translator import GoogleTranslator

# ---------------------- Banner ----------------------
def print_banner():
    print(r"""
 _                       _       _   _                   _        
| |_ _ __ __ _ _ __  ___| | __ _| |_(_) ___  _ __    ___| |_ _ __ 
| __| '__/ _` | '_ \/ __| |/ _` | __| |/ _ \| '_ \  / __| __| '__|
| |_| | | (_| | | | \__ \ | (_| | |_| | (_) | | | | \__ \ |_| |   
 \__|_|  \__,_|_| |_|___/_|\__,_|\__|_|\___/|_| |_| |___/\__|_|    
""")

# ---------------------- Spinner Animation ----------------------
done_loading = False

def spinner():
    while not done_loading:
        for ch in "|/-\\":
            print(f"\r🔁 Loading... {ch}", end="", flush=True)
            time.sleep(0.1)

# ---------------------- Help Menu ----------------------
def print_help():
    print("""
Usage:
  python3 str2.py -f <input.srt> -t <language>
  python3 str2.py -f <input.srt> -translation <language>

Example:
  python3 str2.py -f movie.srt -t greek
  python3 str2.py -f /home/user/movie.srt -translation greek

Options:
  -f              Input subtitle (.srt) file
  -t              Target language (Greek, French, etc.)
  -translation    Same as -t, alternative option
  -help           Show this help message
""")

# ---------------------- Translate Function ----------------------
def translate_srt(input_file, target_lang):
    global done_loading
    output_file = f"{input_file.rsplit('.', 1)[0]}_{target_lang}.srt"
    translator = GoogleTranslator(source='auto', target=target_lang)

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Count how many subtitle blocks exist
    total_blocks = sum(1 for line in lines if line.strip().isdigit())
    translated_lines = []
    buffer = []
    block_counter = 0

    # Start spinner in background
    spin_thread = threading.Thread(target=spinner)
    spin_thread.start()

    for line in lines:
        if line.strip().isdigit() or "-->" in line or line.strip() == "":
            if buffer:
                text_to_translate = ' '.join(buffer)
                try:
                    translated = translator.translate(text_to_translate)
                except Exception as e:
                    print(f"\n⚠️ Error translating: {e}")
                    translated = text_to_translate
                translated_lines.extend([translated + '\n'])
                buffer = []
                block_counter += 1

                # Show percent progress
                percent = (block_counter / total_blocks) * 100
                print(f"\r✅ Translated blocks: {block_counter}/{total_blocks} ({percent:.1f}%)", end="", flush=True)

            translated_lines.append(line)
        else:
            buffer.append(line.strip())

    if buffer:
        text_to_translate = ' '.join(buffer)
        try:
            translated = translator.translate(text_to_translate)
        except Exception as e:
            print(f"\n⚠️ Error translating: {e}")
            translated = text_to_translate
        translated_lines.extend([translated + '\n'])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(translated_lines)

    # Stop spinner
    done_loading = True
    spin_thread.join()

    print(f"\n✅ Translation complete! File saved as: {output_file}")

# ---------------------- Main Program ----------------------
if __name__ == "__main__":
    print_banner()

    if "-help" in sys.argv or "--help" in sys.argv or len(sys.argv) < 4:
        print_help()
        sys.exit(0)

    try:
        file_index = sys.argv.index("-f") + 1
        input_file = sys.argv[file_index]
    except (ValueError, IndexError):
        print("❌ Missing or invalid -f argument")
        print_help()
        sys.exit(1)

    try:
        if "-t" in sys.argv:
            lang_index = sys.argv.index("-t") + 1
        elif "-translation" in sys.argv:
            lang_index = sys.argv.index("-translation") + 1
        else:
            raise ValueError
        target_lang = sys.argv[lang_index].lower()
    except (ValueError, IndexError):
        print("❌ Missing or invalid -t / -translation argument")
        print_help()
        sys.exit(1)

    translate_srt(input_file, target_lang)
