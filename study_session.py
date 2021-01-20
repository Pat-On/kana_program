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
        self.symbols_needed_to_fake_answers = dict
        self.obj_material_generator = material_generator.MaterialGenerator()
        self.obj_student = student.Student()

    def chosen_set_by_student(self):
        """ Method is going to take chosen symbols and call material_generator to create necessary dictionary"""

        self.chosen_set = self.obj_material_generator.hiragana_or_katakana(self.obj_student.choosing_material_to_study())
        return self.chosen_set

    def twenty_negative_answers(self):
        """ this method is going to update 20 negative answer use with 1 correct in proposed answers"""

        self.symbols_needed_to_fake_answers = self.obj_material_generator.generator_20_neg_answers()
        return self.symbols_needed_to_fake_answers

    def questions_for_student(self):
        """ it is going through dict in random order and  print it to student. So we will have to mark
        in __init__ proper answer to have access to it from different place in code - technical problem"""
        pass

    def three_incorrect_answers(self):
        """
        this method is going to create 1 positive and 3 not correct proposition of answers, printed on the screen"
        I'm not sure if it is good place for it, or it is going to be better to put it into MaterialGenerator Class
        :return:
        """
        # self.obj_material_generator.get_20_neg_answers()
        # self.symbols_needed_to_fake_answers = self.obj_material_generator.get_20_neg_answers()
        # return self.symbols_needed_to_fake_answers
        pass

    def answer_checker(self, dictionary):
        """
        Leave the if else statement and try to use dictionary as a hash value to check is the answer is true
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

    def end_study_session(self):
        """ we can put it in check statement related to input from student"""
        pass

    def update_statistic_result(self):
        """update statistick stored in student class? or we are going to do different solution?"""
        pass

    # I'm quite sure, that is not good way to doing it
    # def student_answer_receiver(self):
    #     self.answer_of_student = student.get_students_answer()
    #
    #     return self.answer_of_student