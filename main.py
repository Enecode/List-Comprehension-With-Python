users = [
    {
        'name': 'Hadizat',
        'age': 21,
        'gender': 'Female',
        'username': 'deezah',
        'is_verify': True,
        'tweets': [
            {'content': 'PO for President', 'Likes': 450, 'retweet': 233},
            {'content': 'PO for President', 'Likes': 450, 'retweet': 233}
        ]
    },
    {
        'name': 'Ibrahim',
        'age': 31,
        'gender': 'Male',
        'username': 'ibro',
        'is_verify': True,
        'tweets': [
            {'content': 'Programming for better life', 'Likes': 50, 'retweet': 33},
            {'content': 'Programming for solving daily life issue', 'Likes': 50, 'retweet': 33}
        ]
    },
    {
        'name': 'Rachael',
        'age': 16,
        'gender': 'Female',
        'username': 'betty',
        'is_verify': True,
        'tweets': [
            {'content': '.', 'Likes': 2450, 'retweet': 2338},
            {'content': 'thinking about Amezing', 'Likes': 2450, 'retweet': 233}
        ]
    },
    {
        'name': 'Dorris',
        'age': 21,
        'gender': 'Female',
        'username': 'chimmamanda',
        'is_verify': False,
        'tweets': [
            {'content': 'I love Chimamanda', 'Likes': 5450, 'retweet': 3233},
            {'content': 'Feminist is the goal', 'Likes': 6450, 'retweet': 2233}
        ]
    },
    {
        'name': 'Hadizat',
        'age': 21,
        'gender': 'Female',
        'username': 'deezah',
        'is_verify': True,
        'tweets': [
            {'content': 'Reflection keep you reflected', 'Likes': 450, 'retweet': 233},
            {'content': 'How to get more likes on tweet', 'Likes': 450, 'retweet': 233}
        ]
    },
    {
        'name': 'Derrick',
        'age': 21,
        'gender': 'Male',
        'username': 'standby_gen',
        'is_verify': False,
        'tweets': [
            {'content': 'PO for President', 'Likes': 450, 'retweet': 233},
            {'content': 'PO for President', 'Likes': 450, 'retweet': 233}
        ]
    },
    {
        'name': 'phisic',
        'age': 21,
        'gender': 'Female',
        'username': 'ceo_whistle',
        'is_verify': True,
        'tweets': [
        ]
    }
]
no_of_users = len(users)
usernames = {user['username'] for user in users}
print(usernames)

users_age = {user['age'] for user in users}
print(users_age)

name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]
print(name_and_age)

average_age_of_users = round(sum([user['age'] for user in users]) / len(users))
print(average_age_of_users)

# female_users = [user for user in users if user['gender'] == 'Female']
# inactive_users = [user for user in users if len(user['tweets']) == 0]
# print(female_users)
