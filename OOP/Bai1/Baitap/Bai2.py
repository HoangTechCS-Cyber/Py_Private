class student:
    def __init__(self, name: str, yob: int, grade: str):
        self.name = name
        self.yob = yob
        self.grade = grade
    def describe(self):
        print("Name:", self.name,"- Namsinh:", self.yob, "- grade:", self.grade)
class teacher:
    def __init__(self, name: str, yob: int, subject: str):
        self.name = name
        self.yob = name
        self.subject = subject
    def describe(self):
        print("Name:", self.name,"- Namsinh:", self.yob, "- subject:", self.subject)

class doctor:
    def __init__(self, name: str, yob: int, specialist: str):
        self.name = name
        self.yob  = yob
        self.cyan = specialist
    def describe(self):
        print("Name:", self.name,"- Namsinh:", self.yob, "- specialist:", self.cyan)

# Ward
