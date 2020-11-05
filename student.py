class Student:
    """
    This class is going to collect information about progress done by student
    statistic: negative / positive answer


    """

    def __init__(self, name="anonim" ):
        self.statistic = dict
        self.answer = str
        self.name = name
        self.chosen_hiragana = False  # do I really need it?
        self.chosen_katakana = False
        self.option = str

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

    def set_answer_from_student(self):
        self.answer = input()

    def get_students_answer(self):
        return self.answer

    @staticmethod
    def test_module():
        print("I'm here!")
