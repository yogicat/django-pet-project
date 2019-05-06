from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, name, phone, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, name, phone,  **extra_fields):

        user = self.create_user(email=email, name=name,
                                phone=phone, **extra_fields)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        # user.is_active = True
        # user.is_staff = True
        # user.is_superuser = True
        # user.set_password(password)
        # user.save(using=self._db)
        # return user
        return self.create_user(email, password, name, phone, **extra_fields)
