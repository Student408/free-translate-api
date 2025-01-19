# Free Translate API

## Description

Free Translate API is a simple and effective service for translating text between multiple languages. It includes a backend built with Go and an interactive frontend using Streamlit.

## Features

- Translate text to over 100 languages.
- Health check endpoint to monitor server status.
- Interactive Streamlit interface for easy use.

## Table of Contents

- [Free Translate API](#free-translate-api)
  - [Description](#description)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Running the API Server](#running-the-api-server)
    - [Using the Streamlit Interface](#using-the-streamlit-interface)
  - [Supported Languages](#supported-languages)
  - [API Endpoints](#api-endpoints)
  - [Testing the API](#testing-the-api)
    - [Translation Endpoint](#translation-endpoint)
    - [Health Check](#health-check)
  - [Contributing](#contributing)
  - [License](#license)

## Getting Started

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/free-translate-api.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd free-translate-api
   ```
3. **Install Go dependencies:**
   ```bash
   go get
   ```
4. **Install Python dependencies:**
   ```bash
   pip install streamlit requests
   ```

## Usage

### Running the API Server

Start the Go server:

```bash
go run main.go
```

The server will start on `http://localhost:8000`.

### Using the Streamlit Interface

Run the Streamlit app:

```bash
python app.py
```

Access the interface at [http://localhost:8501](http://localhost:8501).

## Supported Languages

The API supports the following languages:

- aa (Afar)
- ab (Abkhazian)
- af (Afrikaans)
- ak (Akan)
- am (Amharic)
- an (Aragonese)
- ar (Arabic)
- as (Assamese)
- av (Avar)
- ay (Aymara)
- az (Azerbaijani)
- ba (Bashkir)
- be (Belarusian)
- bg (Bulgarian)
- bh (Bihari)
- bi (Bislama)
- bm (Bambara)
- bn (Bengali)
- bo (Tibetan)
- br (Breton)
- bs (Bosnian)
- ca (Catalan)
- ce (Chechen)
- ch (Chamorro)
- co (Corsican)
- cr (Cree)
- cs (Czech)
- cu (Old Church Slavonic)
- cv (Chuvash)
- cy (Welsh)
- da (Danish)
- de (German)
- dv (Divehi)
- dz (Dzongkha)
- ee (Ewe)
- el (Greek)
- en (English)
- eo (Esperanto)
- es (Spanish)
- et (Estonian)
- eu (Basque)
- fa (Persian)
- ff (Peul)
- fi (Finnish)
- fj (Fijian)
- fo (Faroese)
- fr (French)
- fy (West Frisian)
- ga (Irish)
- gd (Scottish Gaelic)
- gl (Galician)
- gn (Guarani)
- gu (Gujarati)
- gv (Manx)
- ha (Hausa)
- he (Hebrew)
- hi (Hindi)
- ho (Hiri Motu)
- hr (Croatian)
- ht (Haitian)
- hu (Hungarian)
- hy (Armenian)
- hz (Herero)
- ia (Interlingua)
- id (Indonesian)
- ie (Interlingue)
- ig (Igbo)
- ii (Sichuan Yi)
- ik (Inupiat)
- io (Ido)
- is (Icelandic)
- it (Italian)
- iu (Inuktitut)
- ja (Japanese)
- jv (Javanese)
- ka (Georgian)
- kg (Kongo)
- ki (Kikuyu)
- kj (Kuanyama)
- kk (Kazakh)
- kl (Greenlandic)
- km (Cambodian)
- kn (Kannada)
- ko (Korean)
- kr (Kanuri)
- ks (Kashmiri)
- ku (Kurdish)
- kv (Komi)
- kw (Cornish)
- ky (Kirghiz)
- la (Latin)
- lb (Luxembourgish)
- lg (Ganda)
- li (Limburgian)
- ln (Lingala)
- lo (Laotian)
- lt (Lithuanian)
- lv (Latvian)
- mg (Malagasy)
- mh (Marshallese)
- mi (Maori)
- mk (Macedonian)
- ml (Malayalam)
- mn (Mongolian)
- mo (Moldovan)
- mr (Marathi)
- ms (Malay)
- mt (Maltese)
- my (Burmese)
- na (Nauruan)
- nd (North Ndebele)
- ne (Nepali)
- ng (Ndonga)
- nl (Dutch)
- nn (Norwegian Nynorsk)
- no (Norwegian)
- nr (South Ndebele)
- nv (Navajo)
- ny (Chichewa)
- oc (Occitan)
- oj (Ojibwa)
- om (Oromo)
- or (Oriya)
- os (Ossetian)
- pa (Punjabi)
- pi (Pali)
- pl (Polish)
- ps (Pashto)
- pt (Portuguese)
- qu (Quechua)
- rm (Raeto-Romance)
- rn (Kirundi)
- ro (Romanian)
- ru (Russian)
- rw (Rwandan)
- sa (Sanskrit)
- sc (Sardinian)
- sd (Sindhi)
- sg (Sango)
- sh (Serbo-Croatian)
- si (Sinhalese)
- sk (Slovak)
- sl (Slovenian)
- sm (Samoan)
- sn (Shona)
- so (Somali)
- sq (Albanian)
- sr (Serbian)
- ss (Swati)
- st (Southern Sotho)
- su (Sundanese)
- sv (Swedish)
- sw (Swahili)
- ta (Tamil)
- te (Telugu)
- tg (Tajik)
- th (Thai)
- ti (Tigrinya)
- tk (Turkmen)
- tl (Tagalog)
- tn (Tswana)
- to (Tonga)
- tr (Turkish)
- ts (Tsonga)
- tt (Tatar)
- tw (Twi)
- ty (Tahitian)
- ug (Uyghur)
- uk (Ukrainian)
- ur (Urdu)
- ve (Venda)
- vi (Vietnamese)
- vo (Volapük)
- wa (Walloon)
- wo (Wolof)
- xh (Xhosa)
- yi (Yiddish)
- yo (Yoruba)
- za (Zhuang)
- zh (Chinese)
- zu (Zulu)

## API Endpoints

- **POST `/translate`**

  - **Description:** Translates the provided text to the specified language.
  - **Request Body:**
    ```json
    {
        "text": "Hello, world!",
        "to": "es"
    }
    ```
  - **Response:**
    ```json
    {
        "translatedText": "¡Hola, mundo!",
        "status": true,
        "message": ""
    }
    ```
- **GET `/health`**

  - **Description:** Checks the health status of the server.
  - **Response:**
    ```json
    {
        "status": "healthy"
    }
    ```

## Testing the API

You can test the API endpoints using cURL:

### Translation Endpoint
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"text\": \"Hello\", \"to\": \"ja\"}" http://localhost:8000/translate
```

Expected response:
```json
{
    "translatedText": "Halo",
    "status": true,
    "message": ""
}
```

### Health Check
```bash
curl http://localhost:8000/health
```

## Contributing

Contributions to the Free Translate API are always welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
