Homework:

Object-Oriented Programming (OOP) Exercises

1. Circle Class
Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math

class Circle:
    #radiusini saqlaydi 
    def __init__(self, radius):
        self.radius=radius       
    # yuzani hisoblash metodi (A=п*r**2)

    def area(self):
        return math.pi*self.radius**2
    
    # perimetr hisoblash 
    def perimeter(self):
        return 2* math.pi*self.radius
    # bu classdan tashqarida turishi kerak 
if __name__ == '__main__':
    doira=Circle(10)

    print(f'doira yuzasi: {doira.area():.2f}')

    print(f'doira perimeter, {doira.perimeter():.2f}')


2. Person Class
Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

from datetime import datetime

class Person:
    """Shaxs sinfi, ism, mamlakat va tug'ilgan sanani saqlaydi va yoshni hisoblaydi."""
    def __init__(self, name, country, date_of_birth):
        if not isinstance(name, str) or not name:
            raise ValueError("Ism bo'sh yoki matn bo'lishi kerak")
        if not isinstance(country, str) or not country:
            raise ValueError("Mamlakat bo'sh yoki matn bo'lishi kerak")
        self.name = name
        self.country = country
        try:
            self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Tug'ilgan sana YYYY-MM-DD formatida bo'lishi kerak")
    
    def get_age(self):
        """Shaxsning yoshini hisoblaydi."""
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

if __name__ == "__main__":
    try:
        person = Person("Jamshid", "Uzbekistan", "2004-11-22")
        print(f"Ism: {person.name}")
        print(f"Mamlakat: {person.country}")
        print(f"Yosh: {person.get_age()} yosh")
    except ValueError as e:
        print(f"Xato: {e}")

3. Calculator Class
Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    """Asosiy arifmetik amallarni bajaradigan kalkulyator sinfi."""
    def add(self, a, b):
        """Ikki sonni qo'shadi."""
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Kiritilgan ma'lumotlar son bo'lishi kerak")
        return a + b

    def subtract(self, a, b):
        """Ikki sonni ayiradi."""
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Kiritilgan ma'lumotlar son bo'lishi kerak")
        return a - b

    def multiply(self, a, b):
        """Ikki sonni ko'paytiradi."""
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Kiritilgan ma'lumotlar son bo'lishi kerak")
        return a * b

    def divide(self, a, b):
        """Ikki sonni bo'ladi."""
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Kiritilgan ma'lumotlar son bo'lishi kerak")
        if b == 0:
            raise ZeroDivisionError("Nolga bo'lish mumkin emas")
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    try:
        print(f"Qo‘shish: 10 + 5 = {calc.add(10, 5)}")
        print(f"Ayirish: 10 - 5 = {calc.subtract(10, 5)}")
        print(f"Ko‘paytirish: 10 * 5 = {calc.multiply(10, 5)}")
        print(f"Bo‘lish: 10 / 5 = {calc.divide(10, 5)}")
        print(f"Nolga bo‘lish: 10 / 0 = ", end="")
        calc.divide(10, 0)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Xato: {e}")


4. Shape and Subclasses
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

import math

class Shakl:
    """Shakllar uchun abstrakt sinf."""
    def yuza(self):
        raise NotImplementedError("Bu metodni voris sinfda aniqlash kerak.")

    def perimetr(self):
        raise NotImplementedError("Bu metodni voris sinfda aniqlash kerak.")

class Doira(Shakl):
    """Doira sinfi, radius orqali yuza va perimetrni hisoblaydi."""
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius musbat son bo'lishi kerak")
        self.radius = radius

    def yuza(self):
        """Doira yuzasini hisoblaydi."""
        return math.pi * self.radius ** 2

    def perimetr(self):
        """Doira perimetrini hisoblaydi."""
        return 2 * math.pi * self.radius

class Kvadrat(Shakl):
    """Kvadrat sinfi, tomon uzunligi orqali yuza va perimetrni hisoblaydi."""
    def __init__(self, tomon):
        if not isinstance(tomon, (int, float)) or tomon <= 0:
            raise ValueError("Tomon musbat son bo'lishi kerak")
        self.tomon = tomon

    def yuza(self):
        """Kvadrat yuzasini hisoblaydi."""
        return self.tomon ** 2

    def perimetr(self):
        """Kvadrat perimetrini hisoblaydi."""
        return 4 * self.tomon

