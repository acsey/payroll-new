"""Basic payroll processing system for Mexican labor law compliance."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import List, Dict
import csv

IMSS_RATE = 0.02375
INFONAVIT_RATE = 0.05


@dataclass
class Deduction:
    name: str
    rate: float = 0.0
    amount: float = 0.0
    dynamic: bool = True


@dataclass
class Employee:
    id: int
    name: str
    daily_salary: float
    worked_days: int
    overtime_hours: int = 0
    sunday_hours: int = 0
    bonuses: float = 0.0
    deductions: List[Deduction] = field(default_factory=list)

    def calculate_base_salary(self) -> float:
        return self.daily_salary * self.worked_days

    def calculate_imss(self, base: float) -> float:
        return base * IMSS_RATE

    def calculate_infonavit(self, base: float) -> float:
        return base * INFONAVIT_RATE

    def calculate_isr(self, base: float) -> float:
        # Placeholder variable ISR calculation
        return base * 0.1

    def total_deductions(self, base: float) -> float:
        total = self.calculate_imss(base) + self.calculate_infonavit(base) + self.calculate_isr(base)
        for d in self.deductions:
            if d.amount:
                total += d.amount
            else:
                total += base * d.rate
        return total

    def total_earnings(self) -> float:
        base = self.calculate_base_salary()
        overtime = self.overtime_hours * (self.daily_salary / 8) * 2
        sunday = self.sunday_hours * (self.daily_salary / 8) * 0.25
        return base + overtime + sunday + self.bonuses

    def net_pay(self) -> float:
        base = self.calculate_base_salary()
        earnings = self.total_earnings()
        return earnings - self.total_deductions(base)


class Payroll:
    def __init__(self, employees: List[Employee]) -> None:
        self.employees = employees
        self.date = date.today()

    @classmethod
    def from_csv(cls, path: str) -> "Payroll":
        employees = []
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                emp = Employee(
                    id=int(row["id"]),
                    name=row["name"],
                    daily_salary=float(row["daily_salary"]),
                    worked_days=int(row["worked_days"]),
                    overtime_hours=int(row.get("overtime_hours", 0)),
                    sunday_hours=int(row.get("sunday_hours", 0)),
                    bonuses=float(row.get("bonuses", 0)),
                )
                employees.append(emp)
        return cls(employees)

    def generate_receipts(self) -> Dict[int, str]:
        receipts = {}
        for emp in self.employees:
            receipts[emp.id] = (
                f"Payroll receipt for {emp.name}\n"
                f"Base salary: {emp.calculate_base_salary():.2f}\n"
                f"Earnings: {emp.total_earnings():.2f}\n"
                f"Deductions: {emp.total_deductions(emp.calculate_base_salary()):.2f}\n"
                f"Net pay: {emp.net_pay():.2f}\n"
            )
        return receipts

    def export_csv(self, path: str) -> None:
        with open(path, "w", newline="") as f:
            fieldnames = [
                "id",
                "name",
                "base_salary",
                "earnings",
                "deductions",
                "net_pay",
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for emp in self.employees:
                base = emp.calculate_base_salary()
                writer.writerow(
                    {
                        "id": emp.id,
                        "name": emp.name,
                        "base_salary": f"{base:.2f}",
                        "earnings": f"{emp.total_earnings():.2f}",
                        "deductions": f"{emp.total_deductions(base):.2f}",
                        "net_pay": f"{emp.net_pay():.2f}",
                    }
                )

    def total_payroll(self) -> float:
        return sum(emp.net_pay() for emp in self.employees)
