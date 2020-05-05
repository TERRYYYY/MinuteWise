from flask import render_template,request,redirect,url_for
from . import main
# from .forms import PitchForm
from ..models import Pitch
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import Pitch, User
# from .forms import PitchForm,UpdateProfile
from .. import db
from flask_login import login_required, current_user
from app.models import User,Pitch,Pitchcategory
import markdown2  

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Moment in Time'

    # search_pitch = request.args.get('pitch_query')
    # pitch= Pitch.get_all_pitches()  

    return render_template('index.html', title = title)

@main.route('/pitch', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # Updated review instance
        new_pitch = Pitch(pitch_id=pitch.id,category=category,description=pitch,user=current_user)

        # save review method
        new_pitch.save_pitch()
        db.session.add(new_pitch)
        db.session.commit()

    return render_template('new_pitch.html',pitch=pitch)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/<int:id>')
def single_pitch(id):
    pitches=Pitchcategory.query.get(id)
    if pitches is None:
        abort(404)
    format_pitches = markdown2.markdown(pitches.pitch_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('pitch.html',pitches = pitches,format_pitches=format_pitches)