class Uchburchak(Shakl):
    """Uchburchak sinfi, uch tomon orqali yuza va perimetrni hisoblaydi."""
    def __init__(self, a, b, c):
        if not all(isinstance(x, (int, float)) for x in [a, b, c]) or any(x <= 0 for x in [a, b, c]):
            raise ValueError("Tomonlar musbat sonlar bo'lishi kerak")
        if a + b <= c or b + c <= a or a + c <= b:
            raise ValueError("Tomonlar uchburchak tengsizligiga mos kelmaydi")
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        """Uchburchak perimetrini hisoblaydi."""
        return self.a + self.b + self.c

    def yuza(self):
        """Uchburchak yuzasini Geron formulasi bo'yicha hisoblaydi."""
        s = self.perimetr() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

if __name__ == "__main__":
    try:
        doira = Doira(5)
        kvadrat = Kvadrat(4)
        uchburchak = Uchburchak(3, 4, 5)
        print(f"Doira yuzi: {doira.yuza():.2f}")
        print(f"Doira perimetri: {doira.perimetr():.2f}")
        print(f"Kvadrat yuzi: {kvadrat.yuza():.2f}")
        print(f"Kvadrat perimetri: {kvadrat.perimetr():.2f}")
        print(f"Uchburchak yuzi: {uchburchak.yuza():.2f}")
        print(f"Uchburchak perimetri: {uchburchak.perimetr():.2f}")
    except ValueError as e:
        print(f"Xato: {e}")


5. Binary Search Tree Class
Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

# Daraxt tuguni (node) sinfi
class Tugun:
    """Ikkilik qidiruv daraxti uchun tugun sinfi."""
    def __init__(self, qiymat):
        self.qiymat = qiymat
        self.chap = None
        self.ong = None

class IkkilikQidiruvDaraxti:
    """Ikkilik qidiruv daraxti sinfi."""
    def __init__(self):
        self.kok = None

    def qoshing(self, qiymat):
        """Daraxtga yangi qiymat qo'shadi."""
        if not isinstance(qiymat, (int, float)):
            raise ValueError("Qiymat son bo'lishi kerak")
        if self.kok is None:
            self.kok = Tugun(qiymat)
        else:
            self._qoshing_rekursiv(self.kok, qiymat)

    def _qoshing_rekursiv(self, joriy, qiymat):
        if qiymat < joriy.qiymat:
            if joriy.chap is None:
                joriy.chap = Tugun(qiymat)
            else:
                self._qoshing_rekursiv(joriy.chap, qiymat)
        elif qiymat > joriy.qiymat:
            if joriy.ong is None:
                joriy.ong = Tugun(qiymat)
            else:
                self._qoshing_rekursiv(joriy.ong, qiymat)
        else:
            raise ValueError(f"Qiymat {qiymat} allaqachon mavjud")

    def qidirish(self, qiymat):
        """Daraxtda qiymat mavjudligini tekshiradi."""
        if not isinstance(qiymat, (int, float)):
            raise ValueError("Qiymat son bo'lishi kerak")
        return self._qidirish_rekursiv(self.kok, qiymat)

    def _qidirish_rekursiv(self, joriy, qiymat):
        if joriy is None:
            return False
        if qiymat == joriy.qiymat:
            return True
        elif qiymat < joriy.qiymat:
            return self._qidirish_rekursiv(joriy.chap, qiymat)
        else:
            return self._qidirish_rekursiv(joriy.ong, qiymat)

if __name__ == "__main__":
    try:
        daraxt = IkkilikQidiruvDaraxti()
        daraxt.qoshing(50)
        daraxt.qoshing(30)
        daraxt.qoshing(70)
        daraxt.qoshing(20)
        daraxt.qoshing(40)
        daraxt.qoshing(60)
        daraxt.qoshing(80)
        print(f"60 soni mavjudmi? -> {daraxt.qidirish(60)}")
        print(f"25 soni mavjudmi? -> {daraxt.qidirish(25)}")
    except ValueError as e:
        print(f"Xato: {e}")



