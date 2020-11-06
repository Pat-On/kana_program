class Student:
    """
    This class is going to collect information about progress done by student
    statistic: negative / positive answer


    """

    def __init__(self,):
        self.name = input("what is your name?")
        self.answer = str
        self.chosen_hiragana = False  # do I really need it?
        self.chosen_katakana = False

        # self.statistic = dict
        self.option = str  # from def choosing_material_to_study()

    # We are starting to make this class more simple and to decide, what we have to change to work with
    # the study_session class in association - it is no longer association - composition!

    def choosing_material_to_study(self):
        self.option = input("Choose option:")

        if self.option == "KANA":
            self.chosen_hiragana = True
            self.chosen_katakana = True
            return self.chosen_hiragana, self.chosen_katakana
        elif self.option == "HIRAGANA":
            self.chosen_hiragana = True
            self.chosen_katakana = False
            return self.chosen_hiragana, self.chosen_katakana
        elif self.option == "KATAKANA":
            self.chosen_hiragana = False
            self.chosen_katakana = True
            return self.chosen_hiragana, self.chosen_katakana
        else:
            print("Incorrect option. Try again")
            self.choosing_material_to_study()  # recursion. Is it going to work?
        return self.chosen_hiragana, self.chosen_katakana

    def set_answer_from_student(self):
        self.answer = input("Your guess: ")
        #  is not better to put here return function or to create new def?

    def get_students_answer(self):
        return self.answer

    # def update_statistic(self):
    #     pass
    #
    # def get_statistic(self):
    #     pass


