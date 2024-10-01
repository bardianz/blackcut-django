def prevent_name_update(strategy, details, user=None, *args, **kwargs):
    if user:
        if user.first_name and user.last_name:
            details['first_name'] = user.first_name
            details['last_name'] = user.last_name
    return


def save_profile_picture(backend, user, response, *args, **kwargs):
    try:
        if backend.name == 'google-oauth2':
            picture_url = response.get('picture')  # آدرس عکس پروفایل از Google
            if picture_url and not user.profile_picture:
                user.profile_picture = picture_url
                user.save()
    except:
        print("Error")