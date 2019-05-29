from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class ormUser(Base):
    __tablename__ = 'orm_user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False)
    user_studybook = Column(String(6), nullable=False)
    user_email = Column(String(40))
    user_year = Column(Date, nullable=False)
    user_birthday = Column(Date, nullable=False)

    orm_skills = relationship('ormSkill', secondary='orm_user_skill')


class ormSkill(Base):
    __tablename__ = 'orm_skill'
    skill_name = Column(String(40), primary_key=True)

    orm_users = relationship('ormUser', secondary='orm_user_skill')


class ormUserSkill(Base):
    __tablename__ = 'orm_user_skill'

    user_id = Column(Integer,ForeignKey('orm_user.user_id'),primary_key = True)
    skill_name = Column(String(40), ForeignKey('orm_skill.skill_name'), primary_key=True)




