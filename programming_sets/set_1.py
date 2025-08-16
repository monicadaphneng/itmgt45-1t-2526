'''Programming Set 1

This assignment will familiarize you with Python's basics.
'''
import math

def savings(gross_pay, tax_rate, expenses):
    """
    Function that calculates the money remaining after taxes and expenses.

    Parameters:
    gross_pay: int
        Gross salary earned in one pay period.
    tax_rate: float
        The tax rate for a particular pay period (a number between 0 and 1).
    expenses: int
        Expenses paid in a pay period.

    Returns:
    int: Money remaining after taxes and expenses.
    """
    after_tax = math.floor(gross_pay * (1 - tax_rate))
    remaining = after_tax - expenses
    return remaining


def material_waste(total_material, material_units, num_jobs, job_consumption):
    """
    Function that calculates how much material input will be wasted after
    running a number of jobs that consume a set amount of material.

    Parameters:
    total_material: int
        Total material available.
    material_units: str
        Units of the material (e.g., "kg", "L", "m").
    num_jobs: int
        Number of jobs to run.
    job_consumption: int
        Material consumption per job.

    Returns:
    str: Remaining material with units (e.g., "10kg").
    """
    consumed = num_jobs * job_consumption
    waste = total_material - consumed
    return str(waste) + material_units


def interest(principal, rate, periods):
    """
    Function that calculates the final value of an investment based on
    simple interest.

    Parameters:
    principal: int
        The principal amount invested.
    rate: float
        Interest rate per period (a number between 0 and 1).
    periods: int
        Number of periods the money is invested for.

    Returns:
    int: Final value of the investment after interest, rounded down.
    """
    final_value = principal + (principal * rate * periods)
    return math.floor(final_value)
