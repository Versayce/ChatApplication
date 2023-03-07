from app.models import db, PmChat, environment, SCHEMA


def seed_pm_chats():

    pm_chat1 = PmChat(
        name='General', 
    )

    pm_chat2 = PmChat(
        name='Private Chat',   
    )


    all_chats = [ pm_chat1, pm_chat2 ]

    for chat in all_chats:
        db.session.add(chat)
    db.session.commit()

    print('Seeded Channels')



def undo_pm_chats():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.channels RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM channels")

    db.session.commit()
