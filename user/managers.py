from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, is_staff=False, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, is_staff=is_staff, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_user(self, username, password=None, **extra_fields):
        # extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        # extra_fields.setdefault('is_superuser', True)

        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, True, **extra_fields)