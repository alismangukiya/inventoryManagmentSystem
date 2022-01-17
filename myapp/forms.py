from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from myapp.models import Item,record

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name')

class Items(ModelForm):
    class Meta:
        model=Item
        fields=('itemName','itemDesc','Category','sellPrice','quantity','username')
        # # labels={
        # #     'itemName' : 'Item Name',
        # #     'itemDesc' : 'Item Description',
        # #     'sellPrice': 'Selling Price per unit', 
        # #     'quantity': 'Total Quantity', 
        # # }
        # def __init__(self,*args, **kwargs):
            # super(Items,self).__init__(*args,**kwargs)
            # self.fields["username"].empty_label="select"
class Records(ModelForm):
    class Meta:
        model=record
        fields=('itemId','itemName','itemDesc','amount','quantity','username','customerName','phone')
        