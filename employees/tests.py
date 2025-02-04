from django.test import TestCase
from employees.models import Employee

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
        self.assertTrue(employee.check_password("Password@123"))