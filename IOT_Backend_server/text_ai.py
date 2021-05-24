import csv
import os
import re
import sys

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

VOCAB_SIZE = 1000
epochs_count = 20
VERBOSE_LEVEL = 2
model_dir = os.path.join(os.path.dirname(__file__), 'model/')
csv_dir = os.path.join(os.path.dirname(__file__), 'FP/')


class AIModule:

    def __init__(self):
        self.__train_text = []
        self.__train_label = []
        self.__model = self.__create_model()
        self.__toknizer = None
        self.__get_model()

    @staticmethod
    def __clean_text(text: str):
        return ' '.join(re.sub("(@[a-zA-Z0-9]+)|([^0-9A-Za-z])|(https://[\w.]+/[\w]+)", " ", text).split())

    @staticmethod
    def __remove_number(text: str):
        result = ""
        for t in text:
            if t not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                result += t
        return result

    @classmethod
    def __clean_list(cls, items: list):
        result = []
        for i in items:
            i = cls.__clean_text(i)
            i = cls.__remove_number(i)
            result.append(i)

        return result

    @staticmethod
    def __create_model():
        m = tf.keras.Sequential([
            tf.keras.layers.Embedding(VOCAB_SIZE, 16),
            tf.keras.layers.GlobalAveragePooling1D(),
            tf.keras.layers.Dense(24, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid'),
        ])
        m.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return m

    @staticmethod
    def is_bad_word(sentance: str) -> bool:
        bad_word_li = []

        with open('datasets/bad-words.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                bad_word_li.append(row[0])

        for s in sentance.split(sep=' '):
            if s.lower() in bad_word_li:
                return True
        return False

    @staticmethod
    def __need_examine(sen: str):
        if not os.path.exists(csv_dir):
            try:
                os.mkdir(csv_dir)
            except:
                print(f"Error occured while creating new file\n{sys.exec_info()[0:1]}")
                raise
        open_mode = 'x'
        file_dir = os.path.join(csv_dir,'file.csv')
        if os.path.exists(file_dir):
            open_mode = 'a'
        with open(file_dir, mode=open_mode) as file:
            writer = csv.writer(file)
            writer.writerow([sen])

    def __get_csv_value(self):
        all_test_lables = []
        all_test_values = []
        emotions = ['anger', 'fear']
        with open('datasets/emotion-labels-train.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                self.__train_text.append(row[0])
                if row[1] in emotions or self.is_bad_word(row[0]):
                    self.__train_label.append(1)
                else:
                    self.__train_label.append(0)

        with open('datasets/train.txt', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                self.__train_text.append(row[0])
                if row[1] in emotions or self.is_bad_word(row[0]):
                    self.__train_label.append(1)
                else:
                    self.__train_label.append(0)
        #
        # with open('datasets/emotion-labels-val.csv', newline='') as f:
        #     reader = csv.reader(f)
        #     for row in reader:
        #         self.__train_text.append(row[0])
        #         if row[1] in ['anger']:
        #             self.__train_label.append(1)
        #         else:
        #             self.__train_label.append(0)

        with open('datasets/emotion-labels-test.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                all_test_values.append(row[0])
                if row[1] in emotions:
                    all_test_lables.append(1)
                else:
                    all_test_lables.append(0)

        self.__train_text = self.__clean_list(self.__train_text)
        all_test_values = self.__clean_list(all_test_values)

        return (self.__train_text, self.__train_label), (all_test_values, all_test_lables)

    def __get_model(self):
        if os.path.exists(model_dir) and len(os.listdir(model_dir)) > 0:
            self.__model.load_weights(model_dir)
        else:
            self.__train_model()

    def __get_toknizer(self):
        tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token='<OOV>')
        tokenizer.fit_on_texts(self.__train_text)
        return tokenizer

    def __tokonize_sentences(self, sentences: str):
        if self.__toknizer == None:
            tokenizer = self.__toknizer = self.__get_toknizer()
        else:
            tokenizer = self.__toknizer
        return np.array(pad_sequences(tokenizer.texts_to_sequences(sentences), padding='post', maxlen=34,
                                      truncating='pre'))

    def __train_model(self):
        # get data from csv files
        (train_sen, train_label), (test_sen, test_label) = self.__get_csv_value()

        # define the tensorFlow model

        tr_sequnces = self.__tokonize_sentences(train_sen)

        label = np.array(train_label)

        self.__model.fit(tr_sequnces, label, epochs=epochs_count, verbose=VERBOSE_LEVEL, callbacks=[
            tf.keras.callbacks.ModelCheckpoint(filepath=model_dir, save_weights_only=True)])

    def predict_values(self, values: list) -> int:
        test_sen = self.__tokonize_sentences(values)
        p = self.__model.predict(test_sen)
        p = p[0][0] * 100
        if p > 70:
            return 1, p
        elif self.is_bad_word(values):
            return 0.5, p
        else:
            return 0, p

    def predict_value(self, val: str) -> int:
        test_sen = self.__tokonize_sentences(val)
        p = self.__model.predict(test_sen)
        p = p[0][0] * 100
        if p > 70:
            return 1, p
        elif self.is_bad_word(val):
            #self.need_examine(val)
            return 0.5, p
        else:
            return 0, p

    def live_predict(self):
        in_sen = input("Insert sentence\n")
        while in_sen.lower() != 'exit':
            (ans, pred) = self.predict_value(in_sen)
            print(ans, pred)
            if ans == 1:
                print("This is a bad sentence")
            elif ans == 0.5:
                print("This sentence seems to have bad content")
            else:
                print('this is a good sentence')

            in_sen = input("Insert sentence\n")


