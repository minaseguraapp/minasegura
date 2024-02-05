from apps.mine.models import Mine


def get_user_mine(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        first_mine = Mine.objects.filter(manager=request.user).first()
        if first_mine:
            return {
                "user_mine": first_mine
            }
    return {
        "user_mine": None
    }
