from flask import Flask, render_template, request
import pycountry
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Get supported language codes from deep_translator
translator = GoogleTranslator(source='auto', target='en')
codes = translator.get_supported_languages()  # list of language codes

def get_language_name(code):
    try:
        # Try 2-letter code first
        lang = pycountry.languages.get(alpha_2=code)
        if not lang:
            # If no 2-letter match, try 3-letter
            lang = pycountry.languages.get(alpha_3=code)
        if lang:
            return lang.name
    except KeyError:
        pass
    return code  # fallback: return code if no full name found

# Create dictionary mapping code to full language name
LANGUAGES = {code: get_language_name(code) for code in codes}

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    original_text = ""
    selected_src = 'auto'
    selected_dest = 'en'

    if request.method == 'POST':
        original_text = request.form['text']
        selected_src = request.form['src_lang']
        selected_dest = request.form['dest_lang']
        translator = GoogleTranslator(source=selected_src, target=selected_dest)
        translated_text = translator.translate(original_text)

    return render_template('index.html',
                           languages=LANGUAGES,
                           translated_text=translated_text,
                           original_text=original_text,
                           selected_src=selected_src,
                           selected_dest=selected_dest)

if __name__ == '__main__':
    app.run(debug=True)
