from django.contrib import admin

# Register your models here.
from DjangoMedicalApp.models import Company, Medicine, Employee, Customer, Bill, EmployeeSalary, BillDetails, \
    MedicalDetails, CompanyBank, EmployeeBank, CustomerRequest, CompanyAccount

admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(MedicalDetails)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(EmployeeSalary)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
admin.site.register(EmployeeBank)
