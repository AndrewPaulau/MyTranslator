from deep_translator import GoogleTranslator

# Перевод текста с английского на русский
translated = GoogleTranslator(source='en', target='ru').translate("Hello, how are you?")

print(f"Перевод: {translated}")

