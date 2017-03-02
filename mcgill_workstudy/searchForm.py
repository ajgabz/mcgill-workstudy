#from flask_wtf import FlaskForm
from wtforms import Form, Field, IntegerField, StringField, SelectField, DateField, validators

class WorkstudySearchForm(Form):
    student_id = IntegerField('studentID', validators = [validators.optional()])
    faculty_id = StringField('facultyID', validators = [validators.optional(), validators.regexp('[A-Za-z]{2}')])
    semester_term = SelectField('semesterTerm', choices=[('Fall', 'Fall'), ('Winter', 'Winter'), ('Summer', 'Summer')]
                                , validators = [validators.optional(), validators.AnyOf(values=['Fall', 'Winter', 'Summer'])])
    term_year = IntegerField('termYear', validators = [validators.optional(), validators.number_range(1950, 2100)])
    applicationdecision = SelectField('applicationDecision', choices=[('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Refused', 'Refused'), ('Revoked', 'Revoked')],
                           validators = [validators.optional(), validators.AnyOf(values=['Accepted', 'Pending', 'Refused', 'Revoked'])])


    #This method MUST ONLY be called after verification.
    def construct_query(self):
        filled_dict = {k:v for k,v in self.data.iteritems() if not(v == "" or v == "None" or v is None)} #Dictionary, whose keys have non-empty values
        query_opening = "SELECT * FROM Application"
        query_sorting = " ORDER BY studentid, termyear, semesterterm"
        query_filters = []
        parameters = []

        for filterKey in filled_dict:
            query_filters.append("(" + filterKey + " = (%s))")
            parameters.append(filled_dict.get(filterKey))

        if len(query_filters) == 0:
            return (query_opening + query_sorting, None)
        elif len(query_filters) == 1:
            query = query_opening + " WHERE " + query_filters[0] + query_sorting
            return (query, parameters)
        else:
            query = query_opening + " WHERE " + query_filters[0] + " AND " + " AND ".join(query_filters[1:]) + query_sorting
            return (query, parameters)


def construct_single_term_query(table, parameter):
    single_term_query = "SELECT * FROM Application WHERE %s = (%s) ORDER BY studentid, termyear, semesterterm"
    return (single_term_query % (table, "%s"), [parameter])