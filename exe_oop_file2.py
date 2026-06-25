

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        return f"שלום, אני {self.name}, בן/בת {self.age} מ{self.city}"


class Student(Person):
    def __init__(self, name, age, city, student_id, grade):
        super().__init__(name, age, city)
        self.student_id = student_id
        self.grade = grade

    def study(self):
        print(f"{self.name} לומד בשכבה {self.grade}")

    def introduce(self):
        base_intro = super().introduce()
        print(f"{base_intro}, לומד בשכבה {self.grade}")

    # משימה 6: קידום שכבה (למשל מט' לי')
    def advance_grade(self, new_grade):
        self.grade = new_grade


class Teacher(Person):
    def __init__(self, name, age, city, subject, years_experience):
        super().__init__(name, age, city)
        self.subject = subject
        self.years_experience = years_experience

    # תיקון הזחה - המתודות כעת מחוץ ל-__init__
    def teach(self):
        print(f"{self.name} מלמד {self.subject} כבר {self.years_experience} שנים")

    def introduce(self):
        base_intro = super().introduce()
        print(f"{base_intro}, מלמד {self.subject}")

    # משימה 7: הוספת שנת ניסיון
    def gain_experience(self):
        self.years_experience += 1


class Principal(Person):
    def __init__(self, name, age, city, years_as_principal):
        super().__init__(name, age, city)
        self.years_as_principal = years_as_principal

    def manage(self):
        print(f"המנהל {self.name} מנהל את בית הספר בריכוז רב")

    def introduce(self):
        base_intro = super().introduce()
        print(f"{base_intro}, מנהל כבר {self.years_as_principal} שנים")

    # משימה 8: הוספת שנת ניהול
    def add_management_experience(self):
        self.years_as_principal += 1


# --- משימות 1-3: יצירת האובייקטים ---
student = Student(name="דני", age=16, city="תל אביב", student_id="S123", grade="ט'")
teacher = Teacher(name="רחל", age=40, city="ירושלים", subject="מתמטיקה", years_experience=10)
principal = Principal(name="ישראל", age=55, city="חיפה", years_as_principal=5)

# --- משימה 4: שימוש במתודת introduce ---
print("\n--- משימה 4: הצגה עצמית ---")
student.introduce()
teacher.introduce()
principal.introduce()

# --- משימה 5: שימוש במתודות הייחודיות ---
print("\n--- משימה 5: פעולות ייחודיות ---")
student.study()
teacher.teach()
principal.manage()

# --- משימות 6-8: עדכון הנתונים ---
student.advance_grade("י'")
teacher.gain_experience()
principal.add_management_experience()

# --- משימה 9: הדפסת הפרטים שוב כדי לראות שינויים ---
print("\n--- משימה 9: הדפסה לאחר השינויים ---")
student.introduce()
teacher.introduce()
principal.introduce()