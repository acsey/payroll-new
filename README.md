# Payroll Processing System

This project provides a minimal payroll processing system compliant with basic aspects of Mexican Federal Labor Law.

## Features

- Basic employee payroll calculations including IMSS and INFONAVIT deductions.
- Placeholder ISR calculation (10% of base salary).
- Support for overtime, Sunday premium, bonuses and dynamic deductions.
- Generation of payroll receipts per employee.
- Export of summarized payroll information to CSV.

## Usage

1. Install Python 3.10 or later.
2. Install dependencies (none required for base usage).
3. Run the tests:

```bash
python -m unittest discover
```

4. Create a CSV file with employee data and load it:

```python
from payroll.payroll import Payroll
payroll = Payroll.from_csv("employees.csv")
receipts = payroll.generate_receipts()
for emp_id, text in receipts.items():
    print(text)
```

## CSV Format

The CSV file must include at least the following columns:

- `id`
- `name`
- `daily_salary`
- `worked_days`

Optional columns:

- `overtime_hours`
- `sunday_hours`
- `bonuses`

## Disclaimer

This project is a simplified reference implementation and does not cover all edge cases or legal obligations. Always verify calculations with a payroll specialist.
