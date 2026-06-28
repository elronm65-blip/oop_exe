class DigitalSafe:
    def __init__(self, id, code):
        # תכונות המחלקה לפי הגדרות הפרטיות
        self._safe_id = id              # מוגן (Protected)
        self.__code = code                   # פרטי (Private) - קוד לפתיחה
        self.__is_locked = True              # פרטי - כספת נעולה כברירת מחדל
        self.__attempt_count = 0             # פרטי - מונה ניסיונות פתיחה

    def try_unlock(self, code):
        """מנסה לפתוח את הכספת. מותר עד 3 ניסיונות כושלים."""
        # אם הכספת כבר פתוחה
        if not self.__is_locked:
            print("הכספת כבר פתוחה!")
            return

        # אם הגענו או עברנו את מקסימום הניסיונות (3)
        if self.__attempt_count >= 3:
            print("הכספת חסומה! הגעת ל-3 ניסיונות כושלים.")
            return

        # בדיקת הקוד
        if code == self.__code:
            self.__is_locked = False
            self.__attempt_count = 0  # איפוס המונה בהצלחה
            print("הכספת נפתחה בהצלחה!")
        else:
            self.__attempt_count += 1
            attempts_left = 3 - self.__attempt_count
            print(f"קוד שגוי! נשארו לך עוד {attempts_left} ניסיונות.")

    def lock(self):
        """נועלת את הכספת"""
        self.__is_locked = True
        print("הכספת ננעלה.")

    def is_locked(self):
        """מחזירה True אם נעול, False אם פתוח"""
        return self.__is_locked

    def get_attempts_left(self):
        """מחזירה את מספר הניסיונות שנותרו"""
        # מספר הניסיונות שנותרו הוא פשוט 3 פחות המונה, אך לא פחות מ-0
        return max(0, 3 - self.__attempt_count)

    def reset_attempts(self):
        """מאפסת את מונה הניסיונות - רק אם הכספת פתוחה!"""
        if not self.__is_locked:
            self.__attempt_count = 0
            print("מונה הניסיונות אופס בהצלחה.")
        else:
            print("לא ניתן לאפס מונה של כספת נעולה!")





# ==========================================
# קוד לבדיקת המחלקה (תוכל להריץ ולראות איך זה עובד)
# ==========================================
if __name__ == "__main__":
    print("--- יצירת כספת חדשה עם קוד 1234 ---")
    my_safe = DigitalSafe("SAFE-99", "1234")


    print("\n--- ניסיון פתיחה עם קוד שגוי (1) ---")
    my_safe.try_unlock("0000")
    print(f"ניסיונות שנותרו: {my_safe.get_attempts_left()}")

    print("\n--- ניסיון פתיחה עם קוד שגוי (2) ---")
    my_safe.try_unlock("5555")

    print("\n--- ניסיון איפוס מונה כשהכספת עדיין נעולה ---")
    my_safe.reset_attempts()

    print("\n--- פתיחה עם קוד נכון ---")
    my_safe.try_unlock("1234")
    print(f"האם נעול? {my_safe.is_locked()}")

    print("\n--- איפוס מונה כשהכספת פתוחה ---")
    my_safe.reset_attempts()

    print("\n--- נעילה מחדש ---")
    my_safe.lock()
    print(f"האם נעול? {my_safe.is_locked()}")