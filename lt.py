import streamlit as st
from translate import Translator

# Streamlit app
def main():
    st.title("Language Translator")
    input_text = st.text_area("Enter a sentence:", "Text here...")
    source_lang = st.selectbox("Select Source Language:", ["auto", "en", "de"])
    target_lang = st.selectbox("Select Target Language:", ["en", "de"])
    if st.button("Translate"):
        translation = translate(input_text, source_lang, target_lang)
        st.write(f"Translated Text ({target_lang}):", translation)

def translate(input_text, source_lang, target_lang):
    try:
        translator = Translator(to_lang=target_lang, from_lang=source_lang)
        translation = translator.translate(input_text)
        return translation
    except Exception as e:
        return f"Translation Error: {str(e)}"

if __name__ == "__main__":
    main()
