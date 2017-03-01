from flask_wtf import FlaskForm
from wtforms import Form, Field, IntegerField, StringField, SelectField, DateField, validators

class WorkstudySearchForm(Form):
    student_id = IntegerField('studentID', validators = [validators.optional()])
    faculty_id = StringField('facultyID', validators = [validators.optional(), validators.regexp('[A-Za-z]{2}')])
    semester_term = SelectField('semesterTerm', choices=[('Fall', 'Fall'), ('Winter', 'Winter'), ('Summer', 'Summer')]
                                , validators = [validators.optional(), validators.AnyOf(values=['Fall', 'Winter', 'Summer'])])
    term_year = IntegerField('termYear', validators = [validators.optional(), validators.number_range(1950, 2100)])
    decision = SelectField('applicationDecision', choices=[('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Refused', 'Refused'), ('Revoked', 'Revoked')],
                           validators = [validators.optional(), validators.AnyOf(values=['Accepted', 'Pending', 'Refused', 'Revoked'])])


    #This method MUST ONLY be called after verification.
    def construct_query(self):
        filled_dict = {k:v for k,v in self.data.iteritems() if not(v == "" or v is None)} #Dictionary, whose keys have non-empty values
        query_opening = "SELECT * FROM Application"
        query_filters = []
        parameters = []

        for filterKey in filled_dict:
            query_filters.append("(" + filterKey + " = ?)")
            parameters.append(filled_dict.get(filterKey))

        if len(query_filters) == 0:
            return (query_opening, None)
        elif len(query_filters) == 1:
            query = query_opening + " WHERE " + query_filters[0]
            return (query, parameters)
        else:
            query = query_opening + " WHERE " + query_filters[0] + " AND " + " AND ".join(query_filters[1:])
            return (query, parameters)


class SearchQuery:
    """ Represents a simple SQL search query on the Application table
        The use of each parameter constitutes an additional filter,
        whereby the filters are combined via conjunction. """

    query_opening = "SELECT * FROM application"

    def __init__(self, student_id = None,  ):
