import random

hiragana_List_of_dictionaries = ({"\u3042": "A"}, {"\u3042": "I"}, {"\u3046": "U"}, {"\u3048": "E"}, {"\u304A": "O"},

                                 {"\u304B": "KA"}, {"\u304D": "KI"}, {"\u304F": "KU"}, {"\u3051": "KE"},
                                 {"\u3053": "KO"},
                                 {"\u304C": "GA"}, {"\u304E": "GI"}, {"\u3050": "GU"}, {"\u3052": "GE"},
                                 {"\u3054": "GO"},

                                 {"\u3055": "SA"}, {"\u3057": "SI"}, {"\u3059": "SU"}, {"\u305B": "SE"},
                                 {"\u305D": "SO"},
                                 {"\u3056": "ZA"}, {"\u3058": "ZI"}, {"\u305A": "ZU"}, {"\u305C": "ZE"},
                                 {"\u305E": "ZO"},

                                 {"\u305F": "TA"}, {"\u3061": "TI"}, {"\u3064": "TU"}, {"\u3066": "TE"},
                                 {"\u3068": "TO"},
                                 {"\u3060": "DA"}, {"\u3062": "DI"}, {"\u3065": "DU"}, {"\u3067": "DE"},
                                 {"\u3069": "DO"},

                                 {"\u306A": "NA"}, {"\u306B": "NI"}, {"\u306C": "NU"}, {"\u306D": "NE"},
                                 {"\u306E": "NO"},

                                 {"\u306F": "HA"}, {"\u3072": "HI"}, {"\u3075": "HU"}, {"\u3078": "HE"},
                                 {"\u307B": "HO"},
                                 {"\u3070": "BA"}, {"\u3073": "BI"}, {"\u3076": "BU"}, {"\u3079": "BE"},
                                 {"\u307C": "BO"},
                                 {"\u3071": "PA"}, {"\u3074": "PI"}, {"\u3077": "PU"}, {"\u307A": "PE"},
                                 {"\u307D": "PO"},

                                 {"\u307E": "MA"}, {"\u307F": "MI"}, {"\u3080": "MU"}, {"\u3081": "ME"},
                                 {"\u3082": "MO"},

                                 {"\u3084": "YA"}, {"\u3086": "YU"}, {"\u3088": "YO"},

                                 {"\u3089": "RA"}, {"\u308A": "RI"}, {"\u308B": "RU"}, {"\u308C": "RE"},
                                 {"\u308D": "RO"},

                                 {"\u308F": "WA"}, {"\u3090": "WI"}, {"\u3091": "WE"}, {"\u3092": "WO"},

                                 {"\u3093": "N"}, {"\u3094": "VU"},)

hiragana_unicode = ["\u3042", "\u3044", "\u3046", "\u3048", "\u304A",
                    "\u304B", "\u304D", "\u304F", "\u3051", "\u3053",
                    "\u304C", "\u304E", "\u3050", "\u3052", "\u3054",

                    "\u3055", "\u3057", "\u3059", "\u305B", "\u305D",
                    "\u3056", "\u3058", "\u305A", "\u305C", "\u305E",

                    "\u305F", "\u3061", "\u3064", "\u3066", "\u3068",
                    "\u3060", "\u3062", "\u3065", "\u3067", "\u3069",

                    "\u306A", "\u306B", "\u306C", "\u306D", "\u306E",

                    "\u306F", "\u3072", "\u3075", "\u3078", "\u307B",
                    "\u3070", "\u3073", "\u3076", "\u3079", "\u307C",
                    "\u3071", "\u3074", "\u3077", "\u307A", "\u307D",

                    "\u307E", "\u307F", "\u3080", "\u3081", "\u3082",

                    "\u3084", "\u3086", "\u3088",

                    "\u3089", "\u308A", "\u308B", "\u308C", "\u308D",

                    "\u308F", "\u3090", "\u3091", "\u3092",

                    "\u3093", "\u3094", ]

hiragana_phonetic_script = ["A", "I", "U", "E", "O",

                            "KA", "KI", "KU", "KE", "KO",
                            "GA", "GI", "GU", "GE", "GO",

                            "SA", "SI", "SU", "SE", "SO",
                            "ZA", "ZI", "ZU", "ZE", "ZO",

                            "TA", "TI", "TU", "TE", "TO",
                            "DA", "DI", "DU", "DE", "DO",

                            "NA", "NI", "NU", "NE", "NO",

                            "HA", "HI", "HU", "HE", "HO",
                            "BA", "BI", "BU", "BE", "BO",
                            "PA", "PI", "PU", "PE", "PO",

                            "MA", "MI", "MU", "ME", "MO",

                            "YA", "YU", "YO",

                            "RA", "RI", "RU", "RE", "RO",

                            "WA", "WI", "WE", "WO",

                            "N", "VU", ]

