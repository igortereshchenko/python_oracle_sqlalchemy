from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError
from dao.db import OracleDb
from dao.userhelper import UserHelper
class SearchForm(Form):

    skill_name = StringField('Skill name: ')
    submit = SubmitField('Search')


    def get_result(self):
        helper = UserHelper()
        return helper.getSkillData(self.skill_name.data)


