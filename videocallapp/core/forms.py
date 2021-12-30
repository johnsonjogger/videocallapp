from django import forms




class LizzyForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    class Meta:
        fields = ('email', 'first_name', 'last_name')
        
        
        
        
class NadiaForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    class Meta:
        fields = ('email', 'first_name', 'last_name')