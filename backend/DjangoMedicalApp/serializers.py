from rest_framework import serializers

from DjangoMedicalApp.models import Bill, Company, CompanyAccount, CompanyBank, Customer, CustomerRequest, Employee, EmployeeBank, MedicalDetails, Medicine


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        # fields = ['name', 'license_no', 'address', 'contact_no', 'email', 'description', 'added_on']
        fields = "__all__"


class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company_id).data
        return response


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        # fields = ['name', 'license_no', 'address', 'contact_no', 'email', 'description', 'added_on']
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["company"] = CompanySerializer(instance.company_id).data
        return response


class MedicalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetails
        # fields = ['name', 'license_no', 'address', 'contact_no', 'email', 'description', 'added_on']
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["medicine"] = MedicineSerializer(instance.medicine_id).data
        return response


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['name', 'license_no', 'address', 'contact_no', 'email', 'description', 'added_on']
        fields = "__all__"


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = ['name', 'license_no', 'address', 'contact_no', 'email', 'description', 'added_on']
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        # fields = ['name', 'license_no', 'address', 'contact_no', 'email', 'description', 'added_on']
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["customer"] = Customer(instance.customer_id).data
        return response


class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        # fields = ['name', 'license_no', 'address', 'contact_no', 'email', 'description', 'added_on']
        fields = "__all__"


class CompanyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        # fields = ['name', 'license_no', 'address', 'contact_no', 'email', 'description', 'added_on']
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["company"] = CompanySerializer(instance.company_id).data
        return response


class EmployeeBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBank
        # fields = ['name', 'license_no', 'address', 'contact_no', 'email', 'description', 'added_on']
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["employee"] = Employee(instance.employee_id).data
        return response
