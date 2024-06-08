from deep_translator import GoogleTranslator


def translate(text, lang):
    try:
        return GoogleTranslator(source='auto', target=lang).translate(text)
    except Exception as e:
        print("Translation error:", e)
        return text
