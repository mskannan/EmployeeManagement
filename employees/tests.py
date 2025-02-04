from django.test import TestCase
from employees.models import Employee
from django.db.utils import IntegrityError

class EmployeeModelTest(TestCase):

    # Test case to create a valid employee
    def test_create_employee(self):
        # Create an employee object
        employee = Employee.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            phone="1234567890",
            username="john1234",
            password="Password@123"
        )
        # Employee Verify creation
        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.email, "john.doe@example.com")
        self.assertEqual(employee.phone, "1234567890")
        self.assertEqual(employee.username, "john1234") 


    # Test case to check email uniqueness
    def test_employee_email_unique(self):
        # Create the first employee with a unique email
        Employee.objects.create(
            name="kannan",
            email="kannan@mail.in",
            phone="9876543210",
            username="kannan1234",
            password="Password@123"
        )
        # Check same email raises an IntegrityError
        with self.assertRaises(IntegrityError):
            Employee.objects.create(
                name="senthamarai",
                email="kannan@mail.in",  # Same email as kannan
                phone="1112233445",
                username="sentha12345",
                password="Password@123"
            )
 