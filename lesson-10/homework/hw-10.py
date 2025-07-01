class Task:
    def __init__(self, title, description, due_date, status=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        status_str = "Completed" if self.status else "Incomplete"
        return f"{self.title} | {self.description} | Due: {self.due_date} | Status: {status_str}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.status = True
                return f"Task '{task_title}' marked as complete."
        return f"Task '{task_title}' not found."

    def list_all_tasks(self):
        return [str(task) for task in self.tasks]

    def display_incomplete_tasks(self):
        return [str(task) for task in self.tasks if not task.status]

# Main CLI
def main():
    todo = ToDoList()
    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Display Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Task title: ")
            desc = input("Description: ")
            due = input("Due date: ")
            task = Task(title, desc, due)
            todo.add_task(task)
            print("Task added.")

        elif choice == '2':
            title = input("Task title to mark complete: ")
            print(todo.mark_complete(title))

        elif choice == '3':
            for t in todo.list_all_tasks():
                print(t)

        elif choice == '4':
            for t in todo.display_incomplete_tasks():
                print(t)

        elif choice == '5':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


























class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author}\n{self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        return [str(post) for post in self.posts]

    def display_posts_by_author(self, author):
        return [str(post) for post in self.posts if post.author == author]

    def delete_post(self, title):
        for i, post in enumerate(self.posts):
            if post.title == title:
                del self.posts[i]
                return f"Post '{title}' deleted."
        return f"Post '{title}' not found."

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                return f"Post '{title}' updated."
        return f"Post '{title}' not found."

    def display_latest_posts(self, count=5):
        return [str(post) for post in self.posts[-count:]]

# Main CLI
def main():
    blog = Blog()
    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Post title: ")
            content = input("Content: ")
            author = input("Author: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added.")

        elif choice == '2':
            for p in blog.list_all_posts():
                print(p)

        elif choice == '3':
            author = input("Author name: ")
            for p in blog.display_posts_by_author(author):
                print(p)

        elif choice == '4':
            title = input("Title of post to delete: ")
            print(blog.delete_post(title))

        elif choice == '5':
            title = input("Title of post to edit: ")
            new_content = input("New content: ")
            print(blog.edit_post(title, new_content))

        elif choice == '6':
            count = int(input("How many latest posts to display? "))
            for p in blog.display_latest_posts(count):
                print(p)

        elif choice == '7':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

























class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def __str__(self):
        return f"Account: {self.account_number} | Holder: {self.holder_name} | Balance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, acc_num):
        for acc in self.accounts:
            if acc.account_number == acc_num:
                return acc
        return None

    def check_balance(self, acc_num):
        acc = self.find_account(acc_num)
        return acc.balance if acc else "Account not found."

    def deposit(self, acc_num, amount):
        acc = self.find_account(acc_num)
        if acc:
            acc.balance += amount
            return f"Deposited {amount}. New balance: {acc.balance}"
        return "Account not found."

    def withdraw(self, acc_num, amount):
        acc = self.find_account(acc_num)
        if acc:
            if acc.balance >= amount:
                acc.balance -= amount
                return f"Withdrawn {amount}. New balance: {acc.balance}"
            else:
                return "Insufficient balance."
        return "Account not found."

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)
        if from_acc and to_acc:
            if from_acc.balance >= amount:
                from_acc.balance -= amount
                to_acc.balance += amount
                return f"Transferred {amount} from {from_acc_num} to {to_acc_num}."
            else:
                return "Insufficient balance to transfer."
        return "One or both accounts not found."

# Main CLI
def main():
    bank = Bank()
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            acc_num = input("Account number: ")
            holder = input("Account holder name: ")
            acc = Account(acc_num, holder)
            bank.add_account(acc)
            print("Account added.")

        elif choice == '2':
            acc_num = input("Account number: ")
            print("Balance:", bank.check_balance(acc_num))

        elif choice == '3':
            acc_num = input("Account number: ")
            amount = float(input("Amount to deposit: "))
            print(bank.deposit(acc_num, amount))

        elif choice == '4':
            acc_num = input("Account number: ")
            amount = float(input("Amount to withdraw: "))
            print(bank.withdraw(acc_num, amount))

        elif choice == '5':
            from_acc = input("From account number: ")
            to_acc = input("To account number: ")
            amount = float(input("Amount to transfer: "))
            print(bank.transfer(from_acc, to_acc, amount))

        elif choice == '6':
            for acc in bank.accounts:
                print(acc)

        elif choice == '7':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
