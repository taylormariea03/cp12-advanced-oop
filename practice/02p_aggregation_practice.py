from helper_functions import clear_screen
clear_screen()

# ======================
# AGGREGATION - PRACTICE
# ======================

# 1. PRACTICE
# Create a simplified system to model the relationship between students and
# class sections, showcasing aggregation.
# Define two classes:
#   ClassSection: with attributes for section_id and course_name,
#   Student: with attributes for name and enrolled_sections, the latter being
#            a list to track the class sections a student is enrolled in.
# Students can be directly enrolled in sections by adding ClassSection
# instances to their enrolled_sections list.

# Code a way for any Student object to display their enrolled class sections.
# Make objects of each class, add ClassSections to student objects,
# and diplay which students are in which class.

class ClassSection:
    def __init__(self, section_id, course_name):
            self.section_id = section_id
            self.course_name = course_name

class Student: 
    def __init__(self, name):
            self.name = name
            self.enrolled_sections = []

    def display_classes(self):
        message = f"{self.name} is enrolled in the following sections:"
        for section in self.enrolled_sections:
            message += f"\n\t{section.section_id} {section.course_name}"
        return message

cs_1 = ClassSection(1, "IS 303")
cs_2 = ClassSection(2, "ACC 200")
cs_3 = ClassSection(3, "FIN 201")
cs_4 = ClassSection(4, "DANCE 101")

s_1 = Student("taylor")
s_1.enrolled_sections.extend([cs_1, cs_2])
s_2 = Student("peyton")
s_2.enrolled_sections.extend([cs_3, cs_4])

print(s_1.display_classes())
print(s_2.display_classes())