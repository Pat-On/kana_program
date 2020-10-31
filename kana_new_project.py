import material_generator
import study_session
import student_student

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#                                      testing and studying section:

chosen1 = material_generator.MaterialGenerator()

# full_chosen_dictionary = material_generator.MaterialGenerator().hiragana_or_katakana(chosen_hiragana=True, chosen_katakana=False)
# full_chosen_dictionary = material_generator.MaterialGenerator().hiragana_or_katakana(chosen_hiragana=False, chosen_katakana=True)


full_chosen_dictionary = chosen1.hiragana_or_katakana(chosen_hiragana=True, chosen_katakana=True)
ten_chosen_symbols = chosen1.generator_10_symbols(dict_param=full_chosen_dictionary)
twenty_negative_answers_list = chosen1.generator_20_neg_answers(dict_param=full_chosen_dictionary)



patryk = student_student.Student()
study = study_session.StudySession()





print(full_chosen_dictionary)
print(ten_chosen_symbols)
print(twenty_negative_answers_list)

stat = type(full_chosen_dictionary)
stat2 = type(ten_chosen_symbols)
stat3 = type(twenty_negative_answers_list)
print(f"Type of full_chosen_dictionary: {stat}")
print(f"Type of ten_chosen_symbols: {stat2}")
print(f"Type of ten_chosen_symbols: {stat3}")