katakana_list_of_dictionaries = ({"\u30A2": "A"}, {"\u30A4": "I"}, {"\u30A6": "U"}, {"\u30A8": "E"}, {"\u30AA": "O"},

                                 {"\u30AB": "KA"}, {"\u30AD": "KI"}, {"\u30AF": "KU"}, {"\u30B1": "KE"},
                                 {"\u30B3": "KO"},
                                 {"\u30AC": "GA"}, {"\u30AE": "GI"}, {"\u30B0": "GU"}, {"\u30B2": "GE"},
                                 {"\u30B4": "GO"},

                                 {"\u30B5": "SA"}, {"\u30B7": "SI"}, {"\u30B9": "SU"}, {"\u30BB": "SE"},
                                 {"\u30BD": "SO"},
                                 {"\u30B6": "ZA"}, {"\u30B8": "ZI"}, {"\u30BA": "ZU"}, {"\u30BC": "ZE"},
                                 {"\u30BE": "ZO"},

                                 {"\u30BF": "TA"}, {"\u30C1": "TI"}, {"\u30C4": "TU"}, {"\u30C6": "TE"},
                                 {"\u30C8": "TO"},
                                 {"\u30C0": "DA"}, {"\u30C2": "DI"}, {"\u30C5": "DU"}, {"\u30C7": "DE"},
                                 {"\u30C9": "DO"},

                                 {"\u30CA": "NA"}, {"\u30CB": "NI"}, {"\u30CC": "NU"}, {"\u30CD": "NE"},
                                 {"\u30CE": "NO"},

                                 {"\u30CF": "HA"}, {"\u30D2": "HI"}, {"\u30D5": "HU"}, {"\u30D8": "HE"},
                                 {"\u30DB": "HO"},
                                 {"\u30D0": "BA"}, {"\u30D3": "BI"}, {"\u30D6": "BU"}, {"\u30D9": "BE"},
                                 {"\u30DC": "BO"},
                                 {"\u30D1": "PA"}, {"\u30D4": "PI"}, {"\u30D7": "PU"}, {"\u30DA": "PE"},
                                 {"\u30DD": "PO"},

                                 {"\u30DE": "MA"}, {"\u30DF": "MI"}, {"\u30E0": "MU"}, {"\u30E1": "ME"},
                                 {"\u30E2": "MO"},

                                 {"\u30E4": "YA"}, {"\u30E6": "YU"}, {"\u30E8": "YO"},

                                 {"\u30E9": "RA"}, {"\u30EA": "RI"}, {"\u30EB": "RU"}, {"\u30EC": "RE"},
                                 {"\u30ED": "RO"},

                                 {"\u30EF": "WA"}, {"\u30F0": "WI"}, {"\u30F1": "WE"}, {"\u30F2": "WO"},

                                 {"\u30F3": "N"}, {"\u30F4": "VU"},

                                 {"\u30F7": "VA"}, {"\u30F8": "VI"}, {"\u30F9": "VE"}, {"\u30FA": "VO"},)

katakana_unicode = ["\u30A2", "\u30A4", "\u30A6", "\u30A8", "\u30AA",

                    "\u30AB", "\u30AD", "\u30AF", "\u30B1", "\u30B3",
                    "\u30AC", "\u30AE", "\u30B0", "\u30B2", "\u30B4",

                    "\u30B5", "\u30B7", "\u30B9", "\u30BB", "\u30BD",
                    "\u30B6", "\u30B8", "\u30BA", "\u30BC", "\u30BE",

                    "\u30BF", "\u30C1", "\u30C4", "\u30C6", "\u30C8",
                    "\u30C0", "\u30C2", "\u30C5", "\u30C7", "\u30C9",

                    "\u30CA", "\u30CB", "\u30CC", "\u30CD", "\u30CE",

                    "\u30CF", "\u30D2", "\u30D5", "\u30D8", "\u30DB",
                    "\u30D0", "\u30D3", "\u30D6", "\u30D9", "\u30DC",
                    "\u30D1", "\u30D4", "\u30D7", "\u30DA", "\u30DD",

                    "\u30DE", "\u30DF", "\u30E0", "\u30E1", "\u30E2",

                    "\u30E4", "\u30E6", "\u30E8",

                    "\u30E9", "\u30EA", "\u30EB", "\u30EC", "\u30ED",

                    "\u30EF", "\u30F0", "\u30F1", "\u30F2",

                    "\u30F3", "\u30F4",

                    "\u30F7", "\u30F8", "\u30F9", "\u30FA", ]

