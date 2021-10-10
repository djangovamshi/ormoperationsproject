from rest_framework import Serializers

class EmployeeSerializer(serializers.serialize):
  class Meta:
    model = Employee
    fields = "__all__""
