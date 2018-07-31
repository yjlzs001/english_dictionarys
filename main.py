#!/usr/bin/env python
# coding=utf-8
import sys

DICT_FILE_PATH = './dictionary.data'

class Main:
    @staticmethod
    def readLines(fileObj):
        strs = fileObj.readlines()
        return strs

    @staticmethod
    def line_data_check(str):
        controlVariable = True
        for ch in str:
            if controlVariable:
                if isalpht(ch):
                    word.append(ch)
                elif ch == ':':
                    controlVariable = False
                else:
                    pass
            else:
                if not ch == ';':
                    interpretation.append(ch)
                else:
                    pass
        return Word(word, interpretation)

    def __init__(self):
        pass

    def item(self):
        while True:

            print('please input a option to work me.')
            print('1. add a new word.')
            print('2. seek a word.')
            print('q. quit program.')

            user_input = input()
            if user_input == '1':
                pass
            elif user_input == '2':
                pass
            elif user_input == 'q':
                pass
            else:
                pass


    def add_word(self):
        pass

#单词输入格式异常
class wordException(Exception):
    def __str__(self):
        return 'Word format exception.'

#释义输入格式异常
class interpretationException(Exception):
    def __str__(self):
        return 'Interpretation format exception.'

class Word:
    @property
    def word(self):
        return self.__word
    @word.setter
    def word(self, word):
        for ch in word:
            if ch != ' ' or not x.isalpha():
                raise wordException
            else:
                pass

    @property
    def interpretation(self):
        return self.__interpretation
    @interpretation.setter
    def interpretation(self, interpretation):
        for ch in interpretation:
            if not u'\u4e00' <= ch <= u'\u9fff':
                raise interpretationException
            else:
                pass

    def __init__(self, word, interpretation):
        self.__word = word
        self.__interpretation = interpretation

class Dictionary:
    def __init__(self, fileObj):
        strs = Main.readLines()
        for x in strs:
            self.append(Main.line_data_check(x))

    def apeend(self, word):
        self.__dictionarys.append(word)

if __name__ == '__main__':
    pass
