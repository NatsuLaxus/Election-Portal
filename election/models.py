from django.db import models
from django.contrib.auth.models import User


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    session = models.ForeignKey('Election', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'candidate'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Election(models.Model):
    faculty = models.ForeignKey(AuthUser, models.CASCADE)
    session_id = models.AutoField(primary_key=True)
    post = models.CharField(max_length=20)
    year = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'election'


# class Faculty(models.Model):
#     faculty = models.OneToOneField(AuthUser,models.CASCADE)
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     phone = models.IntegerField()
#     email = models.CharField(max_length=60)

#     class Meta:
#         managed = False
#         db_table = 'faculty'


class Result(models.Model):
    user = models.ForeignKey(AuthUser, models.SET_NULL,null=True)
    session_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'result'


class Student(models.Model):
    student = models.OneToOneField(AuthUser,models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.IntegerField()
    email = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'student'


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=100)
#     isAdmin = models.IntegerField(db_column='isAdmin')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'user'


class Vote(models.Model):
    reference_no = models.AutoField(primary_key=True)
    session = models.ForeignKey(Election, models.CASCADE)
    hashed_value = models.CharField(max_length=100)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vote'
