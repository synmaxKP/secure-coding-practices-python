from flask import request

# Code Example - Lack of Input Validation:
def update_profile(request):
    # Extract the user's input
    name = request.form.get("name")
    age = request.form.get("age")

    # Update the profile without validating the inputs
    # ...


# # Proper Solution - Input Validation:
# def update_profile(request):
#     # Extract the user's input
#     name = request.form.get("name")
#     age = request.form.get("age")

#     # Validate the inputs
#     if not name or npyot age:
#         return "Invalid input data. Please provide valid name and age."

#     # Update the profile with validated inputs
#     # ...

# Example usage
app = Flask(__name__)

@app.route('/profile', methods=['POST'])
def profile():
    error_message = update_profile(request)
    if error_message:
        return error_message
    else:
        return "Profile updated successfully."
