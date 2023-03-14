from main_thao import celery
from datetime import datetime
from src.models.users import UserApp
from src.models.shared import db
from main_thao import app


# task một decorator để định nghĩa một task trong Celery.
@celery.task(bind=True, max_retries=3)
def update_last_login(self):
    with app.app_context():
        try:
            users = UserApp.query.all()
            for user in users:
                user.last_login_date = datetime.now()
                db.session.add(user)
            db.session.commit()
            return print("Updated last login time for user ")
        except Exception as e:
            # Retry task nếu có lỗi xảy ra
            self.retry(exc=e)
            return print("ERROR")
