


def user_id_from(user):
    return user['id']

def get_ids_from_list_of_users(users):
    return [ user_id_from(user) for user in users]

def get_ids_from_list_of_users_with_map(users):
    return map(lambda user:user['id'],users)

def get_user_ids_imperative(users):
    results = []
    for user in users:
        results.append(user['id'])
    return results