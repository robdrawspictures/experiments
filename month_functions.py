months = [
    {"name" : "January", "short" : "Jan", "number" : 1},
    {"name" : "March", "short" : "Mar", "number" : 3},
    {"name" : "March", "short" : "Apr", "number" : 4},
    {"name" : "September", "short" : "Sep", "number" : 9},
    {"name" : "March", "short" : "Oct", "number" : 10},
]

def number_to_full_month_name(num_month):
    for month in months:
        if num_month == month["number"]:
            return month["name"]


def number_to_short_month_name(num_month):
    for month in months:
        if num_month == month["number"]:
            return month["short"]

# I think these will only work when copied into the
# python_functions_practice.py file, in their current state.