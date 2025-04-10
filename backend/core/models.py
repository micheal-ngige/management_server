import uuid
from django.db import models


def generate_uuid():
    return str(uuid.uuid4())


class Department(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    name = models.CharField(max_length=255)


class HRPersonel(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    personal_no = models.CharField(max_length=10, unique=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='hr_personnels')


class Manager(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    personal_no = models.CharField(max_length=10, unique=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='managers')


class Employee(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    personal_no = models.CharField(max_length=10, unique=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')


class EmployeeProfile(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    date_of_birth = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mantra = models.TextField()
    phone_contact = models.BigIntegerField()
    profile_photo = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)


class ManagerProfile(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    date_of_birth = models.DateField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mantra = models.TextField()
    phone_contact = models.BigIntegerField()
    profile_photo = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)


class HrProfile(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    date_of_birth = models.DateField()
    hr_personnel = models.ForeignKey(HRPersonel, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mantra = models.TextField()
    phone_contact = models.BigIntegerField()
    profile_photo = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)


class Documents(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='documents')
    link_url = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=[('official', 'Official'), ('institution', 'Institution'), ('other', 'Other')])


class Remuneration(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    name = models.CharField(max_length=30)
    salary = models.FloatField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='remunerations')
    remuneration_date = models.DateTimeField(auto_now_add=True)


class RemunerationDescription(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    remuneration = models.ForeignKey(Remuneration, on_delete=models.CASCADE, related_name='descriptions')
    type = models.CharField(max_length=20, choices=[('deduction', 'Deduction'), ('bonus', 'Bonus'), ('allowance', 'Allowance'), ('normal', 'Normal')])
    name = models.CharField(max_length=30)
    description = models.TextField()
    amount = models.FloatField()


class Experience(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='experiences')
    name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Session(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    name = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Goals(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='goals')
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, default=None, related_name='overseen_goals')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='goals')
    name = models.CharField(max_length=30)
    description = models.TextField()


class Training(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    title = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateTimeField()
    start_time = models.TimeField()
    end_date = models.DateTimeField()
    end_time = models.TimeField()


class EmployeeTraining(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)


class Leave(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leaves')
    description = models.TextField()
    approved = models.BooleanField(default=False)


class LeaveApproval(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    leave = models.ForeignKey(Leave, on_delete=models.CASCADE, related_name='approvals')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    hr_personnel = models.ForeignKey(HRPersonel, on_delete=models.SET_NULL, null=True)
    approved_by_manager = models.BooleanField(default=False)
    approved_by_hr = models.BooleanField(default=False)
    manager_app_date = models.DateTimeField(null=True, blank=True)
    hr_approval_date = models.DateTimeField(null=True, blank=True)


class Education(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=36)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class TokenBlocklist(models.Model):
    id = models.AutoField(primary_key=True)
    jti = models.CharField(max_length=36, db_index=True)
    created_at = models.DateTimeField()
