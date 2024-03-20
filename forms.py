from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional

from flask_app import Employer, Employee


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Log in")


class SearchForm(FlaskForm):
    search = StringField("Search", validators=[DataRequired()])
    submit = SubmitField("Search")


class NewEmployerForm(FlaskForm):
    employer_name = StringField("Employer Name", validators=[DataRequired()])
    headquarters_address = StringField('Headquarters Address', validators=[DataRequired()])
    description = StringField('Description', validators=[Optional()])
    start_date = DateField('Start Date', validators=[DataRequired()], format='%Y-%m-%d')
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Add Employer')


class EditEmployerForm(FlaskForm):
    employer_name = StringField("Employer Name", validators=[DataRequired()])
    headquarters_address = StringField('Headquarters Address', validators=[Optional()])
    description = StringField('Description', validators=[Optional()])
    start_date = DateField('Start Date', validators=[Optional()], format='%Y-%m-%d')
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Edit Employer')


class DeleteEmployerForm(FlaskForm):
    employer_name = StringField("Employer Name", validators=[DataRequired()])
    submit = SubmitField('Delete Employer')


class RelationForm(FlaskForm):
    parent_name = StringField("Parent Name", validators=[DataRequired()])
    child_name = StringField('Child Name', validators=[DataRequired()])
    submit = SubmitField('Add Relation')


class AddAdminForm(FlaskForm):
    email_address = StringField("Email Address", validators=[DataRequired()])
    submit = SubmitField("Create Admin")


class AddEmployeeForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired(), Length(min=10, max=15)])
    employee_address = StringField("Address", validators=[DataRequired()])
    email_address = StringField("Email Address", validators=[DataRequired(), Email()])
    submit = SubmitField("Add Employee")


class EditEmployeeForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired(), Length(min=10, max=15)])
    employee_address = StringField("Address", validators=[DataRequired()])
    email_address = StringField("Email Address", validators=[DataRequired(), Email()])
    submit = SubmitField("Edit Employee")


class DeleteEmployeeForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Delete Employee")


class RecordNewJobForm(FlaskForm):
    employee_id = SelectField("Employee", choices=[(employee.id, f"{employee.first_name} {employee.last_name}") for employee in Employee.query.order_by(Employee.first_name).all()], coerce=int, validators=[DataRequired()])
    employer_id = SelectField("Employer", choices=[(employer.id, employer.employer_name) for employer in Employer.query.order_by(Employer.employer_name).all()], coerce=int, validators=[DataRequired()])
    jobTitle = StringField("Job Title", validators=[DataRequired()])
    startDate = DateField("Start Date", validators=[DataRequired()], format='%Y-%m-%d')
    endDate = DateField("End Date", validators=[Optional()], format='%Y-%m-%d')
    submit = SubmitField("Record Job")


#              NEED TO ADD THE FOLLOWING FORMS
# 1. AddDegreeOrCertification
# 2. RemoveEmployeeForm (I am not sure if you really need this or not. I would think you would need this form
# to select which employee to remove.)
# 3.