import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":

    user_manager = UserManager()
    add_user = user_manager.add_user
    get_all_names = user_manager.get_all_names

    for i in range(266):
        user_manager.add_user(i, f"User{i}")
    
    print("end")
    # print("Average user ID:", user_manager.average_user_id())
    # Simulate adding users
    # Uncomment the following lines to test adding users


        

    
    # add_user(1, "Alice")
    # add_user(2, "Bob")
    # add_user(3, "Charlie")
    # add_user(4, "David")
    # add_user(5, "Eve") ``

    # print("All user IDs:", get_all_names())
