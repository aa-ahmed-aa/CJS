import pytest

@pytest.mark.django_db
def test_user_count():
	assert User.objects.count() == 0
