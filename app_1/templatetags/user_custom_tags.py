from  django import template
# from ..models import register_info_tabel, request_for_add_balance_with_info, add_user_balance
register = template.Library()

# reguler order count



@register.simple_tag
def count_get_user(request):
    user_Register_id = request.session.get('Login_Email_Address')

    return user_Register_id




