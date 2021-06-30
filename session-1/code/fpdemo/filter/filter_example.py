


def get_users_of_gender(users,gender):
    return  (user for user in users if user['gender'] == gender)


def get_users_of_gender_filter(users,gender):
    return filter(lambda user:user['gender'] == gender,users)


def get_users_of_gender_imperative(users,gender):
    results = []
    for user in users:
        if(user['gender'] == gender):
            results.append(user)
    return results
