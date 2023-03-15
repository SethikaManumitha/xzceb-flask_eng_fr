# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:33:46 2023

@author: user
"""

import unittest
import sys
sys.path.append(r'C:\Users\user\Documents\GitHub\xzceb-flask_eng_fr\machinetranslation')
from translator import english_to_french,french_to_english

class TestMyModule(unittest.TestCase):
    def test_englishToFrench_not_null(self):
        self.assertIsNone(english_to_french('hello'), 'not null')
    
    def test_frenchToEnglish_not_null(self):
        self.assertIsNone(french_to_english('bonjour'), 'not null')
    
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('hello'), "Bonjour")
        
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('bonjour'), "Hello")
        
    

if __name__ == '__main__':
    unittest.main()
    