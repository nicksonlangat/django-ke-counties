from ..models import County
from ..tests.base_test import BaseTest


class CountyTests(BaseTest):
    def test_get_counties(self):
        counties = County.objects.all()
        assert len(counties) == 47
