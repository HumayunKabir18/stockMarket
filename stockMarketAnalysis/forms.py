#for learning perpose
from django import forms
from .models import stock_market_data
class addnew_form(forms.ModelForm):
    class Meta:
        model= stock_market_data
        fields=['date','trade_code','high','low','open','close','volume']
        def __init__(self,*args,**kwargs):
            super(addnew_form,self).__init__(*args,**kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class']='form-control'

                