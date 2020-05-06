"""Initial Migration

Revision ID: 4c4852dd51d5
Revises: 
Create Date: 2020-05-06 15:42:09.078068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c4852dd51d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pitches', sa.Column('category', sa.String(length=255), nullable=True))
    op.add_column('pitches', sa.Column('description', sa.String(length=255), nullable=True))
    op.add_column('pitches', sa.Column('downvotes', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('upvotes', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_pitches_category'), 'pitches', ['category'], unique=False)
    op.create_index(op.f('ix_pitches_description'), 'pitches', ['description'], unique=False)
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.drop_constraint('users_pitch_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'pitch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_pitch_id_fkey', 'users', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'email')
    op.drop_column('users', 'bio')
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_index(op.f('ix_pitches_description'), table_name='pitches')
    op.drop_index(op.f('ix_pitches_category'), table_name='pitches')
    op.drop_column('pitches', 'user_id')
    op.drop_column('pitches', 'upvotes')
    op.drop_column('pitches', 'downvotes')
    op.drop_column('pitches', 'description')
    op.drop_column('pitches', 'category')
    op.drop_table('comments')
    # ### end Alembic commands ###