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
    find_user = user_manager.find_user
    delete_user = user_manager.delete_user
    average_user_id = user_manager.average_user_id



    for i in range(266):
        user_manager.add_user(i, f"User{i}")
    
    print("end")


    # for i in range(266):
    #     user_manager.find_user(i)
    #     time.sleep(0.01)
    #     print("User found:", i)
    # print("end")
    

    for i in range(266):
        user_manager.delete_user(i)
        time.sleep(0.01)
        print("User deleted:", i)
        if i % 50 == 0:
            print("Current users:", get_all_names())
            print("Average user ID:", average_user_id())

    print("end")


    # for i in range(266):
    #     user_manager.find_user(i)
    #     time.sleep(0.01)
    #     print("User found:", i)
    # print("end")


