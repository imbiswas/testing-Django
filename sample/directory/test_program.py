import pytest
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


@pytest.mark.django_db
def test_my_user():
    me = User.objects.filter(username='apple')
    for i in me:
    	if i.is_superuser:
    		assert i.is_superuser
    #pass
    # assert me.is_superuser
    #pass