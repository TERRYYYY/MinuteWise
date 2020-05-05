from flask import render_template,request,redirect,url_for
from . import main
# from .forms import PitchForm
from ..models import Pitch

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Moment in Time'

    search_pitch = request.args.get('pitch_query')
    pitches= Pitch.get_all_pitches()  

    return render_template('index.html', title = title, pitch= pitch)