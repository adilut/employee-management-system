import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Initialize an empty dictionary to store employee data
employee_data = {}

# Messages to display on the canvas
messages = []

# Function to create an employee entry
def create_employee(input_text):
    return input_text.strip()

# Function to clear canvas and messages
def clear_canvas():
    messages.clear()

# Function to add an employee to the dictionary
def add_employee():
    clear_canvas()
    emp_id = create_employee(id.get_text())
    emp_name = create_employee(name.get_text())
    emp_number = create_employee(number.get_text())
    emp_salary = create_employee(salary.get_text())

    if emp_id and emp_name and emp_number:
        if emp_id in employee_data:
            messages.append("Employee with the same ID already exists.")
        elif not emp_salary.isdigit():
            messages.append("Salary must be a numeric value.")
        elif not emp_number.isdigit() or len(emp_number) < 10:
            messages.append("Number must be numeric and have a length of at least 10 characters.")
        else:
            employee_data[emp_id] = {
                "name": emp_name,
                "number": emp_number,
                "salary": emp_salary
            }
            messages.append("Employee Added Successfully")
            messages.append(f"ID: {emp_id}, Name: {emp_name}, Number: {emp_number}, Salary: {emp_salary}")
    else:
        messages.append("Please fill in all required fields.")# Function to delete an employee from the dictionary
def delete_employee():
    clear_canvas()
    emp_id = create_employee(delete_id.get_text())
    if emp_id in employee_data:
        del employee_data[emp_id]
        messages.append(f"Employee with ID {emp_id} deleted.")
    else:
        messages.append(f"Employee with ID {emp_id} not found.")
# Function to update an employee's information
def update_employee():
    clear_canvas()
    emp_id = create_employee(update_id.get_text())
    if emp_id in employee_data:
        emp_name = create_employee(update_name.get_text())
        emp_number = create_employee(update_number.get_text())
        emp_salary = create_employee(update_salary.get_text())

        if not emp_salary.isdigit():
            messages.append("Salary must be a numeric value.")
        else:
            employee_data[emp_id]["name"] = emp_name
            employee_data[emp_id]["number"] = emp_number
            employee_data[emp_id]["salary"] = emp_salary
            messages.append(f"Employee with ID {emp_id} updated.")
    else:
        messages.append(f"Employee with ID {emp_id} not found.")

# Function to display all employees on canvas
def display_employees_canvas():
    clear_canvas()
    emp_info = []
    for emp_id, emp_data in employee_data.items():
        emp_info.append(
            f"ID: {emp_id}, Name: {emp_data['name']}, Number: {emp_data['number']}, Salary: {emp_data['salary']}")

    if emp_info:
        messages.extend(emp_info)
    else:
        messages.append("No employees to display.")
def delete_all_employees():
    clear_canvas()
    if employee_data:
        # Add a confirmation dialog here if needed.
        employee_data.clear()
        messages.append("All employees deleted.")
    else:
        messages.append("No employees to delete.")

# Function to display all messages on canvas
def draw(canvas):
    y_position = 100
    for message in messages:
        canvas.draw_text(message, (20, y_position), 25, "Red")
        y_position += 50

# Create the GUI
frame = simplegui.create_frame("Employee Management System", 700, 600, 200)
id = frame.add_input("ID:", create_employee, 100)
name = frame.add_input("Name:", create_employee, 100)
number = frame.add_input("Number:", create_employee, 100)
salary = frame.add_input("Salary:", create_employee, 100)
frame.add_button("Add Employee", add_employee)
delete_id = frame.add_input("Delete ID:", create_employee, 100)
frame.add_button("Delete Employee", delete_employee)
update_id = frame.add_input("Update ID:", create_employee, 100)
update_name = frame.add_input("Update Name:", create_employee, 100)
update_number = frame.add_input("Update Number:", create_employee, 100)
update_salary = frame.add_input("Update Salary:", create_employee, 100)
frame.add_button("Update Employee", update_employee)
frame.add_button("Display All Employees", display_employees_canvas)
frame.add_button("Delete All Employees", delete_all_employees)  # Added button for deleting all employees
frame.set_draw_handler(draw)
frame.start()