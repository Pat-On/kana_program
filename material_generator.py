import hiragana_katakana_dictionaries
import random


class MaterialGenerator:
    """
    This class is responsible for generating sets of 10 randomly chosen symbols from hiragana or katakana.
    """

    def __init__(self):
        # self.katakana = hiragana_katakana_dictionaries.katakana_dictionary
        # self.hiragana = hiragana_katakana_dictionaries.hiragana_dictionary

        # WE are going to play now with object and composition
        self.obj_hiragana_katakana_dictionaries = hiragana_katakana_dictionaries.HiraganaKatakanaDictionaries()

        self.words_to_study = {}
        # self.answers_to_studies_words = []  # It may be not necessary if im going to use dictionaries
        self.neg_answers = []
        self.chosen_hiragana = False  # do I really need it?
        self.chosen_katakana = False
        # self.chosen = self.chosen # Why it don't work with it?
        self.dict_param = dict
        self.random_symbol = dict
        self.chosen = None

    def hiragana_or_katakana(self, chosen_hiragana=False, chosen_katakana=False):
        """
        This function is going to choose dictionary - base on decision of player
        :key chosen_hiragana: boolean
        :key chosen_katakana: boolean
        :return self.chosen: dictionary
        """
        if (chosen_hiragana is not False) and (chosen_katakana is not False):
            # self.chosen = dict(self.hiragana.update(self.katakana))
            self.chosen = {**self.obj_hiragana_katakana_dictionaries.get_hiragana(), **self.obj_hiragana_katakana_dictionaries.get_katakana()}
        elif chosen_hiragana is not False:
            self.chosen = self.obj_hiragana_katakana_dictionaries.get_hiragana()
        elif chosen_katakana is not False:
            self.chosen = self.obj_hiragana_katakana_dictionaries.get_katakana()

        return self.chosen

    def generator_10_symbols(self, dict_param):
        """
        This function is going to take 10 chosen symbols from passed through dictionary
        :key dict_param: dictionary
        :return words_to_study: dictionary
        """
        self.dict_param = dict_param
        # "_" python way of iteration through iterable
        for _ in range(10):
            self.random_symbol = (random.choice(list(self.dict_param.keys())))
            self.words_to_study[self.random_symbol] = self.dict_param[self.random_symbol]
            self.dict_param.pop(self.random_symbol)

        return self.words_to_study

    def generator_20_neg_answers(self, dict_param):
        """ It is going to take choose 10 randomly chosen answers to use it in study_session as a 3 fake correct answers

        I have to think it over if I'm going to need it at all, because I'm going to use dictionaries {key:value}
        I'm going to leave it now, later I will decide what to do with that.
        Better option in my opinion is it to put it in "StudySession" class
        """
        self.dict_param = dict_param
        for _ in range(20):
            self.random_symbol = (random.choice(list(self.dict_param.keys())))
            self.neg_answers.append(self.dict_param[self.random_symbol])
            self.dict_param.pop(self.random_symbol)

        return self.neg_answers

    def cleaning_words_to_study(self):
        """
        This Method is going to clean only the words_to_study (dictionary)
        :key None
        :return None
        """

        self.words_to_study = {}

    def get_20_neg_answers(self):

        return self.neg_answers

    def get_10_generated_symbols(self):

        return self.words_to_study

