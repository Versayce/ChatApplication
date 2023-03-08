from app.models import db, PmChat, User, environment, SCHEMA


def seed_pm_chats():

    pm_chat1 = PmChat(
        name='General', 
    )

    pm_chat2 = PmChat(
        name='Private Chat',   
    )


    all_chats = [ pm_chat1, pm_chat2 ]
    tyson = User.query.filter(User.username == 'Iron Mike').first()
    pidgeon = User.query.filter(User.username == 'Pidgeon').first()
    demo1 = User.query.filter(User.username == 'DemoUser1').first()
    demo2 = User.query.filter(User.username == 'DemoUser2').first()
    
    
    tyson.pm_chats.append(pm_chat1)
    pidgeon.pm_chats.append(pm_chat2)
    demo1.pm_chats.append(pm_chat1)
    demo2.pm_chats.append(pm_chat2)
    print('============ SEEDING CHAT DATA ============', '\n', demo1.pm_chats[0].to_dict(), '\n', '============ SEEDING CHAT DATA ============')

    for chat in all_chats:
        db.session.add(chat)
    db.session.commit()

    print('Seeded Chats')



def undo_pm_chats():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.channels RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM channels")

    db.session.commit()
