def get_level(xp):

    if xp >= 1500:
        return "Senior QA"

    elif xp >= 700:
        return "Middle QA"

    elif xp >= 300:
        return "Strong Junior"

    elif xp >= 100:
        return "Junior QA"

    else:
        return "Intern"