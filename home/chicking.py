from  customer.models import UserOTP


def chickingvalue(request):
    try:
        q = UserOTP.objects.get(email=request.user.email)
        if request.user.is_authenticated:
            if q.is_email_verified:
                return True
            else:
                return False
        else:
            return False
    except:
        return False
