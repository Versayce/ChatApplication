from flask import Blueprint, request
from ..models import PmChat, Message, db
from ..forms.pm_chat_form import PmChatForm


pm_chat_bp = Blueprint('chats', __name__)

@pm_chat_bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def pm_chat_by_id(id):
    pm_chat = PmChat.query.get(id)

    if pm_chat:

        if request.method == 'GET':
            pm_chat_dict = pm_chat.to_dict()
            pm_chat_dict['pm_messages'] = [message.to_dict() for message in pm_chat.messages]
            return pm_chat_dict

        if request.method == 'PUT':
            form = PmChatForm()
            form['csrf_token'].data = request.cookies['csrf_token']

            if form.validate_on_submit():
                pm_chat.name = form.data['name']
                pm_chat.private = form.data['private']
                db.session.commit()
                return pm_chat.to_dict()
            else:
                return form.errors

        if request.method == 'DELETE':
            db.session.delete(pm_chat)
            db.session.commit()
            return {'message': 'Pm Chat Deleted!'}

    return { "error": "Channel not found", "errorCode" : 404 }, 404


@pm_chat_bp.route('/new', methods=['POST'])
def new_pm_chat():
    form = PmChatForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_pm_chat = PmChat()
        form.populate_obj(new_pm_chat)

        db.session.add(new_pm_chat)
        db.session.commit()
        return new_pm_chat.to_dict()

    else:
        return form.errors


@pm_chat_bp.route('/<int:id>/messages')
def get_all_messages_by_channel_id(id):
    pm_chat = PmChat.query.get(id)
    
    if pm_chat:
        pm_chat_messages = Message.query.filter(Message.pm_chat_id == id).all()
        messages_list = { 'messages' : [message.to_dict() for message in pm_chat_messages]}
        return messages_list
    else:
        return { "error": "Pm Chat not found", "errorCode" : 404 }, 404
