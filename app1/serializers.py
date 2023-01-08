from .models import Employee
from rest_framework import serializers

def multiple_of_1000(value):
    if value % 1000 != 0:
        raise serializers.ValidationError('Salary should be in multiple of 1000')

class EmployeeSerializer(serializers.Serializer):
    eid = serializers.IntegerField()
    ename = serializers.CharField(max_length =100)
    eaddr = serializers.CharField(max_length = 500)
    esal = serializers.FloatField(validators=[multiple_of_1000,])
    email = serializers.EmailField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.eid = validated_data.get('eid', instance.eid)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.eaddr = validated_data.get('eaddr', instance.eaddr)
        instance.esal = validated_data.get('esal', instance.esal)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance

    def validate_esal(self, value):
        if value < 5000:
            raise serializers.ValidationError('Salary should be more than 5000')
        return value

    def validate(self, data):
        print(type(data))
        email = data.get('email')
        print(type(email))
        if email.endswith('gmail.com') != True:
            raise serializers.ValidationError("Domain name should be gmail.com")
        return data

