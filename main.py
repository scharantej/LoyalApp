
# Required imports
from flask import Flask, render_template, request

# Create the Flask application
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    """Main landing page of the application."""
    return render_template('index.html')

@app.route('/earn_points')
def earn_points():
    """Displays various ways to earn loyalty points."""
    # Get the form data
    years_of_membership = request.args.get('years_of_membership')
    top_up_percentage = request.args.get('top_up_percentage')
    # Calculate the number of points earned
    points_earned = calculate_points_earned(years_of_membership, top_up_percentage)
    # Render the template with the calculated points
    return render_template('earn_points.html', points_earned=points_earned)

@app.route('/spend_points')
def spend_points():
    """Lists available options for spending loyalty points."""
    # Get the form data
    option = request.args.get('option')
    amount_of_points = request.args.get('amount_of_points')
    # Deduct the corresponding number of points from the user's balance
    deduct_points(option, amount_of_points)
    # Render the template
    return render_template('spend_points.html')

@app.route('/program_details')
def program_details():
    """Displays a detailed description of the loyalty program."""
    return render_template('program_details.html')

@app.route('/report')
def report():
    """Generates a report containing insights into the program's customer satisfaction, revenue generation, and operational costs."""
    # Generate the report
    report = generate_report()
    # Render the template with the report
    return render_template('report.html', report=report)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
