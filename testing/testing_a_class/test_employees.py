from employee import Employee
import unittest 

class TestEmployeeFunctions(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("John", "Doe", 50000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary,55000)

    def test_give_custom_raise(self):
        self.employee.give_raise(15000)
        self.assertEqual(self.employee.annual_salary,65000)

unittest.main()
