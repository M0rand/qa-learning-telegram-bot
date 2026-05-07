from data.achievements import achievements


user_achievements = {}


def unlock_achievement(user_id, key):

    if user_id not in user_achievements:

        user_achievements[user_id] = []

    if key not in user_achievements[user_id]:

        user_achievements[user_id].append(key)

        return achievements[key]

    return None


def get_achievements(user_id):

    return user_achievements.get(user_id, [])