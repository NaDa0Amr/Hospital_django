# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admission(models.Model):
    admission_id = models.AutoField(primary_key=True)
    admission_in_date = models.DateTimeField(blank=True, null=True)
    admission_out_date = models.DateTimeField(blank=True, null=True)
    admission_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                        null=True)
    room_number = models.ForeignKey('Room', models.DO_NOTHING, db_column='room_number', blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Admission'


class Appointment(models.Model):
    appointment_id = models.AutoField(db_column='Appointment_id', primary_key=True)  # Field name made lowercase.
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    physician = models.ForeignKey('Physician', models.DO_NOTHING, blank=True, null=True)
    appointment_date = models.DateTimeField(blank=True, null=True)
    appointment_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                          null=True)

    class Meta:
        managed = False
        db_table = 'Appointment'


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    payment_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bill'


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'Department'

    def __str__(self):
        return self.dept_name


class EmergencyContactPerson(models.Model):
    ec_id = models.AutoField(db_column='EC_id', primary_key=True)  # Field name made lowercase.
    pname = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    phone_number = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emergency_Contact_Person'


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS')
    hire_date = models.DateField()
    ssn = models.CharField(db_column='SSN', unique=True, max_length=100,
                           db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        managed = False
        db_table = 'Employee'

    def  __str__(self):
        """Get the full name of the employee from the EmpName model."""
        if hasattr(self, 'empname'):
            return f"{self.empname.empfirst_name} {self.empname.emplast_name}"
        return "Name not set"


class EmpName(models.Model):
    id = models.AutoField(primary_key=True)
    emp = models.OneToOneField(Employee, on_delete=models.CASCADE)
    empfirst_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    emplast_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'Emp_Name'


class EmpPhone(models.Model):
    id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_default = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emp_Phone'
        unique_together = (('emp', 'phone_number'),)


class EmpAddress(models.Model):
    id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE)
    street = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    city = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_default = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emp_Address'


class LabTest(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_result = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    test_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Lab_Test'


class Nurse(models.Model):
    nurse_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Nurse'

    def __str__(self):
        return self.emp.__str__()


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ssn = models.CharField(db_column='SSN', unique=True, max_length=50,
                           db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patient'

    def __str__(self):
        try:
            return f"{self.patientname.first_name} {self.patientname.last_name} ({self.ssn})"
        except PatientName.DoesNotExist:
            return f"Patient {self.ssn}"


class PatientName(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'Patient_Name'


class PatientPhone(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', )

    class Meta:
        managed = False
        db_table = 'Patient_Phone'
        unique_together = (('patient', 'phone_number'),)


class Physician(models.Model):
    physician_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    speciality = models.ForeignKey('Speciality', models.DO_NOTHING)

    def __str__(self):
        return self.emp.__str__()

    class Meta:
        managed = False
        db_table = 'Physician'


class Radiology(models.Model):
    rid = models.AutoField(primary_key=True)
    report = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Radiology'


class Room(models.Model):
    room_number = models.AutoField(primary_key=True)
    capacity = models.IntegerField(blank=True, null=True)
    occupation = models.IntegerField(blank=True, null=True)
    room_type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'Room'

    def __str__(self):
        return str(self.room_number)


class Speciality(models.Model):
    speciality_id = models.AutoField(primary_key=True)
    speciality_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'Speciality'

    def __str__(self):
        return self.speciality_name


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class NurseService(models.Model):
    nurse_service_id = models.AutoField(db_column='nurse_Service_id', primary_key=True)  # Field name made lowercase.
    room_number = models.ForeignKey(Room, models.DO_NOTHING, db_column='room_number', blank=True, null=True)
    nurse = models.ForeignKey(Nurse, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nurse_Service'
