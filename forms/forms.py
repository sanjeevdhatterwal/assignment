# from django import forms
# from .models import Video
# class FileForm(forms.ModelForm):
#     class Meta:
#         model= Video
#         fields= ["name", "filepath"]
# class VideoForm(forms.ModelForm):
#     class Meta:
#         model= Video
#         fields= ["name", "Video"]
from django import forms
from .models import Video


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ["videofile"]