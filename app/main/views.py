from flask import render_template,request,redirect,url_for
from . import main
# from .forms import PitchForm
from ..models import Pitch
from flask_login import login_required

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Moment in Time'

    search_pitch = request.args.get('pitch_query')
    pitches= Pitch.get_all_pitches()  

    return render_template('index.html', title = title, pitch= pitch)

@main.route('/pitch', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # Updated review instance
        new_pitch = Pitch(pitch_id=movie.id,category=category,description=pitch)

        # save review method
        new_pitch.save_pitch()
        db.session.add(new_pitch)
        db.session.commit()

    return render_template('new_pitch.html',pitch=pitch)