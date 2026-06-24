import random


class Animal:
    def __init__(self, legs:int ,color:str , nums_kids:int, type:str):
        self.legs = legs
        self.color =color
        self.nums = nums_kids
        self.type =type
        self.tail = None

    def add_tail(self, long ,wide , fast_move):
        self.tail = Tail(long ,wide , fast_move)


class Tail:
    def __init__(self ,long ,wide , fast_move):
        self.long = long
        self.wide= wide
        self.fast_move = fast_move

class Cat(Animal):
    def __init__(self, color, nums_kids, whiskers_length):

        super().__init__(legs=4, color=color, nums_kids=nums_kids, type="חתול")
        self.whiskers_length = whiskers_length
        self.counter_mice = 0

    def mice_hunted_get(self):
        return self.counter_mice

    def mouse_hunt(self):
        self.counter_mice += 1
        print("🐈 מיאו! צדתי עוד עכבר!")



   



my_cat =Cat("brown" , 8 , 4)
print(f"לחתול שלי יש שפם באורך של {my_cat.whiskers_length}מ.ס")
print(f"ניסיון 1 - החתול צד היום: {my_cat.get_hunted_mice()} עכברים.")









a1 = Animal(4, "yelow", 4,"fish")
a2 = Animal(3, "black", 8, "fish")

a1.add_tail(6, 1.5, 54)



