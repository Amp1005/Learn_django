from faker import Faker
import random
from .models import *

fake = Faker()

def create_subject_marks(n):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(f"Error: {e}")


def seed_db(n=10) -> None:
    try:
        departments_objs = list(Department.objects.all())  # Convert QuerySet to list
        
        if not departments_objs:  # Ensure departments exist
            print("No departments found. Please create departments first.")
            return
        
        for _ in range(n):
            department = random.choice(departments_objs)  # Choose a department safely
            student_id = f'STU-0{random.randint(100, 999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 25)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )

        print(f"Successfully seeded {n} students.")

    except Exception as e:
        print(f"Error: {e}")
