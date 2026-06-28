#3
class User:
    __user_count =0
    users_list = []
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self._password_hush =self._hash_password(password)
        User.__user_count += 1
        User.users_list.append(self)

    @staticmethod
    def _hash_password(password):
        return f"str(hash({password}))"

    @staticmethod
    def is_valid_email(email):
        if "@" in email and "." in email.split("@")[-1]:
            return True
        return  False

    @staticmethod
    def is_strong_password(password):
        has_upper = False
        has_lower = False
        has_digit = False
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
        return      has_upper and has_lower and has_digit
    @staticmethod
    def create_user_safely(username, email, password):
        if not User.is_valid_email(email):
            print("error with email")
            return  None
        if not User.is_strong_password(password):
            print("week password")
            return None
        return  User(username , email ,password)
    @classmethod
    def get_user_count(cls):
        return cls.__user_count
    @classmethod
    def find_user_by_username(cls,username):
        for user in cls.users_list:
            if user.username == username:
                return user
        return  None
if __name__ == "__main__":
    print("--- בדיקה 1: ניסיון יצירת משתמש עם אימייל לא תקין ---")
    u1 = User.create_user_safely("elron", "invalid-email", "Pass1234")

    print("\n--- בדיקה 2: ניסיון יצירת משתמש עם סיסמה חלשה ---")
    u2 = User.create_user_safely("elron", "elron@gmail.com", "123")
    print("\n--- בדיקה 3: יצירת משתמשים תקינים ---")
    user_a = User.create_user_safely("dan", "dan@gmail.com", "SecurePass1")
    user_b = User.create_user_safely("rachel", "rachel@yahoo.com", "MyPassword9")

    print("\n--- בדיקה 4: בדיקת מונה המשתמשים הכללי ---")
    found_user = User.find_user_by_username("dan")
    if found_user:
        print(f"the user is founded his email is:{found_user.email}")


#4
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        if value > 0:
            self._width = value
        else:
            print("שגיאה: רוחב חייב להיות חיובי")

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        if value > 0:
            self._height = value
        else:
            print("שגיאה: גובה חייב להיות חיובי")

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    @property
    def is_square(self) -> bool:
        return self.width == self.height

    @staticmethod
    def create_square(side: float) -> 'Rectangle':
        return Rectangle(side, side)

    @staticmethod
    def compare_areas(rect1: 'Rectangle', rect2: 'Rectangle') -> str:
        if rect1.area > rect2.area:
            return f"המלבן הראשון גדול יותר (שטח: {rect1.area} לעומת {rect2.area})"
        elif rect2.area > rect1.area:
            return f"המלבן השני גדול יותר (שטח: {rect2.area} לעומת {rect1.area})"
        else:
            return f"השטחים שווים (שטח: {rect1.area})"


if __name__ == "__main__":
    r1 = Rectangle(5, 4)
    r2 = Rectangle(3, 6)

    print(f"מלבן 1: רוחב={r1.width}, גובה={r1.height}")
    print(f"שטח מלבן 1: {r1.area}, היקף מלבן 1: {r1.perimeter}")
    print(f"האם מלבן 1 הוא ריבוע? {r1.is_square}")

    r1.width = 6
    r1.height = 6
    print(f"לאחר שינוי - מלבן 1: רוחב={r1.width}, גובה={r1.height}")
    print(f"שטח חדש: {r1.area}, היקף חדש: {r1.perimeter}")
    print(f"האם מלבן 1 הוא ריבוע כעת? {r1.is_square}")

    r1.width = -2
    print(f"הרוחב בפועל נשאר: {r1.width}")

    square = Rectangle.create_square(4)
    print(f"נוצר ריבוע באמצעות מתודה סטטית: רוחב={square.width}, גובה={square.height}, שטח={square.area}")

    print(Rectangle.compare_areas(r1, r2))

#5
class Product:
    TAX_RATES = {
        'food': 0.05,
        'books': 0.0,
        'electronics': 0.17,
        'clothing': 0.12,
        'other': 0.17
    }

    def __init__(self, name, base_price, category='other', discount_percent=0):
        self._name = name
        self._base_price = 0
        self.base_price = base_price
        self._category = 'other'
        self.category = category
        self._discount_percent = 0
        self.discount_percent = discount_percent

    @property
    def name(self):
        return self._name

    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        if value < 0:
            print("שגיאה: מחיר לא יכול להיות שלילי")
        else:
            self._base_price = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value not in Product.TAX_RATES:
            print("שגיאה: קטגוריה לא קיימת")
        else:
            self._category = value

    @property
    def discount_percent(self):
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, value):
        if not (0 <= value <= 100):
            print("שגיאה: אחוז ההנחה חייב להיות בין 0 ל-100")
        else:
            self._discount_percent = value

    @property
    def price_after_discount(self):
        discount_amount = self.base_price * (self.discount_percent / 100)
        return self.base_price - discount_amount

    @property
    def tax_amount(self):
        tax_rate = Product.get_tax_rate(self.category)
        return self.price_after_discount * tax_rate

    @property
    def final_price(self):
        return self.price_after_discount + self.tax_amount

    @staticmethod
    def get_tax_rate(category):
        if category in Product.TAX_RATES:
            return Product.TAX_RATES[category]
        return Product.TAX_RATES['other']

    @staticmethod
    def calculate_bulk_discount(quantity, unit_price):
        if quantity >= 100:
            discount_rate = 0.15
        elif 50 <= quantity <= 99:
            discount_rate = 0.10
        elif 10 <= quantity <= 49:
            discount_rate = 0.05
        else:
            discount_rate = 0.0
        return quantity * unit_price * discount_rate


if __name__ == "__main__":
    p1 = Product("חלב", 6.5, "food")
    p2 = Product("מחשב נייד", 4000, "electronics", 10)

    print(f"מוצר: {p1.name} | מחיר מקורי: {p1.base_price} | מחיר סופי: {p1.final_price:.2f}")
    print(f"מוצר: {p2.name} | מחיר אחרי הנחה: {p2.price_after_discount} | מס: {p2.tax_amount} | מחיר סופי: {p2.final_price:.2f}")

    p1.base_price = -5
    p1.category = "space_ships"
    p1.discount_percent = 120

    unknown_tax = Product.get_tax_rate("unknown_category")
    print(f"מס לקטגוריה לא מוכרת: {unknown_tax}")

    bulk_discount = Product.calculate_bulk_discount(60, 10)
    print(f"סכום הנחת כמות: {bulk_discount} ש''ח")

