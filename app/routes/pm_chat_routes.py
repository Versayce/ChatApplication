from flask import Blueprint, request
from ..models import PmChat, Message, User, db
from ..forms.pm_chat_form import PmChatForm


pm_chat_bp = Blueprint('chats', __name__)

@pm_chat_bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def pm_chat_by_id(id):
    pm_chat = PmChat.query.get(id)

    if pm_chat:

        if request.method == 'GET':
            pm_chat_dict = pm_chat.to_dict()
            # pm_chat_dict['pm_messages'] = [message.to_dict() for message in pm_chat.pm_messages]
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

    return { "error": "Chat not found", "errorCode" : 404 }, 404


@pm_chat_bp.route('/new', methods=['POST'])
def new_pm_chat():
    form = PmChatForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_pm_chat = PmChat()
        print('WITHIN NEW CHAT ROUTE -------------- BACKEND --------------- ', new_pm_chat)
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


@pm_chat_bp.route('/checkavailability/<int:user1Id>/<int:user2Id>')
def check_if_pm_exists(user1Id, user2Id):
    user1 = User.query.get(user1Id)
    user2 = User.query.get(user2Id)
    chats = PmChat.query.filter(PmChat.pmchat_users.contains(user1), PmChat.pmchat_users.contains(user2)).all()
    if chats:
        return { "error": "Pm Chatroom already exists", "errorCode" : 403 }, 403
    else:
        return {'existingPmChats' : [chat.to_dict() for chat in chats]}
