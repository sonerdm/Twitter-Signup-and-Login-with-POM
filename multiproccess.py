import unittest
from testAll_with_chrome import TestHome
from testAll_with_chrome import TestSignUpPage
from testAll_with_chrome import TestSignInPage
from multiprocessing import Pool


def run_test(test_to_run):
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_to_run)


tests = [TestHome("test_TC001_check_buttons"),
         TestHome("test_TC002_assert_title"),
         TestSignUpPage("test_TC003_create_acc"),
         TestSignInPage("test_TC004_log_in")]

if __name__ == "__main__":
    with Pool(3) as p:
        p.map(run_test, tests)
