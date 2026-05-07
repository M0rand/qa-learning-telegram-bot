user_xp = {}

user_progress = {}


def add_xp(user_id, xp):

    if user_id not in user_xp:
        user_xp[user_id] = 0

    user_xp[user_id] += xp

    return user_xp[user_id]


def get_xp(user_id):

    return user_xp.get(user_id, 0)


def set_progress(user_id, lesson):

    user_progress[user_id] = lesson


def get_progress(user_id):

    return user_progress.get(user_id, 1)