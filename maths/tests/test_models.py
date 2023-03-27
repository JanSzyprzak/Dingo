from django.test import TestCase
from maths.models import Math, Result


class MathModelTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="add", a=1, b=2)
        Math.objects.create(operation="sub", a=20, b=30)

    def test_math_str(self):
        m1 = Math.objects.get(operation="add")
        m2 = Math.objects.get(operation="sub")

        self.assertEqual(str(m1), "id:1, a=1, b=2, op=add")
        self.assertEqual(str(m2), "id:2, a=20, b=30, op=sub")



class ResultModelTest(TestCase):

    def setUp(self):
        Result.objects.create(value=10)
        Result.objects.create(error="0 division error!")

    def test_result_str(self):
        r1 = Result.objects.get(value=10)
        r2 = Result.objects.get(error="0 division error!")

        self.assertEqual(str(r1), 'value: 10.0 | error: None')
        self.assertEqual(str(r2), 'value: None | error: 0 division error!')