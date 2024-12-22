from django.contrib import admin
from .models import (Patient, PatientName, PatientPhone, Employee, Department, EmpName, EmpPhone, EmpAddress, Physician,
                     Speciality, Nurse, Room, Appointment, Radiology, LabTest, Bill, EmergencyContactPerson,
                     NurseService, Admission)


class PatientNameInline(admin.StackedInline):
    model = PatientName
    can_delete = False
    verbose_name_plural = "Patient Name"
    fk_name = "patient"


class PatientPhoneInline(admin.StackedInline):
    model = PatientPhone
    can_delete = False
    verbose_name_plural = "Patient Phone"
    fk_name = "patient"


class EmpNameInline(admin.StackedInline):
    model = EmpName
    extra = 1  # Allows adding one EmpName instance by default
    can_delete = False  # Prevent deleting the name


class EmpPhoneInline(admin.TabularInline):
    model = EmpPhone
    extra = 1  # Allows adding one phone number by default


class EmpAddressInline(admin.TabularInline):
    model = EmpAddress
    extra = 1  # Allows adding one address by default


class NurseInline(admin.TabularInline):
    model = NurseService
    extra = 1


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id',  'get_full_name','ssn', 'age', 'gender',)
    inlines = [PatientNameInline, PatientPhoneInline]

    def get_full_name(self, obj):
        """Return the full name of the patient."""
        return f"{obj.patientname.first_name} {obj.patientname.last_name}" if hasattr(obj, 'patientname') else "N/A"

    get_full_name.short_description = 'Full Name'

    def get_phone_number(self, obj):
        """Return the phone number of the patient."""
        return obj.patientphone.phone_number if hasattr(obj, 'patientphone') else "N/A"

    get_phone_number.short_description = 'Phone Number'


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [EmpNameInline, EmpPhoneInline, EmpAddressInline]
    list_display = ('emp_id', 'get_full_name', 'salary', 'gender', 'hire_date', 'ssn', 'get_department_name')
    search_fields = ('emp_id', 'ssn', 'gender', 'empname__empfirst_name', 'empname__emplast_name', 'dept__dept_name')
    list_filter = ('gender', 'dept', 'hire_date')


    def get_full_name(self, obj):
        """Get the full name of the employee from the EmpName model."""
        if hasattr(obj, 'empname'):
            return f"{obj.empname.empfirst_name} {obj.empname.emplast_name}"
        return "Name not set"

    get_full_name.short_description = 'Full Name'

    def get_department_name(self, obj):
        """Get the department name (object_name) from the related Department model."""
        return obj.dept.dept_name if obj.dept else "No Department"

    get_department_name.short_description = 'Department'


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('speciality_name',)


@admin.register(Physician)
class PhysicianAdmin(admin.ModelAdmin):
    list_display = ('emp',)


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('emp',)



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'occupation', 'room_type')
    inlines = [NurseInline]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'physician', 'appointment_date', 'appointment_status')


@admin.register(Radiology)
class RadiologyAdmin(admin.ModelAdmin):
    list_display = ('patient','report', )


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_name','test_result',)


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('patient', 'payment_type', 'payment_date', 'total_amount')


@admin.register(EmergencyContactPerson)
class EmergencyContactPersonAdmin(admin.ModelAdmin):
    list_display = ('patient', 'pname', 'phone_number')

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'room_number')