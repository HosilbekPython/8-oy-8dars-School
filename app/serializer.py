from rest_framework import serializers
from .models import Class , Student , Teacher , User , Admin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'role']
        extra_kwargs = {'password': {'write_only': True}, 'role': {'read_only': True}}
        read_only_field = ['role']


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = ['user', 'phone_number', 'addres', 'classs']
        read_only_fields = ['role']

    def validate_classs(self, value):
        if not value:
            raise serializers.ValidationError("Class list may not be empty.")
        for class_id in value:
            if not Class.objects.filter(id=class_id).exists():
                raise serializers.ValidationError(f"Class with ID {class_id} does not exist.")
        return value

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        password = user_data.pop("password")
        user_data['role'] = 'admin'  # Role ni avtomatik belgilash
        user = User.objects.create_user(**user_data)
        user.set_password(password)
        user.save()
        admin = Admin.objects.create(user=user, **validated_data)
        admin.classs.set(validated_data.get('classs', []))  # ManyToMany maydonini to‘g‘ri sozlash
        return admin

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        user = instance.user

        # User ma’lumotlarini yangilash
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        # Admin ma’lumotlarini yangilash
        classs_data = validated_data.pop('classs', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # ManyToMany maydonini yangilash
        if classs_data is not None:
            instance.classs.set(classs_data)

        return instance



class TeacherSerilizer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'photo', 'addres', 'classs']
        read_only_fields = ['role']

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        password = user_data.pop("password")
        user_data['role'] = 'teacher'  # Role ni avtomatik belgilash
        user = User.objects.create_user(**user_data)
        user.set_password(password)
        user.save()
        teacher = Teacher.objects.create(user=user, **validated_data)
        teacher.classs.set(validated_data.get('classs', []))
        return teacher

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        user = instance.user

        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        classs_data = validated_data.pop('classs', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if classs_data is not None:
            instance.classs.set(classs_data)
        instance.save()
        return instance


class StudentSerilizer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['user', 'photo', 'addres', 'classs']
        read_only_fields = ['role']

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        password = user_data.pop("password")
        user_data['role'] = 'student'  # Role ni avtomatik belgilash
        user = User.objects.create_user(**user_data)
        user.set_password(password)
        user.save()
        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        user = instance.user

        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



class ClassSerilizer(serializers.ModelSerializer):
    teachers = TeacherSerilizer(many=True , read_only=True , source='teacher_set')

    class Meta:
        model = Class
        fields = ['id', 'name', 'teachers']

    def create(self, validated_data):
        class_instance = Class.objects.create(**validated_data)
        return class_instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



