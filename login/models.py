from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

# Custom Manager for the model of Admin User 

class AdminUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo de email es obligatorio')
        
        email = self.normalize_email(email)
        user = self.model(email=semail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


# Custom Admin User model

class AdminUser(AbstractBaseUser):
    #Regex Validators
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,16}$',
        message="El número de teléfono debe tener el formato: '+573168456558'. Hasta 16 dígitos permitidos."
    )
    
    #Admin User fields

    first_name=models.CharField(max_length=50, null=False, blank=False)
    last_name=models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(unique=True)
    profile = models.CharField(max_length=100, null=False, blank=True)
    dni = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True)
    profile =models.CharField(max_length=15,null=False, blank=False)
    
    is_superuser=True
    is_active=True
    
    #Abstract Base User Fields
    USERNAME_FIELD = 'email'

    #Set the Manager
    objects = AdminUserManager()

    
    def __str__(self):
        return self.email