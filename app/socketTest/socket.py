from flask_socketio import SocketIO, emit, join_room, leave_room, send
import os
from app.models import db, Message

socketio = SocketIO(logger=True, engineio_logger=True, cors_allowed_origins="*")



@socketio.on("chat")
def handle_chat(data):
    room = data["roomId"]
    emit("chat", data, room=room)
    print('', '\n', '===========INSIDE OF CHAT ROUTE===========', data, '\n', '')

# @socketio.on("chat")
# def chat_handler(data):
#     room = data["id"]
#     user = data["user"]
#     message = data["msg"]
#     send(user + ": " + message, to=room)

@socketio.on("join")
def channel_join(data):
    name = data["user"]
    room = data["roomId"]
    join_room(room)
    send(name + ' has entered the room.', room=room)
    print('=========== INSIDE OF OUR SOCKET JOIN ROUTE ==============', '\n', data, '\n', '=========== INSIDE OF OUR SOCKET JOIN ROUTE ==============')
    
@socketio.on("leave")
def channel_leave(data):
    username = data['user']
    room = data['roomId']
    leave_room(room)
    send(username + ' has left the room.', room=room)
    print('***************************LEAVING ROOM**************************','\n', data, '\n', '***************************LEAVING ROOM**************************')
    
    
    
    
# Routes for pm chatrooms below: #
@socketio.on("pm_chat")
def handle_pm_chat(data):
    room = f'pm{data["roomId"]}'
    emit("chat", data, room=room)
    print('', '\n', '=========== INSIDE OF CHAT ROUTE ===========', '\n', data, '\n', '=========== INSIDE OF CHAT ROUTE ===========', '\n', '')


@socketio.on("pm_join")
def pm_chatroom_join(data):
    name = data["user"]
    room = f'pm{data["roomId"]}'
    join_room(room)
    send(name + ' has entered the room.', room=room)
    print('============= SOCKET PM JOIN ==============', '\n', room, '\n', '============= SOCKET PM JOIN ==============')
    
    
@socketio.on("pm_leave")
def pm_chatroom_leave(data):
    username = data['user']
    room = data['roomId']
    leave_room(room)
    send(username + ' has left the room.', room=room)
    print('', '\n', '============= LEAVING ROOM ==============','\n', data, '\n', '============= LEAVING ROOM ==============', '\n', '')
