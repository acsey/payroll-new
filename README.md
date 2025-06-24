# Payroll Processing System (Laravel)

This repository contains a Laravel-based payroll processing backend with a minimal API.
The application uses PostgreSQL via Docker Compose and can be extended with a modern frontend using Vite.

## Requirements
- PHP 8.3 or later
- Composer
- Docker (for Sail)

## Running with Sail
Laravel Sail provides a Docker environment that includes PHP, Nginx and PostgreSQL.

```bash
cd laravel-app
./vendor/bin/sail up -d
```

The API will be available at `http://localhost` and PostgreSQL will be available on port `5432`.

## API Endpoints
- `GET /api/employees` – list employees
- `POST /api/employees` – create an employee (accepts JSON fields: `name`, `daily_salary`, `worked_days`, `overtime_hours`, `sunday_hours`, `bonuses`)

These routes are defined in `routes/api.php` and handled by `PayrollController`.

## Kubernetes
For Kubernetes deployments you can build a container image using the Sail Dockerfile
and create appropriate Deployment and Service manifests pointing to the `laravel.test` service.
