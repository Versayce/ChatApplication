from app.models import db, Server, environment, SCHEMA, User


def seed_servers():

    server1 = Server(
        name = 'Mike Tyson Mysteries',
        server_image = 'http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcSFe9ShSurjuKqi5axvhoY3162zMSRNn6yy66o3vKH9V-GkmocA8DjSJSYDnddMvjrYlGKwoLccdB7yk2c',
        owner_id = 1,
    )

    server2 = Server(
        name = 'Boxing',
        server_image = 'http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcSFe9ShSurjuKqi5axvhoY3162zMSRNn6yy66o3vKH9V-GkmocA8DjSJSYDnddMvjrYlGKwoLccdB7yk2c',
        owner_id = 2,
    )

    server3 = Server(
        name = 'Tyson\'s Tigers',
        server_image = 'http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcSFe9ShSurjuKqi5axvhoY3162zMSRNn6yy66o3vKH9V-GkmocA8DjSJSYDnddMvjrYlGKwoLccdB7yk2c',
        owner_id = 3,
    )

    server4 = Server(
        name = 'Face Tattoos',
        server_image = 'http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcSFe9ShSurjuKqi5axvhoY3162zMSRNn6yy66o3vKH9V-GkmocA8DjSJSYDnddMvjrYlGKwoLccdB7yk2c',
        owner_id = 4,
    )

    all_servers = [ server1, server2, server3, server4 ]
    all_users = User.query.all()
    for i in range(len(all_users)):
        for j in range(len(all_servers)):
            all_users[i].servers.append(all_servers[j])

    for server in all_servers:
        db.session.add(server)
    db.session.commit()

    print("Servers Seeded")


def undo_server():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.servers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM servers")

    db.session.commit()
