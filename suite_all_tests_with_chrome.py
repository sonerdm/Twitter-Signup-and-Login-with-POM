import unittest
from testAll_with_chrome import TestHome
from testAll_with_chrome import TestSignUpPage
from testAll_with_chrome import TestSignInPage


def suite():
    suite = unittest.TestSuite()

    # HomePage Tests
    suite.addTest(TestHome("test_TC001_check_buttons"))
    suite.addTest(TestHome("test_TC002_assert_title"))

    # TestSignUpPage page Tests
    suite.addTest(TestSignUpPage("test_TC003_create_acc"))

    # TestSignInPage page Tests
    suite.addTest(TestSignInPage("test_TC004_log_in"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    runner.run(suite)
