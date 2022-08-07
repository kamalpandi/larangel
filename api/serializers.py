from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Admin, User, turfDetails, turfImages
from django.contrib.auth import get_user_model
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth.hashers import make_password



#"create_user": "http://127.0.0.1:8000/crud_user/",
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',            
        ]

#"create_admin": "http://127.0.0.1:8000/crud_admin/", 
class AdminSerializer(serializers.ModelSerializer):
    userName =serializers.CharField(source='user.username',read_only=True)
    #user = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = Admin
        fields = ['userName','id','firstName','lastName','mobileNumber','email','dateOfBirth','gender','address','pincode','user']

class TurfDetailsSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='admin.firstName',read_only=True)
    class Meta:
        model = turfDetails
        fields = '__all__' #['images','id','firstName','turfName','mobileNumber','openingTime','cloasingTime','addressOfTurf','aminities','admin',]
        
class TurfImageSerializer(serializers.ModelSerializer):
    #generalTurfImages =serializers.ImageField()
    turfName = serializers.CharField(source='turfDetails.turfName',read_only=True)
    #turfDetails = serializers.CharField(source='turfDetails.id',read_only=True)
    class Meta:
        model = turfImages
        fields = '__all__' #['id','turfDetails','generalTurfImages','turfName']


    # def create(self, validated_data):

    #     return turfImages.objects.create(validated_data)
    # def update(self, validated_data):
    #     return turfImages.objects.update(validated_data)



# #"list_user_admin": "http://127.0.0.1:8000/list_user_admin/"
# class AdminListSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
#     class Meta:
#         model = Admin
#         fields = ['user','firstName','lastName','mobileNumber','dateOfBirth','gender','address','pincode']

# class UserListSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
#     username = serializers.CharField(read_only=True)
#     email = serializers.CharField(read_only=True)
#     admin = AdminListSerializer()
#     class Meta:
#         model = User
#         fields = [
#             'id',
#             'username',
#             'email',
#             'admin',
#         ]

#use this to exclude the password(also add other fields too) retrived from db #https://www.abheist.com/django-hide-serializer-depth-fields/
# class UserPassSerializer(serializers.ModelSerializer):
#     username =serializers.CharField(read_only=True)
#     class Meta:
#         model = get_user_model()
#         exclude =['password','last_login','first_name','last_name','is_staff','is_active','groups','user_permissions','is_superuser','date_joined','email']
    
# class AdminSerializer(serializers.ModelSerializer):
#     #user = UserPassSerializer()    
#     name = serializers.CharField(source='user.username',read_only=True)
#     uid = serializers.CharField(source='user.id',read_only=True)
#     # 'uid','name','user',
#     class Meta:
#         model = Admin
#         fields = ['uid','name','id','firstName','lastName','mobileNumber','dateOfBirth','gender','address','pincode']
#         depth = 1