6. Stack Data Structure
Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class Stack:
    """Stack ma'lumotlar tuzilmasini amalga oshiradi."""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Elementni stack tepasiga qo'shadi."""
        self.items.append(item)

    def pop(self):
        """Stack tepasidagi elementni olib tashlaydi va qaytaradi."""
        if self.is_empty():
            raise IndexError("Stack bo‘sh, element olib tashlab bo‘lmaydi")
        return self.items.pop()

    def is_empty(self):
        """Stack bo'sh ekanligini tekshiradi."""
        return len(self.items) == 0

    def size(self):
        """Stackdagi elementlar sonini qaytaradi."""
        return len(self.items)

    def peek(self):
        """Stack tepasidagi elementni qaytaradi, olib tashlamasdan."""
        if self.is_empty():
            raise IndexError("Stack bo‘sh, element ko‘rsatib bo‘lmaydi")
        return self.items[-1]

if __name__ == "__main__":
    try:
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        print(f"Stack tepasidagi element: {stack.peek()}")
        print(f"Element olib tashlandi: {stack.pop()}")
        print(f"Yangi stack tepasidagi: {stack.peek()}")
        print(f"Stack hajmi: {stack.size()}")
    except IndexError as e:
        print(f"Xato: {e}")





7. Linked List Data Structure
Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

