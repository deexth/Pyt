#here we are going to create 2 lists for comparing.
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can go ahead and post if you wish.")
#python is checking in 5 if the user is not in banned_users, if the user was in that list the nothing would
#displayed since there is no else used.