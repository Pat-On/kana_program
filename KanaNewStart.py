import random

hiragana_dictionary = dict(あ="A", い="I", う="U", え="E", お="O", か="KA", き="KI", く="KU", け="KE", こ="KO", が="GA", ぎ="GI",
                           ぐ="GU", げ="GE", ご="GO", さ="SA", し="SI", す="SU", せ="SE", そ="SO", ざ="ZA", じ="ZI", ず="ZU",
                           ぜ="ZE", ぞ="ZO", た="TA", ち="TI", つ="TU", て="TE", と="TO", だ="DA", ぢ="DI", づ="DU", で="DE",
                           ど="DO", な="NA", に="NI", ぬ="NU", ね="NE", の="NO", は="HA", ひ="HI", ふ="HU", へ="HE", ほ="HO",
                           ば="BA", び="BI", ぶ="BU", べ="BE", ぼ="BO", ぱ="PA", ぴ="PI", ぷ="PU", ぺ="PE", ぽ="PO", ま="MA",
                           み="MI", む="MU", め="ME", も="MO", や="YA", ゆ="YU", よ="YO", ら="RA", り="RI", る="RU", れ="RE",
                           ろ="RO", わ="WA", ゐ="WI", ゑ="WE", を="WO", ん="N", ゔ="VU")

katakana_dictionary = dict(ア="A", イ="I", ウ="U", エ="E", オ="O", カ="KA", キ="KI", ク="KU", ケ="KE", コ="KO", ガ="GA", ギ="GI",
                           グ="GU", ゲ="GE", ゴ="GO", サ="SA", シ="SI", ス="SU", セ="SE", ソ="SO", ザ="ZA", ジ="ZI", ズ="ZU",
                           ゼ="ZE", ゾ="ZO", タ="TA", チ="TI", ツ="TU", テ="TE", ト="TO", ダ="DA", ヂ="DI", ヅ="DU", デ="DE",
                           ド="DO", ナ="NA", ニ="NI", ヌ="NU", ネ="NE", ノ="NO", ハ="HA", ヒ="HI", フ="HU", ヘ="HE", ホ="HO",
                           バ="BA", ビ="BI", ブ="BU", ベ="BE", ボ="BO", パ="PA", ピ="PI", プ="PU", ペ="PE", ポ="PO", マ="MA",
                           ミ="MI", ム="MU", メ="ME", モ="MO", ヤ="YA", ユ="YU", ヨ="YO", ラ="RA", リ="RI", ル="RU", レ="RE",
                           ロ="RO", ワ="WA", ヰ="WI", ヱ="WE", ヲ="WO", ン="N", ヴ="VU", ヷ="VA", ヸ="VI", ヹ="VE", ヺ="VO")


class MaterialGenerator:
    """
    This class is responsible for generating sets of 10 randomly chosen symbols from hiragana or katakana.
    """

    def __init__(self):
        self.katakana = katakana_dictionary
        self.hiragana = hiragana_dictionary
        self.words_to_study = {}
        # self.answers_to_studies_words = []  # It may be not necessary if im going to use dictionaries
        # self.neg_answers = []
        self.chosen_hiragana = False  # do I really need it?
        self.chosen_katakana = False
        # self.chosen = self.chosen # Why it don't work with it?

    def hiragana_or_katakana(self, chosen_hiragana=False, chosen_katakana=False):
        """
        This function is going to choose dictionary - base on decision of player
        :key chosen_hiragana: boolean
        :key chosen_katakana: boolean
        :return self.chosen: dictionary
        """
        # Future modification: add possibility to chose two dictionaries at the same time
        if chosen_hiragana is not False:
            self.chosen = self.hiragana
        elif chosen_katakana is not False:
            self.chosen = self.katakana

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

    def generator_3_neg_answers(self):
        """ I have to think it over if I'm going to need it at all, because I'm going to use dictionaries {key:value}

        I'm going to leave it now, later I will decide what to do with that.

        >>> Better option in my opinion is it to put it in "StudySession" class
        """
        pass

    def cleaning_words_to_study(self):
        """
        This Method is going to clean only the words_to_study (dictionary)
        :key nothing
        :return nothing
        """


        self.words_to_study = {}


class StudySession:
    """
    It is going to be main "loop" for entire program. It is going to have method which is going to initialize entire
    study session, and by this it is going to keep doing and taking input and sending output to other classes

    """
    def __init__(self):

    def answer_checker(self):
        pass

    def student_ques(self):
        pass

    def passing_answer(self):
        pass

    def update_statistic_result(self):
        pass

    def end_study_session(self):
        pass

class Student:
    """
    This class is going to collect information about progress done by student
    statistic: negative / positive answer


    """
    def __init__(self, ):
        pass



class MenuCMD:
    """
    Here are stored all print functions needed to not GUI version of application

    """
    def __init__(self):
        pass


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#                                      testing and studying section:

chosen1 = MaterialGenerator()

full_chosen_dictionary = MaterialGenerator().hiragana_or_katakana(chosen_hiragana=False, chosen_katakana=True)

ten_chosen_symbols = MaterialGenerator().generator_10_symbols(dict_param=full_chosen_dictionary)

print(full_chosen_dictionary)
print(ten_chosen_symbols)

stat = type(full_chosen_dictionary)
stat2 = type(ten_chosen_symbols)
print(f"Type of full_chosen_dictionary: {stat}")
print(f"Type of ten_chosen_symbols: {stat2}")