class Node:
    """Bog'langan ro'yxat uchun tugun sinfi."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Bog'langan ro'yxat ma'lumotlar tuzilmasi."""
    def __init__(self):
        self.head = None

    def display(self):
        """Ro'yxatdagi elementlarni ko'rsatadi."""
        if self.head is None:
            print("Ro'yxat bo'sh.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        """Ro'yxat oxiriga yangi element qo'shadi."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        """Berilgan qiymatga ega tugunni o'chiradi."""
        current = self.head
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if current is None:
            print(f"{value} ro'yxatda topilmadi.")
            return False
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        print(f"{value} o'chirildi.")
        return True

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.display()
    ll.delete(20)
    ll.display()
    ll.delete(40)


8. Shopping Cart Class
Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    """Xarid savatini boshqarish uchun sinf."""
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        """Savatga mahsulot qo'shadi."""
        if not isinstance(name, str) or not name:
            raise ValueError("Mahsulot nomi bo'sh yoki matn bo'lishi kerak")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Narx musbat son bo'lishi kerak")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Miqdor musbat butun son bo'lishi kerak")
        if name in self.items:
            self.items[name][1] += quantity
        else:
            self.items[name] = [price, quantity]

    def remove_item(self, name, quantity=1):
        """Savatdan mahsulotni olib tashlaydi."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Miqdor musbat butun son bo'lishi kerak")
        if name in self.items:
            self.items[name][1] -= quantity
            if self.items[name][1] <= 0:
                del self.items[name]
        else:
            raise ValueError(f"{name} savatda yo'q.")

    def get_total(self):
        """Savatdagi umumiy narxni hisoblaydi."""
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total

    def show_cart(self):
        """Savatdagi mahsulotlarni ko'rsatadi."""
        if not self.items:
            print("Savat bo'sh.")
        else:
            print("Savatdagi mahsulotlar:")
            for name, (price, quantity) in self.items.items():
                print(f"{name}: {quantity} dona, {price} so'm/dona")

if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("Olma", 5000, 3)
        cart.add_item("Banan", 7000, 2)
        cart.add_item("Olma", 5000, 1)
        cart.show_cart()
        print(f"Umumiy narx: {cart.get_total()} so'm")
        cart.remove_item("Banan", 1)
        cart.show_cart()
        print(f"Yangi umumiy narx: {cart.get_total()} so'm")
        cart.remove_item("Banan", 1)
        cart.show_cart()
    except ValueError as e:
        print(f"Xato: {e}")


9. Stack with Display
Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

class Stack:
    """Stack ma'lumotlar tuzilmasi, ko'rsatish funksiyasi bilan."""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Elementni stack tepasiga qo'shadi."""
        self.items.append(item)
        print(f"{item} stackga qo'shildi.")

    def pop(self):
        """Stack tepasidagi elementni olib tashlaydi va qaytaradi."""
        if self.is_empty():
            raise IndexError("Stack bo‘sh, element olib tashlab bo‘lmaydi")
        removed = self.items.pop()
        print(f"{removed} stackdan olib tashlandi.")
        return removed

    def display(self):
        """Stackdagi elementlarni yuqoridan pastga ko'rsatadi."""
        if self.is_empty():
            print("Stack bo'sh.")
        else:
            print("Stackdagi elementlar (yuqoridan pastga):")
            for item in reversed(self.items):
                print(item)

    def is_empty(self):
        """Stack bo'sh ekanligini tekshiradi."""
        return len(self.items) == 0

if __name__ == "__main__":
    try:
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        stack.display()
        stack.pop()
        stack.display()
    except IndexError as e:
        print(f"Xato: {e}")

10. Queue Data Structure
Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    """Navbat ma'lumotlar tuzilmasini amalga oshiradi."""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Elementni navbat oxiriga qo'shadi."""
        self.items.append(item)
        print(f"{item} navbatga qo'shildi.")

    def dequeue(self):
        """Navbat boshidagi elementni olib tashlaydi va qaytaradi."""
        if self.is_empty():
            raise IndexError("Navbat bo‘sh, element olib tashlab bo‘lmaydi")
        removed = self.items.pop(0)
        print(f"{removed} navbatdan olib tashlandi.")
        return removed

    def display(self):
        """Navbatdagi elementlarni boshidan oxirigacha ko'rsatadi."""
        if self.is_empty():
            print("Navbat bo'sh.")
        else:
            print("Navbatdagi elementlar (boshidan oxirigacha):")
            for item in self.items:
                print(item)

    def is_empty(self):
        """Navbat bo'sh ekanligini tekshiradi."""
        return len(self.items) == 0

if __name__ == "__main__":
    try:
        queue = Queue()
        queue.enqueue("Ali")
        queue.enqueue("Vali")
        queue.enqueue("Sami")
        queue.display()
        queue.dequeue()
        queue.display()
    except IndexError as e:
        print(f"Xato: {e}")


11. Bank Class
Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.


class Account:
    """Bank hisobini boshqarish uchun sinf."""
    def __init__(self, account_number, owner, balance=0):
        if not isinstance(account_number, str) or not account_number:
            raise ValueError("Hisob raqami bo'sh yoki matn bo'lishi kerak")
        if not isinstance(owner, str) or not owner:
            raise ValueError("Egasi bo'sh yoki matn bo'lishi kerak")
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Boshlang'ich balans musbat son bo'lishi kerak")
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Hisobga pul qo'shadi."""
        if not isinstance(amount, (int, float)):
            raise ValueError("Summa son bo'lishi kerak")
        if amount <= 0:
            raise ValueError("Summa musbat bo'lishi kerak")
        self.balance += amount
        print(f"{amount} so'm balansingizga qo'shildi.")
        return True

    def withdraw(self, amount):
        """Hisobdan pul yechadi."""
        if not isinstance(amount, (int, float)):
            raise ValueError("Summa son bo'lishi kerak")
        if amount > self.balance:
            raise ValueError("Hisobingizda yetarli mablag‘ yo‘q")
        if amount <= 0:
            raise ValueError("Summa musbat bo'lishi kerak")
        self.balance -= amount
        print(f"{amount} so'm yechildi.")
        return True

    def get_balance(self):
        """Joriy balansni qaytaradi."""
        return self.balance

class Bank:
    """Bank hisoblarini va tranzaksiyalarni boshqaradi."""
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, owner):
        """Yangi hisob ochadi."""
        if account_number in self.accounts:
            raise ValueError("Bu hisob raqami allaqachon mavjud")
        self.accounts[account_number] = Account(account_number, owner)
        print(f"Yangi hisob ochildi: {account_number}, egasi: {owner}")
        return True

    def deposit(self, account_number, amount):
        """Berilgan hisobga pul qo'shadi."""
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Hisob raqami topilmadi")
        return account.deposit(amount)

    def withdraw(self, account_number, amount):
        """Berilgan hisobdan pul yechadi."""
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Hisob raqami topilmadi")
        return account.withdraw(amount)

    def check_balance(self, account_number):
        """Berilgan hisobning balansini ko'rsatadi."""
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Hisob raqami topilmadi")
        print(f"Balans: {account.get_balance()} so'm")
        return account.get_balance()

if __name__ == "__main__":
    try:
        bank = Bank()
        bank.create_account("12345", "Ali")
        bank.create_account("67890", "Vali")
        bank.deposit("12345", 100000)
        bank.withdraw("12345", 25000)
        bank.check_balance("12345")
        bank.withdraw("67890", 5000)
        bank.check_balance("67890")
    except ValueError as e:
        print(f"Xato: {e}")
