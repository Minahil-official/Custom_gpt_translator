from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
# Initialize model
api_key = os.getenv("groq_api_key")
model = ChatGroq(model="deepseek-r1-distill-llama-70b",api_key= api_key)


# Language dictionary
languages = {
    "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar",
    "Armenian": "hy", "Azerbaijani": "az", "Basque": "eu", "Belarusian": "be",
    "Bengali": "bn", "Bosnian": "bs", "Bulgarian": "bg", "Catalan": "ca",
    "Cebuano": "ceb", "Chinese (Simplified)": "zh-CN", "Chinese (Traditional)": "zh-TW",
    "Corsican": "co", "Croatian": "hr", "Czech": "cs", "Danish": "da",
    "Dutch": "nl", "English": "en", "Esperanto": "eo", "Estonian": "et",
    "Finnish": "fi", "French": "fr", "Frisian": "fy", "Galician": "gl",
    "Georgian": "ka", "German": "de", "Greek": "el", "Gujarati": "gu",
    "Haitian Creole": "ht", "Hausa": "ha", "Hawaiian": "haw", "Hebrew": "he",
    "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu", "Icelandic": "is",
    "Igbo": "ig", "Indonesian": "id", "Irish": "ga", "Italian": "it",
    "Japanese": "ja", "Javanese": "jv", "Kannada": "kn", "Kazakh": "kk",
    "Khmer": "km", "Kinyarwanda": "rw", "Korean": "ko", "Kurdish": "ku",
    "Kyrgyz": "ky", "Lao": "lo", "Latin": "la", "Latvian": "lv",
    "Lithuanian": "lt", "Luxembourgish": "lb", "Macedonian": "mk", "Malagasy": "mg",
    "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Maori": "mi",
    "Marathi": "mr", "Mongolian": "mn", "Myanmar (Burmese)": "my", "Nepali": "ne",
    "Norwegian": "no", "Nyanja (Chichewa)": "ny", "Odia (Oriya)": "or", "Pashto": "ps",
    "Persian": "fa", "Polish": "pl", "Portuguese": "pt", "Punjabi": "pa",
    "Romanian": "ro", "Russian": "ru", "Samoan": "sm", "Scots Gaelic": "gd",
    "Serbian": "sr", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd",
    "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so",
    "Spanish": "es", "Sundanese": "su", "Swahili": "sw", "Swedish": "sv",
    "Tagalog": "tl", "Tajik": "tg", "Tamil": "ta", "Tatar": "tt",
    "Telugu": "te", "Thai": "th", "Turkish": "tr", "Ukrainian": "uk",
    "Urdu": "ur", "Uzbek": "uz", "Vietnamese": "vi", "Welsh": "cy",
    "Xhosa": "xh", "Yiddish": "yi", "Yoruba": "yo", "Zulu": "zu"
}

st.title("🌍 Multi-Language Translator")

# Sidebar for language selection
with st.sidebar:
    st.header("Select Target Language")
    selected_language = st.selectbox("Choose a language:", options=list(languages.keys()), index=list(languages.keys()).index("Urdu"))

# Search bar to filter languages
search_query = st.text_input("Search Language:")

# Filtered languages based on search query
filtered_languages = {lang: code for lang, code in languages.items() if search_query.lower() in lang.lower()}

# Determine which language to use:
# 1. If user searches but doesn't select -> Use first result from search
# 2. If user selects -> Use selected language
if search_query and filtered_languages:
    target_language = next(iter(filtered_languages))  # First search result
else:
    target_language = selected_language  # Use selected language from dropdown

# User input for translation
user_input = st.text_area("Enter text to translate:")

if st.button("Translate"):
    if user_input:
        prompt = f"""Translate the following text into {target_language} ({languages[target_language]}):
        "{user_input}" """

        # Get response from the model
        response = model.invoke(prompt)
        
        # Display result
        st.subheader(f"Translation in {target_language}:")
        st.write(response.content)
    else:
        st.warning("Please enter text to translate.")
