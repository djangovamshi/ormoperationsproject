from rest_framework import serializers
from ormoperationapp.models import Employee
class EmployeeSerializer(serializers.ModelSerializer): # Employee Serilaizers responsible for all the fields
  class Meta:
    model = Employee
    fields = '__all__'   # reperesentation of all The Fields Instead Writting All The COde We JUst Use MOdelSerializers For Shortcut
