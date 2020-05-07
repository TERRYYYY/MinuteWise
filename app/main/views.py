from flask import render_template,request,redirect,url_for
from . import main
# from .forms import PitchForm
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import Pitch, User
# from .forms import PitchForm,UpdateProfile
from .. import db
from flask_login import login_required, current_user
from app.models import User,Pitch,Comment
from .forms import UpdateProfile, PitchForm, CommentForm
import markdown2  

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'MinuteWise | Pitch'

    # search_pitch = request.args.get('pitch_query')
    # pitch= Pitch.get_all_pitches()  

    return render_template('index.html', title = title)


@main.route("/pitch" ,methods=["GET", "POST"])
@login_required
def pitch():
    form = PitchForm()
    pitches = Pitch.query.all()


    if request.method == "POST":
        req = request.form
        print(req)

        pitch = req.get('pitch')
        new_pitch = Pitch(description = pitch , user = current_user)
        db.session.add(new_pitch)
        db.session.commit()
        pitches = Pitch.query.all()

        
    return render_template("new_pitch.html" ,pitches = pitches , form= form)

# @main.route('/pitch', methods = ['GET','POST'])
# @login_required
# def new_pitch():
#     form = PitchForm()
#     if form.validate_on_submit():
#         category = form.category.data
#         description = form.description.data
#         user_id = current_user

#         # Updated review instance
#         new_pitch=Pitch(pitch_id=pitch.id,category=category,description=description,user=current_user)

#         # save review method
#         new_pitch.save_pitch()
#         db.session.add(new_pitch)
#         db.session.commit()

#     return render_template('new_pitch.html',form = form )


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
    pitches=Pitch.query.get(id)
    if pitches is None:
        abort(404)
    format_pitches = markdown2.markdown(pitches.pitch_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('pitch.html',pitches = pitches,format_pitches=format_pitches)

@main.route('/comment/<int:id>', methods=["GET", "POST"])
@login_required
def comment(id):
    form = CommentForm()
    comments = Comment.query.filter_by(pitch_id = id)
    post = Pitch.query.filter_by(id=id).first()
    if request.method == 'POST':
            req = request.form
            print(req)

            pitch = req.get('comment')
            comment = Comment(description = pitch , user = current_user , pitch = post)

            db.session.add(comment)
            db.session.commit()
   
    title = 'Comments'
    return render_template("comment.html" ,title = title , pitch = post , form= form, comments = comments)


# @main.route('/comment' ,methods=['POST', 'GET'])
# @login_required
# def comment(pitch_id):
#     form = CommentForm()
#     pitch = Pitch.query.get(pitch_id)
#     all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
#     if form.validate_on_submit():
#         comment = form.comment.data
#         pitch_id = pitch_id
#         user_id = current_user._get_current_object().id
#         new_comment = Comment(
#             comment=comment, user_id=user_id, pitch_id=pitch_id)
#         new_comment.save_c()
#         return redirect(url_for('main.comment', pitch_id=pitch_id))
#     return render_template('comment.html', form=form, pitch=pitch, all_comments=all_comments)
# <int:pitch_id>


@main.route('/like', methods=['POST', 'GET'])
@login_required
def like(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index', id=id))
        else:
            continue
    new_vote = Upvote(user=current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.index', id=id))
# <int:id>'

@main.route('/dislike', methods=['POST', 'GET'])
@login_required
def dislike(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in pitch:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index', id=id))
        else:
            continue
    new_downvote = Downvote(user=current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.index', id=id))

