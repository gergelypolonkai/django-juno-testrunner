import time

from django.test import TestCase, TransactionTestCase

try:
    # Django 1.6
    from django.utils import unittest
except ImportError:
    # Django 1.7+ because bundled unittest is going away
    import unittest


class JunorunnerTestCase(TestCase):

    def test_can_run_tests(self):
        pass

    def test_counts_tests_correctly(self):
        """
        Added this test to make sure the number of tests != number of test cases
        (so that we can assert the total count is correct when running tests in parallel)
        """
        pass


class JunorunnerTransactionTestCase(TransactionTestCase):

    def test_can_run_transaction_bound_tests(self):
        pass

    def test_erring_test(self):
        self.this_method_clearly_doesnt_exist()

    def test_failing_test(self):
        self.assertEqual(1, 2)

    @unittest.skip("Let's skip this")
    def test_skipped(self):
        pass

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2, "Well, this was expected")

    @unittest.expectedFailure
    def test_unexpected_success(self):
        self.assertEquals(1, 1, "You don't say...")
