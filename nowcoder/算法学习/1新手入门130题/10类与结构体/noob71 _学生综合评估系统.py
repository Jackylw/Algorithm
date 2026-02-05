# https://www.nowcoder.com/practice/d8d5d6294b8f48b684ea93fbb4935a2b
class Student:
    def __init__(self, student_id, academic_score, activity_score):
        self.id = student_id
        self.academic_score = academic_score
        self.activity_score = activity_score


def is_excellent(student):
    s = student.academic_score * 0.7 + student.activity_score * 0.3
    total = student.academic_score + student.activity_score
    if total > 140 and s >= 80:
        return True
    return False
