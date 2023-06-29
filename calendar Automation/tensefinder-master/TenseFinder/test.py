# import os.path

# with open('last_event', 'w') as file:
#     file.write('tmro dfsfg')


# with open('last_event') as f:
#     lines = f.readlines()

# print(lines)

# from datetime import datetime, timedelta

# print(datetime.now() + timedelta(hours=24))
# print(datetime.now())

from TenseParser import TenseParser
tense_parser = TenseParser()
p1 = tense_parser.find_tense_simple_form_str("let's meet tomorrow")

p2 = tense_parser.find_tense_simple_form_str("I'm going tomorrow")
# p3 = tense_parser.find_tense_simple_form_str("I was there")
print(p1)
print(p2)
# print(p3)