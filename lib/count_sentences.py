#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Use the property setter to initialize the value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Use regex to split on ., !, ?
        sentences = re.split(r'[.!?]+', self._value)
        # Filter out any empty strings from the list
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
