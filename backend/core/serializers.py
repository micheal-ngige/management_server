from rest_framework import serializers
from .models import (
    Employee, Department, Documents, Experience, EmployeeTraining, EmployeeProfile,
    HRPersonel, HrProfile, Manager, ManagerProfile, Leave, LeaveApproval, Session,
    Training, Remuneration, RemunerationDescription, Goals, Education
)

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    goals = GoalsSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = '__all__'


class LeaveApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApproval
        fields = '__all__'


class EmployeeTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTraining
        fields = '__all__'


class TrainingSerializer(serializers.ModelSerializer):
    trainings = EmployeeTrainingSerializer(many=True, read_only=True)

    class Meta:
        model = Training
        fields = '__all__'


class RemunerationDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemunerationDescription
        fields = '__all__'


class RemunerationSerializer(serializers.ModelSerializer):
    remunerations = RemunerationDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Remuneration
        fields = '__all__'


class HrProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HrProfile
        fields = '__all__'


class ManagerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerProfile
        fields = '__all__'


class LeaveSerializer(serializers.ModelSerializer):
    leave_approval = LeaveApprovalSerializer(many=True, read_only=True)

    class Meta:
        model = Leave
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    employee_profiles = EmployeeProfileSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)
    leaves = LeaveSerializer(many=True, read_only=True)
    goals = GoalsSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    remunerations = RemunerationSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        exclude = ['password']


class ManagerSerializer(serializers.ModelSerializer):
    leave_approvals = LeaveApprovalSerializer(many=True, read_only=True)
    manager_profile = ManagerProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Manager
        exclude = ['password']


class HrSerializer(serializers.ModelSerializer):
    leave_approvals = LeaveApprovalSerializer(many=True, read_only=True)
    hr_profiles = HrProfileSerializer(many=True, read_only=True)

    class Meta:
        model = HRPersonel
        exclude = ['password']
