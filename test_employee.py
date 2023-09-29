from classes import Employee, Developer
import unittest

class testEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.emp = Employee("bob", "smith", 200000)
        self.dev = Developer("mary", "brown", 120000, ["Python", "Django"])
        return super().setUp()

    def test_add_employee(self):
        self.assertEqual(self.emp.fn, "bob")
        self.assertEqual(self.emp.ln, "smith")
        self.assertEqual(self.emp.salary, 200000)
        self.assertEqual(self.emp.email, "bob.smith@test.com")

    def test_change_sal(self):
        self.emp.change_salary(105000)
        self.assertEqual(self.emp.salary, 105000)

    def test_add_developer(self):
        self.assertEqual(self.dev.email,"mary.brown@test.com")
        self.assertEqual(self.dev.languages,["Python","Django"])

    def test_add_languages(self):
        self.dev.add_languages(["Java"])
        self.assertEqual(self.dev.languages,["Python","Django","Java"] )

if __name__ == "__main__":
    unittest.main()