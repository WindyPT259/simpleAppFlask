from src.models.users import User

def home ():
    return "hello Thẽo thẽo"
def get_list ():
    users = User.query.all()
    print(users)
    return {
        "avatar": "user.avatar",
        "email": "user.email"
    }
