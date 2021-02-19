from wtforms import Form,StringField,InitgerField
form wtforms.validator import length,NumberRange
class SearchForm(form):
    q = StringField(validators=[length(min=1,max=30)])
    page = InitgerField(validators = [NumberRange(min=1,max=99)])