from django.test import TestCase
from employees.models import Employee
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

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

    # Test case to check phone uniqueness
    def test_employee_phone_unique(self):
        # Create an employee with a unique phone number
        Employee.objects.create(
            name="Ramkumar",
            email="ramkumar@mail.in",
            phone="5555555555",
            username="Ramkumar1234",
            password="Password@123"
        )
        # Check that trying to create another employee with the same phone number raises an IntegrityError
        with self.assertRaises(IntegrityError):
            Employee.objects.create(
                name="Basith",
                email="basith@mail.in",
                phone="5555555555",  # Same phone as Alice
                username="Basith1234",
                password="Password@123"
            )

    # Test case to check password complexity (lowercase, uppercase, special char, and minimum length)
    def test_password_complexity(self):
        # Password too simple (just lowercase letters)
        with self.assertRaises(ValidationError):
            employee = Employee(
                name="WeakPassUser",
                email="weakpass@example.com",
                phone="1234567890",
                username="weakuser1",
                password="password@123"  # This is too simple and doesn't meet the complexity requirements
            )
            employee.full_clean()  # This will trigger model validation

        # Password valid (meets complexity requirements)
        employee = Employee(
            name="StrongPassUser",
            email="strongpass@example.com",
            phone="9876543210",
            username="stronguser1",
            password="Password@123"  # This meets the complexity requirements
        )
        employee.full_clean()  # This should pass validation

    #check if the employee username is alphanumeric
    def test_username_alphanumeric(self):
        # Username with non-alphanumeric character (invalid username)
        with self.assertRaises(ValidationError):
            employee = Employee(
                name="InvalidUser",
                email="invaliduser@example.com",
                phone="9876543210",
                username="invalid$user",  # Invalid username with a special character
                password="Password@123"
            )
            employee.full_clean()  # This should raise ValidationError due to non-alphanumeric character

