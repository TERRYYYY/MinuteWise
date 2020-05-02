# from flask import render_template
# from flask import render_template,request,redirect,url_for
# from .models import Pitch 
# from .forms import PitchForm

# # Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
    
#     title = 'Moment in Time'
#     return render_template('index.html', title = title)

# @app.route('/pitch/<int:pitch_id>')
# def pitch(pitch_id):

#     '''
#     View pitch page function that returns the pitches details page and its data
#     '''
#     return render_template('pitch.html',id = pitch_id)

# @app.route('/movie/pitch/new/<int:id>', methods = ['GET','POST'])
# def new_pitch(id):
#     form = PitchForm()
#     pitch = get_pitch(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#         new_pitch = Pitch(pitch.id,title,review)
#         new_pitch.save_pitch()
#         return redirect(url_for('pitch',id = pitch.id ))

#     return render_template('new_pitch.html',title = title, pitch_form=form, movie=movie)