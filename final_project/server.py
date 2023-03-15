import sys
sys.path.append(r'C:\Users\user\Documents\GitHub\xzceb-flask_eng_fr\machinetranslation')
from translator import english_to_french,french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    new_text=english_to_french(textToTranslate)
    return new_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    new_text=french_to_english(textToTranslate)
    return new_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
