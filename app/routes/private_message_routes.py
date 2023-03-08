from flask import Blueprint, render_template, redirect, request

from app.forms.pm_message_form import PmMessageForm
from ..models import PmMessage, db


private_message_bp = Blueprint('pm_messages', __name__)


@private_message_bp.route('/new', methods=['POST'])
def new_private_message():
    form = PmMessageForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_pm_message = PmMessage()
        form.populate_obj(new_pm_message)

        db.session.add(new_pm_message)
        db.session.commit()
        return new_pm_message.to_dict()

    else:
        return form.errors


@private_message_bp.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def pm_message_by_id(id):
    pm_message = PmMessage.query.get(id)

    if pm_message:

        if request.method == 'GET':
            pm_message_dict = pm_message.to_dict()
            pm_message_dict['author'] = pm_message.author.to_dict()
            return pm_message_dict

        if request.method == 'DELETE':
            db.session.delete(pm_message)
            db.session.commit()
            return {'message': 'Message Deleted!'}

        if request.method == 'PUT':
            form = PmMessageForm()
            form['csrf_token'].data = request.cookies['csrf_token']
            if form.validate_on_submit():
                pm_message.body = form.data['body']
                db.session.commit()
                return pm_message.to_dict()

            return form.errors

    return { "error": "Message not found", "errorCode" : 404 }, 404
