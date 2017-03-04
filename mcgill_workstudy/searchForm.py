from wtforms import Form, Field, IntegerField, StringField, SelectField, DateField, validators


class WorkstudySearchForm(Form):
    student_id = IntegerField('studentID', validators = [validators.optional()])
    faculty_id = StringField('facultyID', validators = [validators.optional(), validators.regexp('[A-Za-z]{2}')])
    term_season = StringField('semesterTerm',
                               validators = [validators.optional(), validators.regexp('(?i)^fall|spring|summer|winter$')])
    term_year = IntegerField('termYear', validators = [validators.optional(), validators.number_range(1950, 2100)])
    status = StringField('applicationDecision',
                                      validators = [validators.optional(),
                                                    validators.regexp('(?i)^accepted|pending|refused|revoked$')])


    #This method MUST ONLY be called after verification.
    def get_search_form_data(self):
        # Dictionary, whose keys have non-empty (or filled) values
        filled_dict = {k:v for k,v in self.data.iteritems() if not(v == "" or v == "None" or v is None)}
        return filled_dict


