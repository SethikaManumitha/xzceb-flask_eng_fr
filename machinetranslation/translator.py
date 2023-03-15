"""
Created on Fri Mar 10 20:38:28 2023

@author: sethika
"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#import os
#from dotenv import load_dotenv

#load_dotenv()
authenticator = IAMAuthenticator('JcbrV2VDMtWIoAztltaZAkK8C_h_wBaUu9h3-W8ddZ1O')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.jp-tok.language-translator.watson.cloud.ibm.com')
#apikey = os.environ['apikey']
#url = os.environ['url']

def english_to_french(english_text):
    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    print(french_text)
    return french_text

def french_to_english(french_text):
    english_text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text = english_text['translations'][0]['translation']
    print(english_text)
    return english_text






