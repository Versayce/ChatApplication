from flask import Blueprint, render_template, redirect, request

from app.forms.server_form import ServerForm
from app.forms.message_form import MessageForm
from ..models import Server, Channel, Message, db


message_bp = Blueprint('messages', __name__)


@message_bp.route('/new', methods=['POST'])
def new_message():
    form = MessageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    
    if form.validate_on_submit():
        new_message = Message()
        form.populate_obj(new_message)
        
        db.session.add(new_message)
        db.session.commit()
        return new_message.to_dict()

    else:
        return form.errors


@message_bp.route('/<int:id>', methods=['DELETE'])
def delete_message(id):
    delete_message = Message.query.get(id)
    
    db.session.delete(delete_message)
    db.session.commit()
    return {'message': 'Message Deleted!'}
