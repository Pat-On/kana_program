class Student:
    """
    This class is going to collect information about progress done by student
    statistic: negative / positive answer


    """

    def __init__(self, name="anonim" ):
        self.statistic = dict
        self.answer = str
        self.name = name

    def set_answer_from_student(self):
        self.answer = input()

        return self.answer

    def get_students_answer(self):
        return self.answer

    def test_module(self):
        print("I'm here!")