katakana_phonetic_script = ["A", "I", "U", "E", "O",

                            "KA", "KI", "KU", "KE", "KO",
                            "GA", "GI", "GU", "GE", "GO",

                            "SA", "SI", "SU", "SE", "SO",
                            "ZA", "ZI", "ZU", "ZE", "ZO",

                            "TA", "TI", "TU", "TE", "TO",
                            "DA", "DI", "DU", "DE", "DO",

                            "NA", "NI", "NU", "NE", "NO",

                            "HA", "HI", "HU", "HE", "HO",
                            "BA", "BI", "BU", "BE", "BO",
                            "PA", "PI", "PU", "PE", "PO",

                            "MA", "MI", "MU", "ME", "MO",

                            "YA", "YU", "YO",

                            "RA", "RI", "RU", "RE", "RO",

                            "WA", "WI", "WE", "WO",

                            "N", "VU",

                            "VA", "VI", "VE", "VO", ]




class Student:
    def __init__(self, ):

        pass


class MaterialGenerator:
    def __init__(self, ):

        pass





# jak tworzysz obiekt jednorazowo to potym jak gra sie konczy
# to ten zostaje skasowany i tworzy sie nowy obiekt jako
# nowy obiekt losowania! jupi!

class HiraganaRandom:

    def __init__(self, no_hiragana):
        self.no_hiragana = no_hiragana
        self.symbols_to_study = []  # accumulator for symbols + answers to study

    def chosen_symbols(self):
        for i in range(0, self.no_hiragana):
            random_int = random.randint(0, len(hiragana_unicode) - 1)
            self.symbols_to_study.append([hiragana_unicode[random_int], hiragana_phonetic_script[random_int]])
        return self.symbols_to_study

    def return_function(self):
        return self.symbols_to_study

    def control_function(self):
        for i in self.symbols_to_study:
            print(i)


class KatakanaRandom:

    def __init__(self, no_katakana):
        self.no_katakana = no_katakana
        self.symbols_to_study = []  # accumulator for symbols + answers to study

    def chosen_symbols(self):
        for i in range(0, self.no_katakana):
            random_int = random.randint(0, len(katakana_unicode) - 1)
            self.symbols_to_study.append([katakana_unicode[random_int], katakana_phonetic_script[random_int]])
        return self.symbols_to_study

    def return_function(self):
        return self.symbols_to_study

    def control_function(self):
        for i in self.symbols_to_study:
            print(i)


class WrongAnswerGenerator:

    def __init__(self, requested_number):
        self.requested_number = requested_number
        self.gen_wrong_answer = []

    def wrong_answer_generator(self):
        for i in range(0, self.requested_number):
            random_int = random.randint(0, len(katakana_unicode) - 1)
            self.gen_wrong_answer.append(katakana_phonetic_script[random_int])

    def deleting_generated_before_answers(self):
        self.gen_wrong_answer = []

    def return_function(self):
        return self.gen_wrong_answer

    def control_function(self):
        for i in self.gen_wrong_answer:
            print(i)



class StudySession:

    def __init__(self, symbols_to_study, gen_wrong_answer):
        self.symbols_to_study = symbols_to_study
        self.gen_wrong_answer = gen_wrong_answer

    def study_session(self):
        # for i in self.symbols_to_study:
        pass


class BasicStatistic:
    pass


# Game:
# Bugs:
# 1. It is checking not correct answer, but it will give answer "good" what ever you choose
# from wrong answer generator
# 2. Doesn't work function to create positive answer....
# 3. You can make one object Kana and Hiragana, because code is going to be the same here
# 4. Logic is totally wrong here. It is not clear and mixed like hell that i do not have idea
# what I was thinking to do it.


hiragana_study = HiraganaRandom(10)
hiragana_study.chosen_symbols()
my_try2 = hiragana_study.return_function()


index_control = 0
for i in my_try2:
    wrong_answers = WrongAnswerGenerator(3)
    wrong_answers.wrong_answer_generator()

    my_try = 0
    my_try = wrong_answers.return_function()
    my_try.append(my_try2[index_control][1])
    print(my_try2[index_control][1])
    # random.shuffle(my_try)
    print(i[0])
    print("Bellow Answers:")
    print(my_try)
    answer = input("provide answer")

    if answer not in my_try2[index_control][1]:
        print("wrong answer")
    else:
        print("good answer")

    wrong_answers.deleting_generated_before_answers()
    print("************************************************")


wrong = Basic

print