import material_generator
import student
import random


class StudySession:
    """
    It is going to be main "loop" for entire program. It is going to have method which is going to initialize entire
    study session, and by this it is going to keep doing and taking input and sending output to other classes

    """

    def __init__(self):
        self.chosen_set = dict
        self.answer_of_student = str
        self.random_symbol = dict

    def four_answer_gen(self):
        """
        I'm not sure if it is good place for it, or it is going to be better to put it into MaterialGenerator Class
        :return:
        """
        pass

    # I'm quite sure, that is not good way to doing it
    # def student_answer_receiver(self):
    #     self.answer_of_student = student.get_students_answer()
    #
    #     return self.answer_of_student

    def answer_checker(self, dictionary):
        """

        """

        self.chosen_set = dictionary  # I'm not sure if it is going to work at all
        # self.answer_of_student = student.get_students_answer()

        while len(self.chosen_set) >= 0:
            self.random_symbol = (random.choice(list(self.chosen_set.keys())))
            print(self.random_symbol)
            self.answer_of_student = student.set_answer_from_student()
            while self.answer_of_student != self.random_symbol.keys():
                if self.answer_of_student == self.random_symbol.keys():
                    print("Good answer!")
                else:
                    print("Try one more time!")
            self.chosen_set.pop(self.random_symbol)


    def answer_option_generator(self):
        """ this method is going to create 1 positive and 3 not correct proposition of answers, printed on the screen"""
        pass

    # I'm not sure how I'm going to use the methods above

    def student_ques(self):
        pass

    def passing_answer(self):
        pass

    def update_statistic_result(self):
        pass

    def end_study_session(self):
        pass
