# app.py
from flask import Flask, render_template, redirect, url_for
from forms import StaffApplicationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your own secret key

@app.route('/', methods=['GET', 'POST'])
def staff_application():
    form = StaffApplicationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        age = form.age.data
        timezone = form.timezone.data
        experience = form.experience.data
        reason = form.reason.data
        additional_info = form.additional_info.data
        
        # Print to console
        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Age: {age}')
        print(f'Timezone: {timezone}')
        print(f'Experience: {experience}')
        print(f'Reason: {reason}')
        print(f'Additional Info: {additional_info}')
        
        return redirect(url_for('success'))

    return render_template('staff_application.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
