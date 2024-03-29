from .db import db, environment, SCHEMA, add_prefix_for_prod
    
chat_users = db.Table(
    'chat_users',
    db.Model.metadata,
    db.Column('chat_id', db.Integer, db.ForeignKey(add_prefix_for_prod('pm_chats.id')), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True))

if environment == 'production':
    chat_users.schema = SCHEMA
    
class PmChat(db.Model):
    __tablename__ = 'pm_chats'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    pm_messages = db.relationship('PmMessage', back_populates='chat', cascade='all, delete')
    
    # users = db.relationship('User', back_populates='chat')
    
    pmchat_users = db.relationship('User', secondary=chat_users, back_populates="pm_chats")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'users': [user.to_dict_pm() for user in self.pmchat_users],
            'messages': [message.to_dict() for message in self.pm_messages],
        }
