class Person:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city


    def introduce(self):
        print(f"hello i am :{self.name} my age is :{self.age} i am from: {self.city}")

    def have_birthday(self):
        self.age += 1
        print(f" happy birthday i am {self.age} today")

person1 = Person("moshe",40 ,"ashdod" )
person2 = Person("מיכל", 30, "חיפה")
person3 = Person("אלרון", 30, "בני ברק")


person1.introduce()
person2.introduce()
person3.introduce()

person1.have_birthday()


class Mosad:
    def __init__(self, name: str, mosad_type: str, students_count: int, city: str):
        self.name = name
        self.type = mosad_type
        self.students_count = students_count
        self.city = city

    def print_details(self):
        print(f"שם המוסד: {self.name}")
        print(f"סוג המוסד: {self.type}")
        print(f"מספר תלמידים: {self.students_count}")
        print(f"עיר: {self.city}")

    def add_students(self, amount: int):
        if amount > 0:
            self.students_count += amount
            print(f"נוספו {amount} תלמידים ל-{self.name}.")
        else:
            print("מספר התלמידים להוספה חייב להיות חיובי!")

    def remove_students(self, amount: int):
        if amount > 0:
            if self.students_count - amount < 0:
                print(f"שגיאה: אין מספיק תלמידים ב-{self.name} כדי להסיר {amount} (יש כרגע רק {self.students_count}).")
            else:
                self.students_count -= amount
                print(f"הוסרו {amount} תלמידים מ-{self.name}.")
        else:
            print("מספר התלמידים להסרה חייב להיות חיובי!")

school = Mosad("תיכון אורט", "בית ספר תיכון", 500, "נתניה")
university = Mosad("אוניברסיטת בר אילן", "אוניברסיטה", 18000, "רמת גן")


print("--- משימה 2: פרטי המוסדות לפני השינוי ---")
school.print_details()
university.print_details()

print("--- משימה 3: ביצוע שינויים ---")
school.add_students(50)
university.remove_students(20)