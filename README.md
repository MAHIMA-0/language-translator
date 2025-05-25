# Language Translator

Language Translator is a Flask web application that translates text between multiple languages. It uses the `pycountry` library to get language codes and names and `GoogleTranslator` for translation.

## Features

- Translate text between many languages  
- Uses `pycountry` to list and handle languages  
- Powered by `GoogleTranslator` for accurate translations  
- Simple web interface with Flask  
- User input via HTML forms  

## Technologies Used

- Python  
- Flask 
- pycountry  
- GoogleTranslator (from `deep-translator`)  

## Project Structure

├── app.py  
├── requirements.txt  
├── Procfile  
├── templates/   
├── static/  



## Setup Instructions

1. Clone the repository:  
git clone https://github.com/MAHIMA-0/language-translator.git

3. Install dependencies:  
pip install -r requirements.txt

4. Run the Flask app:  
python app.py

5. Open your browser at `http://127.0.0.1:5000`

## Deployment

Ready to deploy on platforms like [Render](https://render.com) or Heroku.

---







