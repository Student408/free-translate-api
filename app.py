import streamlit as st
import requests

# Streamlit interface
st.title("Text Translation Interface")

# Input fields
text_to_translate = st.text_area("Enter the text to translate:", "")
target_language = st.selectbox(
    "Select target language:",
    [
        "aa (Afar)", "ab (Abkhazian)", "af (Afrikaans)", "ak (Akan)", "am (Amharic)",
        "an (Aragonese)", "ar (Arabic)", "as (Assamese)", "av (Avar)", "ay (Aymara)", 
        "az (Azerbaijani)", "ba (Bashkir)", "be (Belarusian)", "bg (Bulgarian)", "bh (Bihari)",
        "bi (Bislama)", "bm (Bambara)", "bn (Bengali)", "bo (Tibetan)", "br (Breton)",
        "bs (Bosnian)", "ca (Catalan)", "ce (Chechen)", "ch (Chamorro)", "co (Corsican)",
        "cr (Cree)", "cs (Czech)", "cu (Old Church Slavonic)", "cu (Old Bulgarian)", "cv (Chuvash)",
        "cy (Welsh)", "da (Danish)", "de (German)", "dv (Divehi)", "dz (Dzongkha)",
        "ee (Ewe)", "el (Greek)", "en (English)", "eo (Esperanto)", "es (Spanish)",
        "et (Estonian)", "eu (Basque)", "fa (Persian)", "ff (Peul)", "fi (Finnish)", 
        "fj (Fijian)", "fo (Faroese)", "fr (French)", "fy (West Frisian)", "ga (Irish)", 
        "gd (Scottish Gaelic)", "gl (Galician)", "gn (Guarani)", "gu (Gujarati)", "gv (Manx)",
        "ha (Hausa)", "he (Hebrew)", "hi (Hindi)", "ho (Hiri Motu)", "hr (Croatian)",
        "ht (Haitian)", "hu (Hungarian)", "hy (Armenian)", "hz (Herero)", "ia (Interlingua)",
        "id (Indonesian)", "ie (Interlingue)", "ig (Igbo)", "ii (Sichuan Yi)", "ik (Inupiat)",
        "io (Ido)", "is (Icelandic)", "it (Italian)", "iu (Inuktitut)", "ja (Japanese)",
        "jv (Javanese)", "ka (Georgian)", "kg (Kongo)", "ki (Kikuyu)", "kj (Kuanyama)", 
        "kk (Kazakh)", "kl (Greenlandic)", "km (Cambodian)", "kn (Kannada)", "ko (Korean)", 
        "kr (Kanuri)", "ks (Kashmiri)", "ku (Kurdish)", "kv (Komi)", "kw (Cornish)",
        "ky (Kirghiz)", "la (Latin)", "lb (Luxembourgish)", "lg (Ganda)", "li (Limburgian)",
        "ln (Lingala)", "lo (Laotian)", "lt (Lithuanian)", "lv (Latvian)", "mg (Malagasy)",
        "mh (Marshallese)", "mi (Maori)", "mk (Macedonian)", "ml (Malayalam)", "mn (Mongolian)", 
        "mo (Moldovan)", "mr (Marathi)", "ms (Malay)", "mt (Maltese)", "my (Burmese)",
        "na (Nauruan)", "nd (North Ndebele)", "ne (Nepali)", "ng (Ndonga)", "nl (Dutch)", 
        "nn (Norwegian Nynorsk)", "no (Norwegian)", "nr (South Ndebele)", "nv (Navajo)", 
        "ny (Chichewa)", "oc (Occitan)", "oj (Ojibwa)", "om (Oromo)", "or (Oriya)",
        "os (Ossetian)", "pa (Punjabi)", "pi (Pali)", "pl (Polish)", "ps (Pashto)", 
        "pt (Portuguese)", "qu (Quechua)", "rm (Raeto-Romance)", "rn (Kirundi)", "ro (Romanian)", 
        "ru (Russian)", "rw (Rwandan)", "sa (Sanskrit)", "sc (Sardinian)", "sd (Sindhi)",
        "sg (Sango)", "sh (Serbo-Croatian)", "si (Sinhalese)", "sk (Slovak)", "sl (Slovenian)", 
        "sm (Samoan)", "sn (Shona)", "so (Somali)", "sq (Albanian)", "sr (Serbian)", 
        "ss (Swati)", "st (Southern Sotho)", "su (Sundanese)", "sv (Swedish)", "sw (Swahili)",
        "ta (Tamil)", "te (Telugu)", "tg (Tajik)", "th (Thai)", "ti (Tigrinya)", 
        "tk (Turkmen)", "tl (Tagalog)", "tn (Tswana)", "to (Tonga)", "tr (Turkish)",
        "ts (Tsonga)", "tt (Tatar)", "tw (Twi)", "ty (Tahitian)", "ug (Uyghur)", 
        "uk (Ukrainian)", "ur (Urdu)", "ve (Venda)", "vi (Vietnamese)", "vo (Volapük)", 
        "wa (Walloon)", "wo (Wolof)", "xh (Xhosa)", "yi (Yiddish)", "yo (Yoruba)", 
        "za (Zhuang)", "zh (Chinese)", "zu (Zulu)"
    ],
)

# Extract the language code from the dropdown
if target_language:
    lang_code = target_language.split(" ")[0]

# Translation button
if st.button("Translate"):
    if text_to_translate.strip() == "":
        st.error("Please enter some text to translate.")
    else:
        # API call
        try:
            response = requests.post(
                "http://localhost:8000/translate",
                headers={"Content-Type": "application/json"},
                json={"text": text_to_translate, "to": lang_code},
            )
            # Handle response
            if response.status_code == 200:
                translated_text = response.json().get("translatedText", "No response text found.")
                st.success("Translation successful!")
                st.text_area("Translated Text:", translated_text, height=150)
            else:
                st.error(f"Translation failed. Error code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
