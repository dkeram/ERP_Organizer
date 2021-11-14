import django_tables2 as tables
from .models import Clients

class ListClient(tables.Table):
    selection = tables.CheckBoxColumn(accessor = 'pk')
    class Meta:
        model = Clients
        template_name = "django_tables2/bootstrap.html"
        fields = ('sirname', 'name','vat','phone','email','address','user_name','password')