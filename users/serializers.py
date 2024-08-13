from rest_framework import serializers
from .models import User
import re
from django.core.validators import validate_email

class UserCreateSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(required=True)


    class Meta:
        model = User
        fields=['name', 'email', 'password']

    def has_lowercase(self, password):
        pattern = r'[a-z]'
        return bool(re.search(pattern, password))
    

    def has_uppercase(self, password):
        pattern = r'[A-Z]'
        return bool(re.search(pattern, password))
    
    def is_valid_email(self, email):
        try:
            validate_email(email)
            return True
        except:
            return False



    def validate(self, data):
        if len(data['name'])  < 4:
            raise serializers.ValidationError("Name must contain atleast 4 characters.")
        if not self.is_valid_email(data['email']):
            raise serializers.ValidationError("Email must be a valid email.")
        if data['password'] == "":
            raise serializers.ValidationError("Password cannot be left empty.")
        if len(data['password']) < 8:
            raise serializers.ValidationError("Minimum Password length is 8.")
        if not self.has_uppercase(data['password']):
            raise serializers.ValidationError("Password must contain atleast one Uppercase alphabet.")
        if not self.has_lowercase(data['password']):
            raise serializers.ValidationError("Password must contain aleast one Lowercase alphabet.")
        
        return super().validate(data)
    
class VerifyOtpSerializer(serializers.ModelSerializer):
    otp=serializers.CharField(required=True)
    email=serializers.EmailField(max_length=100)

    def is_valid_email(self, email):
        try:
            validate_email(email)
            return True
        except:
            return False

    def validate(self, data):
        if not self.is_valid_email(data['email']):
            raise serializers.ValidationError("Email must be a valid email.")
        if data['otp'] == "":
            raise serializers.ValidationError("Otp cannot be left empty.")
        if len(data['otp']) < 6 or len(data['otp']) > 6:
            raise serializers.ValidationError("Otp must contain 6 numbers.")
        
        return super().validate(data)
        
    class Meta:
        model=User
        fields=['email', 'otp']
        
class RegenerateOtpSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=100)

    class Meta:
        model=User
        fields=['email']

class ForgotPasswordSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=100)

    class Meta:
        model=User
        fields=['email']

class VerifyForgotOtpSerializer(serializers.ModelSerializer):
    otp=serializers.CharField(required=True)
    email=serializers.EmailField(max_length=100)

    def is_valid_email(self, email):
        try:
            validate_email(email)
            return True
        except:
            return False

    def validate(self, data):
        if not self.is_valid_email(data['email']):
            raise serializers.ValidationError("Email must be a valid email.")
        if data['otp'] == "":
            raise serializers.ValidationError("Otp cannot be left empty.")
        if len(data['otp']) < 6 or len(data['otp']) > 6:
            raise serializers.ValidationError("Otp must contain 6 numbers.")
        
        return super().validate(data)
        
    class Meta:
        model=User
        fields=['email', 'otp']
    
class ValidateTokenSerializer(serializers.ModelSerializer):
    token=serializers.CharField(required=True)

    class Meta:
        model = User
        fields=['token']
    
    def validate(self, attrs):
        if (attrs['token'] == "" or attrs['token'] == None):
            raise serializers.ValidationError("Token is required.")
        return super().validate(attrs)
    
class ChangePasswordSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=100)
    password = serializers.CharField(required=True)
    otp = serializers.CharField(required=True)

    class Meta:
        model = User
        fields=['email', 'otp', 'password']

    def has_lowercase(self, password):
        pattern = r'[a-z]'
        return bool(re.search(pattern, password))
    

    def has_uppercase(self, password):
        pattern = r'[A-Z]'
        return bool(re.search(pattern, password))
    
    def validate(self, data):
        
        if data['password'] == "":
            raise serializers.ValidationError("Password cannot be left empty.")
        if len(data['password']) < 8:
            raise serializers.ValidationError("Minimum Password length is 8.")
        if not self.has_uppercase(data['password']):
            raise serializers.ValidationError("Password must contain atleast one Uppercase alphabet.")
        if not self.has_lowercase(data['password']):
            raise serializers.ValidationError("Password must contain aleast one Lowercase alphabet.")
        if data['otp'] == "":
            raise serializers.ValidationError("Otp cannot be left empty.")
        if len(data['otp']) < 6 or len(data['otp']) > 6:
            raise serializers.ValidationError("Otp must contain 6 numbers.")
        
        return super().validate(data)
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(required=True)


    class Meta:
        model = User
        fields=['email', 'password']

    def has_lowercase(self, password):
        pattern = r'[a-z]'
        return bool(re.search(pattern, password))
    

    def has_uppercase(self, password):
        pattern = r'[A-Z]'
        return bool(re.search(pattern, password))
    
    def is_valid_email(self, email):
        try:
            validate_email(email)
            return True
        except:
            return False



    def validate(self, data):
        if not self.is_valid_email(data['email']):
            raise serializers.ValidationError("Email must be a valid email.")
        if data['password'] == "":
            raise serializers.ValidationError("Password cannot be left empty.")
        if len(data['password']) < 8:
            raise serializers.ValidationError("Minimum Password length is 8.")
        if not self.has_uppercase(data['password']):
            raise serializers.ValidationError("Password must contain atleast one Uppercase alphabet.")
        if not self.has_lowercase(data['password']):
            raise serializers.ValidationError("Password must contain aleast one Lowercase alphabet.")
        
        return super().validate(data)    

class LogoutSerializer(serializers.ModelSerializer):
    token=serializers.CharField(required=True)

    class Meta:
        model = User
        fields=['token']
    
    def validate(self, attrs):
        if (attrs['token'] == "" or attrs['token'] == None):
            raise serializers.ValidationError("Token is required.")
        return super().validate(attrs)