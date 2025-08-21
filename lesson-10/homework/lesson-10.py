Homework Projects:

Homework 1. ToDo List Application

1.Define Task Class:
Create a Task class with attributes such as task title, description, due date, and status.

class Task:
    def __init__(self, title, description, due_date, status=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status  # False = incomplete, True = complete

2.Define ToDoList Class:
Create a ToDoList class that manages a list of tasks.
Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.

class ToDoList:
    def __init__(self):
        """Initialize an empty list to store tasks."""
        self.tasks = []

    def add_task(self, task_description):
        """Add a new task to the list."""
        task = {
            'description': task_description,
            'completed': False
        }
        self.tasks.append(task)
        print(f"Task '{task_description}' added successfully.")

    def mark_task_complete(self, task_index):
        """Mark a task as complete by its index."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            print(f"Task '{self.tasks[task_index]['description']}' marked as complete.")
        else:
            print("Invalid task index.")

    def list_all_tasks(self):
        """Display all tasks with their status."""
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("\nAll Tasks:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task['completed'] else "Incomplete"
            print(f"{index + 1}. {task['description']} - {status}")

    def list_incomplete_tasks(self):
        """Display only incomplete tasks."""
        incomplete_tasks = [task for task in self.tasks if not task['completed']]
        if not incomplete_tasks:
            print("No incomplete tasks.")
            return
        print("\nIncomplete Tasks:")
        for index, task in enumerate(incomplete_tasks):
            print(f"{index + 1}. {task['description']}")

# Example usage:
if __name__ == "__main__":
    todo = ToDoList()
    todo.add_task("Buy groceries")
    todo.add_task("Finish homework")
    todo.add_task("Call mom")
    todo.list_all_tasks()
    todo.mark_task_complete(1)
    todo.list_all_tasks()
    todo.list_incomplete_tasks()



3.Create Main Program:
Develop a simple CLI to interact with the ToDoList.
Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Task '{self.tasks[index].description}' marked as complete.")
        else:
            print("Invalid task index.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("All Tasks:")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Incomplete"
                print(f"{i}. {task.description} - {status}")

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if not task.completed]
        if not incomplete:
            print("No incomplete tasks.")
        else:
            print("Incomplete Tasks:")
            for i, task in enumerate(incomplete):
                print(f"{i}. {task.description}")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            try:
                index = int(input("Enter task index to mark complete: "))
                todo_list.mark_complete(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            todo_list.list_all_tasks()
        elif choice == "4":
            todo_list.list_incomplete_tasks()
        elif choice == "5":
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()


4.Test the Application:
Create instances of tasks and test the functionality of your ToDoList.


def test_todo_list():
    todo_list = ToDoList()
    print("Starting ToDoList tests...")

    print("\nTest 1: Adding tasks")
    todo_list.add_task(Task("Buy groceries", "", ""))
    todo_list.add_task(Task("Finish homework", "", ""))
    todo_list.add_task(Task("Call doctor", "", ""))
    todo_list.list_all_tasks()

    print("\nTest 2: Marking task as complete")
    todo_list.mark_task_complete(1)
    todo_list.list_all_tasks()

    print("\nTest 3: Listing incomplete tasks")
    todo_list.list_incomplete_tasks()

    print("\nTest 4: Marking task with invalid index")
    todo_list.mark_task_complete(10)

    print("\nTest 5: Empty list behavior")
    todo_list.tasks = []
    todo_list.list_all_tasks()
    todo_list.list_incomplete_tasks()

if __name__ == "__main__":
    test_todo_list()

Homework 2. Simple Blog System

1.Define Post Class:
Create a Post class with attributes like title, content, and author.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Content: {self.content}")



2.Define Blog Class:
Create a Blog class that manages a list of posts.
Include methods to add a post, list all posts, and display posts by a specific author.


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)
        print(f"Post '{title}' by {author} added.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts in the blog.")
        else:
            print("All Posts:")
            for i, post in enumerate(self.posts):
                print(f"{i}. Title: {post.title}, Author: {post.author}")
                print(f"   Content: {post.content}\n")

    def list_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author.lower() == author.lower()]
        if not author_posts:
            print(f"No posts found by author '{author}'.")
        else:
            print(f"Posts by {author}:")
            for i, post in enumerate(author_posts):
                print(f"{i}. Title: {post.title}")
                print(f"   Content: {post.content}\n")


3.Create Main Program:
Develop a CLI to interact with the Blog system.
Include options to add posts, list all posts, and display posts by a specific author.


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)
        print(f"Post '{title}' by {author} added.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts in the blog.")
        else:
            print("All Posts:")
            for i, post in enumerate(self.posts):
                print(f"{i}. Title: {post.title}, Author: {post.author}")
                print(f"   Content: {post.content}\n")

    def list_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author.lower() == author.lower()]
        if not author_posts:
            print(f"No posts found by author '{author}'.")
        else:
            print(f"Posts by {author}:")
            for i, post in enumerate(author_posts):
                print(f"{i}. Title: {post.title}")
                print(f"   Content: {post.content}\n")

def main():
    blog = Blog()
    while True:
        print("\nBlog System Menu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(title, content, author)
        elif choice == "2":
            blog.list_all_posts()
        elif choice == "3":
            author = input("Enter author name: ")
            blog.list_posts_by_author(author)
        elif choice == "4":
            print("Exiting Blog System.")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()

4.Enhance Blog System:
Add functionality to delete a post, edit a post, and display the latest posts.


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)
        print(f"Post '{title}' by {author} added.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts in the blog.")
        else:
            print("All Posts:")
            for i, post in enumerate(self.posts):
                print(f"{i}. Title: {post.title}, Author: {post.author}")
                print(f"   Content: {post.content}\n")

    def list_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author.lower() == author.lower()]
        if not author_posts:
            print(f"No posts found by author '{author}'.")
        else:
            print(f"Posts by {author}:")
            for i, post in enumerate(author_posts):
                print(f"{i}. Title: {post.title}")
                print(f"   Content: {post.content}\n")

def main():
    blog = Blog()
    while True:
        print("\nBlog System Menu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(title, content, author)
        elif choice == "2":
            blog.list_all_posts()
        elif choice == "3":
            author = input("Enter author name: ")
            blog.list_posts_by_author(author)
        elif choice == "4":
            print("Exiting Blog System.")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()


5.Test the Application:
Create instances of posts and test the functionality of your Blog system.


from blog_cli import Post, Blog  # Agar alohida faylga yozilgan bo'lsa, aks holda bu qatorni olib tashlang

def test_blog_system():
    # Yangi Blog obyektini yaratish
    blog = Blog()
    print("Blog tizimi testlari boshlanmoqda...")

    # Test 1: Post qo'shish
    print("\nTest 1: Post qo'shish")
    blog.add_post("First Post", "This is a test post.", "Alice")
    blog.add_post("Tech Talk", "Discussing AI advancements.", "Bob")
    blog.add_post("Life Update", "My recent adventures.", "Alice")
    blog.add_post("Python Tips", "Learning Python basics.", "Bob")
    print("Kutilmoqda: 4 ta post qo'shildi.")
    blog.list_all_posts()  # 4 ta post ko‘rsatilishi kerak

    # Test 2: Muallif bo‘yicha postlarni ko‘rsatish
    print("\nTest 2: Muallif 'Alice' postlarini ko‘rsatish")
    blog.list_posts_by_author("Alice")  # Alice ning 2 ta posti ko‘rsatilishi kerak

    # Test 3: Postni tahrirlash
    print("\nTest 3: Postni tahrirlash")
    blog.edit_post(0, "Updated First Post", "This is an updated test post.", "Alice Smith")
    print("Kutilmoqda: 0-indeksdagi post yangilandi.")
    blog.list_all_posts()  # 0-indeksdagi post yangilangan ko‘rinishi kerak

    # Test 4: Postni o‘chirish
    print("\nTest 4: Postni o‘chirish")
    blog.delete_post(1)  # "Tech Talk" postini o‘chirish
    print("Kutilmoqda: 1-indeksdagi post o‘chirildi.")
    blog.list_all_posts()  # Endi 3 ta post qolgan

    # Test 5: So‘nggi postlarni ko‘rsatish
    print("\nTest 5: So‘nggi 2 ta postni ko‘rsatish")
    blog.list_latest_posts(2)  # Oxirgi 2 post ko‘rsatiladi

    # Test 6: Noto‘g‘ri indeks bilan o‘chirish (xato holat)
    print("\nTest 6: Noto‘g‘ri indeks bilan post o‘chirish")
    blog.delete_post(10)  # Xato indeks uchun xabar chiqishi kerak

    # Test 7: Noto‘g‘ri indeks bilan tahrirlash (xato holat)
    print("\nTest 7: Noto‘g‘ri indeks bilan post tahrirlash")
    blog.edit_post(10, "Invalid Post", "Invalid content", "Invalid")  # Xato indeks uchun xabar

    # Test 8: Mavjud bo‘lmagan muallif postlarini ko‘rsatish
    print("\nTest 8: Mavjud bo‘lmagan muallif 'Charlie' postlari")
    blog.list_posts_by_author("Charlie")  # Post topilmasa xabar

    # Test 9: Bo‘sh blog holati
    print("\nTest 9: Bo‘sh blog holati")
    blog.posts = []  # Postlarni tozalash
    blog.list_all_posts()  # Post yo‘qligi haqida xabar
    blog.list_latest_posts(3)  # Post yo‘qligi haqida xabar
    blog.list_posts_by_author("Alice")  # Post yo‘qligi haqida xabar

if __name__ == "__main__":
    test_blog_system()


Homework 3. Simple Banking System


1.Define Account Class:
Create an Account class with attributes like account number, account holder name, and balance.

class Account:
    def __init__(self,account_number,account_holder_name,balance=0.0):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.balance=float(balance)


2.Define Bank Class:
Create a Bank class that manages a list of accounts.
Include methods to add an account, check balance, deposit money, and withdraw money.


class Account:
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = float(balance)

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account_number, account_holder_name, initial_balance=0.0):
        # Check if account_number already exists
        if any(account.account_number == account_number for account in self.accounts):
            print(f"Account number '{account_number}' already exists.")
            return
        account = Account(account_number, account_holder_name, initial_balance)
        self.accounts.append(account)
        print(f"Account '{account_number}' for {account_holder_name} added with balance {initial_balance:.2f}.")

    def check_balance(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                print(f"Account '{account_number}' balance: {account.balance:.2f}")
                return
        print(f"Account number '{account_number}' not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        for account in self.accounts:
            if account.account_number == account_number:
                account.balance += float(amount)
                print(f"Deposited {amount:.2f} to account '{account_number}'. New balance: {account.balance:.2f}")
                return
        print(f"Account number '{account_number}' not found.")

    def withdraw(self, account_number, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        for account in self.accounts:
            if account.account_number == account_number:
                if account.balance >= amount:
                    account.balance -= float(amount)
                    print(f"Withdrew {amount:.2f} from account '{account_number}'. New balance: {account.balance:.2f}")
                else:
                    print(f"Insufficient balance in account '{account_number}'. Current balance: {account.balance:.2f}")
                return
        print(f"Account number '{account_number}' not found.")


3.Create Main Program:
Develop a CLI to interact with the Banking system.
Include options to add accounts, check balance, deposit money, and withdraw money.


class Account:
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = float(balance)

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account_number, account_holder_name, initial_balance=0.0):
        if any(account.account_number == account_number for account in self.accounts):
            print(f"Account number '{account_number}' already exists.")
            return
        account = Account(account_number, account_holder_name, initial_balance)
        self.accounts.append(account)
        print(f"Account '{account_number}' for {account_holder_name} added with balance {initial_balance:.2f}.")

    def check_balance(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                print(f"Account '{account_number}' balance: {account.balance:.2f}")
                return
        print(f"Account number '{account_number}' not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        for account in self.accounts:
            if account.account_number == account_number:
                account.balance += float(amount)
                print(f"Deposited {amount:.2f} to account '{account_number}'. New balance: {account.balance:.2f}")
                return
        print(f"Account number '{account_number}' not found.")

    def withdraw(self, account_number, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        for account in self.accounts:
            if account.account_number == account_number:
                if account.balance >= amount:
                    account.balance -= float(amount)
                    print(f"Withdrew {amount:.2f} from account '{account_number}'. New balance: {account.balance:.2f}")
                else:
                    print(f"Insufficient balance in account '{account_number}'. Current balance: {account.balance:.2f}")
                return
        print(f"Account number '{account_number}' not found.")

def main():
    bank = Bank()
    while True:
        print("\nBanking System Menu:")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            try:
                initial_balance = input("Enter initial balance (default 0.0): ")
                initial_balance = float(initial_balance) if initial_balance.strip() else 0.0
                if initial_balance < 0:
                    print("Initial balance cannot be negative.")
                else:
                    bank.add_account(account_number, account_holder_name, initial_balance)
            except ValueError:
                print("Please enter a valid number for initial balance.")
        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(account_number, amount)
            except ValueError:
                print("Please enter a valid number for deposit amount.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(account_number, amount)
            except ValueError:
                print("Please enter a valid number for withdrawal amount.")
        elif choice == "5":
            print("Exiting Banking System.")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()


4.Enhance Banking System:
Add functionality to transfer money between accounts, display account details, and handle account overdrafts.


class Account:
    def __init__(self, account_number, account_holder_name, balance=0.0, overdraft_limit=0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = float(balance)
        self.overdraft_limit = float(overdraft_limit)

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account_number, account_holder_name, initial_balance=0.0, overdraft_limit=0.0):
        if any(account.account_number == account_number for account in self.accounts):
            print(f"Account number '{account_number}' already exists.")
            return
        account = Account(account_number, account_holder_name, initial_balance, overdraft_limit)
        self.accounts.append(account)
        print(f"Account '{account_number}' for {account_holder_name} added with balance {initial_balance:.2f} and overdraft limit {overdraft_limit:.2f}.")

    def check_balance(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                print(f"Account '{account_number}' balance: {account.balance:.2f}")
                return
        print(f"Account number '{account_number}' not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        for account in self.accounts:
            if account.account_number == account_number:
                account.balance += float(amount)
                print(f"Deposited {amount:.2f} to account '{account_number}'. New balance: {account.balance:.2f}")
                return
        print(f"Account number '{account_number}' not found.")

    def withdraw(self, account_number, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        for account in self.accounts:
            if account.account_number == account_number:
                if account.balance - amount >= -account.overdraft_limit:
                    account.balance -= float(amount)
                    print(f"Withdrew {amount:.2f} from account '{account_number}'. New balance: {account.balance:.2f}")
                else:
                    print(f"Insufficient funds in account '{account_number}'. Current balance: {account.balance:.2f}, Overdraft limit: {account.overdraft_limit:.2f}")
                return
        print(f"Account number '{account_number}' not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        from_account = None
        to_account = None
        for account in self.accounts:
            if account.account_number == from_account_number:
                from_account = account
            elif account.account_number == to_account_number:
                to_account = account
        if not from_account:
            print(f"From account '{from_account_number}' not found.")
            return
        if not to_account:
            print(f"To account '{to_account_number}' not found.")
            return
        if from_account.balance - amount >= -from_account.overdraft_limit:
            from_account.balance -= float(amount)
            to_account.balance += float(amount)
            print(f"Transferred {amount:.2f} from '{from_account_number}' to '{to_account_number}'.")
            print(f"New balance for '{from_account_number}': {from_account.balance:.2f}")
            print(f"New balance for '{to_account_number}': {to_account.balance:.2f}")
        else:
            print(f"Insufficient funds in account '{from_account_number}'. Current balance: {from_account.balance:.2f}, Overdraft limit: {from_account.overdraft_limit:.2f}")

    def display_account_details(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                print(f"Account Details:")
                print(f"Account Number: {account.account_number}")
                print(f"Account Holder: {account.account_holder_name}")
                print(f"Balance: {account.balance:.2f}")
                print(f"Overdraft Limit: {account.overdraft_limit:.2f}")
                return
        print(f"Account number '{account_number}' not found.")

def main():
    bank = Bank()
    while True:
        print("\nBanking System Menu:")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            try:
                initial_balance = input("Enter initial balance (default 0.0): ")
                initial_balance = float(initial_balance) if initial_balance.strip() else 0.0
                overdraft_limit = input("Enter overdraft limit (default 0.0): ")
                overdraft_limit = float(overdraft_limit) if overdraft_limit.strip() else 0.0
                if initial_balance < 0:
                    print("Initial balance cannot be negative.")
                elif overdraft_limit < 0:
                    print("Overdraft limit cannot be negative.")
                else:
                    bank.add_account(account_number, account_holder_name, initial_balance, overdraft_limit)
            except ValueError:
                print("Please enter valid numbers for balance and overdraft limit.")
        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(account_number, amount)
            except ValueError:
                print("Please enter a valid number for deposit amount.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(account_number, amount)
            except ValueError:
                print("Please enter a valid number for withdrawal amount.")
        elif choice == "5":
            from_account_number = input("Enter from account number: ")
            to_account_number = input("Enter to account number: ")
            try:
                amount = float(input("Enter amount to transfer: "))
                bank.transfer(from_account_number, to_account_number, amount)
            except ValueError:
                print("Please enter a valid number for transfer amount.")
        elif choice == "6":
            account_number = input("Enter account number: ")
            bank.display_account_details(account_number)
        elif choice == "7":
            print("Exiting Banking System.")
            break
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()

5.Test the Application:
Create instances of accounts and test the functionality of your Banking system.

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds for withdrawal.")

    def get_balance(self):
        return self.balance
