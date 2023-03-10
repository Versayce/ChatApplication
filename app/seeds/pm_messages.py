from app.models import db, PmMessage, MessageImage, environment, SCHEMA


def seed_pm_messages():
    pm_message1 = PmMessage(
        body='Test1', chat_id=1, author_id=2
    )
    pm_message2 = PmMessage(
        body='Test2', chat_id=1, author_id=3
    )
    pm_message3 = PmMessage(
        body='Test3', chat_id=1, author_id=2
    )
    pm_message4 = PmMessage(
        body='Test4', chat_id=1, author_id=3
    )
    pm_message5 = PmMessage(
        body='Test5', chat_id=1, author_id=2,
    )
    pm_message6 = PmMessage(
        body='Test6', chat_id=2, author_id=4,
    )
    pm_message7 = PmMessage(
        body='Test7', chat_id=2, author_id=1,
    )
    
    db.session.add(pm_message1)
    db.session.add(pm_message2)
    db.session.add(pm_message3)
    db.session.add(pm_message4)
    db.session.add(pm_message5)
    db.session.add(pm_message6)
    db.session.add(pm_message7)
    db.session.add(pm_message8)
    db.session.add(pm_message9)
    db.session.add(pm_message10)
    db.session.add(pm_message11)
    db.session.commit()
    
    print('Pm Chat Messages Seeded')
    
# def seed_pm_message_images():
#     image1 = MessageImage(
#         image_url='/static/images/message_images/assault-dog.jpeg', message_id=3
#     )
#     image2 = MessageImage(
#         image_url='/static/images/message_images/beef-cat.jpg', message_id=5
#     )
#     image3 = MessageImage(
#         image_url='/static/images/message_images/footzo.png', message_id=7
#     )
#     image4 = MessageImage(
#         image_url='/static/images/message_images/hampster.jpg', message_id=9
#     )
#     image5 = MessageImage(
#         image_url='/static/images/message_images/rogan-tyson.jpg', message_id=11
#     )
    
#     db.session.add(image1)
#     db.session.add(image2)
#     db.session.add(image3)
#     db.session.add(image4)
#     db.session.add(image5)
#     db.session.commit()
    
def undo_pm_messages():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.pm_messages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM messages")
        
    db.session.commit()
    
# def undo_pm_message_images():
#     if environment == "production":
#         db.session.execute(f"TRUNCATE table {SCHEMA}.pm_message_images RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute("DELETE FROM message_images")
        
#     db.session.commit()
