"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from app import db

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


from app.propertyform import NewPropertyForm
from app.models import Property

@app.route('/properties/create', methods=['GET', 'POST'])
def newproperty():
    
    form = NewPropertyForm()

    if request.method == "POST":
        if form.validate_on_submit():
            title = request.form['title']
            description = request.form['description']
            rooms = request.form['rooms']
            bathrooms = request.form['bathrooms']
            price = request.form['price']
            propertytype = request.form['propertytype']
            location = request.form['location']
            photo = request.files['photo']

            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            print(title,description,rooms,bathrooms,price,propertytype,location,filename)

            properti = Property(title,description,rooms,bathrooms,price,propertytype,location,filename)
            db.session.add(properti)
            db.session.commit()
            
            flash("Property was successfully uploaded")
            return redirect(url_for('displayproperties'))

    return render_template('newproperty.html', form = form)


@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)


@app.route('/properties')
def displayproperties():
    data = db.session.query(Property).all()
    return render_template('displayproperty.html', data = data)


@app.route('/properties/<propertyid>')
def individualProperty(propertyid):

    ip = Property.query.filter_by(id=propertyid).first()
    
    return render_template('individualproperty.html', individualData = ip)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
