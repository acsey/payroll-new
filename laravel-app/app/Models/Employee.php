<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Employee extends Model
{
    protected $fillable = [
        'name',
        'daily_salary',
        'worked_days',
        'overtime_hours',
        'sunday_hours',
        'bonuses',
    ];
}
