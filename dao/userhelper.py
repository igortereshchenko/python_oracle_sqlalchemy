from dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def getSkillData(self, skill_name=None):

        if skill_name:
            skill_name="'{0}'".format(skill_name)
        else:
            skill_name='null'

        query = "select * from table(orm_user_skillS.GetSkillData({0}))".format(skill_name)

        result = self.db.execute(query)
        return result.fetchall()




if __name__ == "__main__":

    helper = UserHelper()

    print(helper.getSkillData('Java'))
    print(helper.getSkillData())
