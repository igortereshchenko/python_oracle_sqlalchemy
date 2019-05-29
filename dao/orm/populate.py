from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormUserSkill).delete()
session.query(ormSkill).delete()
session.query(ormUser).delete()


# populate database with new rows

Bob = ormUser( user_name="Bob",
               user_birthday='10-OCT-2000',
               user_email='bob@gmail.com',
               user_studybook='KM1111',
               user_year='10-SEP-2010',
               )



Boba = ormUser( user_name="Boba",
               user_birthday='10-OCT-2001',
               user_email='boba@gmail.com',
               user_studybook='KM2222',
               user_year='10-OCT-2010',
               )


Boban = ormUser( user_name="Boban",
               user_birthday='10-OCT-2001',
               user_email='boba@gmail.com',
               user_studybook='KM2222',
               user_year='10-OCT-2010',
               )



Java = ormSkill(skill_name='Java')
Oracle = ormSkill(skill_name='Oracle')

# create relations
Bob.orm_skills.append(Java)
Bob.orm_skills.append(Oracle)

Boba.orm_skills.append(Java)

Boban.orm_skills.append(Oracle)

# insert into database
session.add_all([Java,Oracle,Boban,Boba,Bob])

session.commit()