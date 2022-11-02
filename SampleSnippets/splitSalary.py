# program to split salary 

total_income = 190000

employee_details = [
    {
        "name":"jasir",
        "base_salary":90000
    },
    {
        "name":"Salih",
        "base_salary":70000
    },
    {
        "name":"saranya",
        "base_salary":35000
    },
    {
        "name":"suhail",
        "base_salary":50000
    },
    {
        "name":"shabeeb at",
        "base_salary":50000
    },
]

# split total_income to all employees in equal percentage based on their base_salary
def split_salary(total_income,employee_details):
    total_base_salary = 0
    for employee in employee_details:
        total_base_salary += employee["base_salary"]
    for employee in employee_details:
        employee["salary"] = (employee["base_salary"]/total_base_salary)*total_income
    
    
    
    return employee_details

split_salary = split_salary(total_income,employee_details)

print("split_salary : ",split_salary)

for emp in split_salary:
    print(emp["name"],":",emp["salary"],"remaning : ",total_income-emp["salary"]," percentage : ",(emp["salary"]/total_income)*100)
    