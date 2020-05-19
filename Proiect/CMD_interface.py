import CLIPS

def input_from_user():
    major_premise = input("Type out major premise:\n")
    minor_premise = input("Type out minor premise:\n")
    conclusion = input("Type out conclusion:\n")
    user_input = [major_premise, minor_premise, conclusion]
    CLIPS.run_CLIPS(user_input)

input_from_user()