from account.models import UserProfile


def prevent_name_update(strategy, details, user=None, *args, **kwargs):
    if user:
        if user.first_name and user.last_name:
            details['first_name'] = user.first_name
            details['last_name'] = user.last_name
    return


def save_profile_picture(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        picture_url = response.get('picture')  # آدرس عکس پروفایل از Google
        if picture_url:
            # در اینجا باید به UserProfile دسترسی پیدا کنید
            profile, created = UserProfile.objects.get_or_create(user=user)  # به پروفایل کاربر دسترسی پیدا کنید
            profile.profile_picture = picture_url
            profile.save()
