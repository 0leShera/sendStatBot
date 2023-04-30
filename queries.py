from connect import get_db_connection


# Count users
def get_all_user_count():
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


def get_new_user_count(date):
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM users WHERE date(created_at) = %s", (date,))
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


# Count clubs
def get_all_clubs_count():
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM clubs")
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


def get_new_clubs_count(date):
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM clubs WHERE date(created_at) = %s", (date,))
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


# Count clubs subscribers
def get_all_subscribers_count():
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM club_users")
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


def get_new_subscribers_count(date):
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM club_users WHERE date(created_at) = %s", (date,))
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


# Count posts
def get_all_posts_count():
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM posts")
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


def get_new_posts_count(date):
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM posts WHERE date(created_at) = %s", (date,))
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


# Count photos
def get_all_photos_count():
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM uploads")
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


def get_new_photos_count(date):
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM uploads WHERE date(created_at) = %s", (date,))
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


# Count likes
def get_all_likes_count():
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM likes")
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


def get_new_likes_count(date):
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM likes WHERE date(created_at) = %s", (date,))
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


# Count comments
def get_all_comments_count():
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM comments")
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count


def get_new_comments_count(date):
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    cur.execute("SELECT COUNT(*) FROM comments WHERE date(created_at) = %s", (date,))
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count

