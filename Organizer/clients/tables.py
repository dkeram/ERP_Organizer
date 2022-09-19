from django_tables2 import tables , TemplateColumn , CheckBoxColumn
from .models import Clients

class ListClient(tables.Table):
    selection = CheckBoxColumn(accessor = 'pk')
    #edit = TemplateColumn(template_name="django_tables2/bootstrap4.html")
    class Meta:
        model = Clients
        template_name = "django_tables2/bootstrap4.html"
        fields = ('sirname', 'name','vat','phone','email','address')