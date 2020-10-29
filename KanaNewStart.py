import material_generator

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#                                      testing and studying section:

chosen1 = material_generator.MaterialGenerator()

full_chosen_dictionary = material_generator.MaterialGenerator().hiragana_or_katakana(chosen_hiragana=False, chosen_katakana=True)

ten_chosen_symbols = material_generator.MaterialGenerator().generator_10_symbols(dict_param=full_chosen_dictionary)

print(full_chosen_dictionary)
print(ten_chosen_symbols)

stat = type(full_chosen_dictionary)
stat2 = type(ten_chosen_symbols)
print(f"Type of full_chosen_dictionary: {stat}")
print(f"Type of ten_chosen_symbols: {stat2}")
