from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=10, required=True)
    phone = forms.CharField(max_length=11, required=False)
    skill = forms.CharField(max_length=10,required=False)
    file = forms.FileField()
    info = forms.CharField(max_length=100, required=True)

    def clean_info(self):
         info = self.cleaned_data['info']
         print(info.split())
         num_info = len(info.split())
         if num_info < 4:
             raise forms.ValidationError("Info not enough words!")
         return info


class UsersForm(forms.Form):
        name = forms.CharField(max_length=10, required=True)
        password = forms.CharField(max_length=12, required=True, widget=forms.PasswordInput)

##入数据库的
# class UserModeForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"
#         exclude = ['sex']