import unittest
from payroll.payroll import Employee, Payroll, Deduction


class TestPayroll(unittest.TestCase):
    def setUp(self):
        self.emp = Employee(
            id=1,
            name="Juan",
            daily_salary=200,
            worked_days=15,
            overtime_hours=4,
            sunday_hours=2,
            bonuses=500,
            deductions=[Deduction(name="loan", amount=100)],
        )
        self.payroll = Payroll([self.emp])

    def test_base_salary(self):
        self.assertAlmostEqual(self.emp.calculate_base_salary(), 3000)

    def test_total_earnings(self):
        earnings = self.emp.total_earnings()
        self.assertGreater(earnings, self.emp.calculate_base_salary())

    def test_net_pay(self):
        net = self.emp.net_pay()
        self.assertGreater(net, 0)

    def test_export_csv(self):
        path = "test_output.csv"
        self.payroll.export_csv(path)
        with open(path) as f:
            header = f.readline()
        self.assertIn("net_pay", header)


if __name__ == "__main__":
    unittest.main()
