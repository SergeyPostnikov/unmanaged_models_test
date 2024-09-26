import pytest
from django.db import connection
from un_tub_p.un_tab.models import UnmanagedTable


# @pytest.fixture(scope="function")
# def create_db(db):
#     with connection.schema_editor() as schema_editor:
#         schema_editor.create_model(UnmanagedTable)


def test_test():
    assert True


# @pytest.mark.django_db
# def test_user_creation(create_db) -> None:
#     assert not UnmanagedTable.objects.all()
