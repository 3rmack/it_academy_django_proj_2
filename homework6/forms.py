from django import forms


class SectionForm(forms.Form):
    section_header = forms.CharField(max_length=100)
    age_qualification = forms.IntegerField(min_value=0, max_value=100)


class ArticleForm(forms.Form):
    article_header = forms.CharField(max_length=100)
    contents = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)


# class ConnectionsForm(forms.Form):
#     article = forms
#     section = models.ForeignKey(Sections)
