from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, SmallInteger, DateTime, TIMESTAMP,Boolean
from src.models.shared import db

class User (db.Model):
    __tablename__ = "user"
    id = Column (Integer, primary_key=True, autoincrement=True, nullable=False)
    username= Column (String(255), nullable=False)
    full_name= Column (String(255), nullable=False)
    email= Column (String(255), nullable=False)
    phone_number= Column (String(255))
    report_access= Column (Boolean )
    view_costs= Column (Boolean )
    last_login_date= Column (TIMESTAMP)
    enabled = Column(Boolean, nullable=False)
    is_corporated= Column (Boolean, nullable=False)
    created_on= Column (DateTime)
    modified_on = Column(DateTime)

    def __repr__(self) -> str:
        return '<User {}>'.format(self.username)   
   

