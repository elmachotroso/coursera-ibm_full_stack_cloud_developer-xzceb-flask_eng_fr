#!/usr/bin/env python3

"""
translator.py
A module that will allow EN <-> FR text translations.
"""

import os
import json
import requests
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Load security information from environment.
load_dotenv()
TRANSLATOR_APIKEY = os.environ['apikey']
TRANSLATOR_URL = os.environ['url']

def create_watson_translator( apikey, url ):
    """
    Creates an instance of the Watson Translator with the given
    api key and url.
    """
    authenticator = IAMAuthenticator( f'{ apikey }' )
    language_translator = LanguageTranslatorV3(
        version = '2021-10-01',
        authenticator = authenticator
    )

    language_translator.set_service_url( f'{ url }' )
    return language_translator

TRANSLATOR = create_watson_translator( TRANSLATOR_APIKEY, TRANSLATOR_URL )

# originally englishToFrench( englishText ) but pylint wants it snake_case
def english_to_french( english_text ):
    """
    Returns the french translation of the englishText provided
    """
    french_text = "le blah"
    return french_text

def main():
    """
    Main function entry point
    """
    print( str( TRANSLATOR ) )

if __name__ == "__main__":
    main()
