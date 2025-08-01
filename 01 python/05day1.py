import sys, json, os
DBFILE = "users.json"

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}
    

def load_users():
    if not os.path.exists(DBFILE):
        return []
    with open(DBFILE, "r") as f:
        return json.load(f)
    

def save_users(users):
    with open(DBFILE, "w") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)


def add_user(name, age):
    users = load_users()
    new_user = User(name, age)
    users.append(new_user.to_dict())
    save_users(users)
    print(f"User {name} added successfully.")

def list_users():
    users = load_users()
    for i, u in enumerate(users):
        print(f"{i+1}. {u['name']} - {u['age']}岁")

if len(sys.argv) < 2:
    print("Usage: python 05day1.py [add|list] [name] [age]")
    sys.exit(1)

cmd = sys.argv[1]
if cmd == "add" and len(sys.argv) == 4:
    name = sys.argv[2]
    age = sys.argv[3]
    add_user(name, age)
elif cmd == "list":
    list_users()
else:
    print("Invalid command or arguments.")
    print("Usage: python 05day1.py [add|list] [name] [age]")
    sys.exit(1)
    