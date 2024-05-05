class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        pass


class TestSuite:
    def __init__(self):
        self.test_cases = []

    def add_test(self, test_case):
        self.test_cases.append(test_case)

    def run(self):
        results = []
        for test_case in self.test_cases:
            result = {'name': test_case.name, 'status': 'Passed'}
            try:
                test_case.run()
            except Exception as e:
                result['status'] = 'Failed'
                result['error_message'] = str(e)
            results.append(result)
        return results


class TestRunner:
    @staticmethod
    def run(test_suite):
        results = test_suite.run()
        print("\nTest Results:")
        for result in results:
            print(f"Test Case: {result['name']}, Status: {result['status']}")
            if 'error_message' in result:
                print(f"  Error: {result['error_message']}")
        passed_tests = sum(1 for result in results if result['status'] == 'Passed')
        failed_tests = sum(1 for result in results if result['status'] == 'Failed')
        print(f"\nSummary: {passed_tests} Passed, {failed_tests} Failed")


class SampleTestCase1(TestCase):
    def run(self):
        assert 1 + 1 == 2, "1 + 1 should be equal to 2"

class SampleTestCase2(TestCase):
    def run(self):
        assert 2 * 3 == 6, "2 * 3 should be equal to 6"


test_case_1 = SampleTestCase1("Test Case 1")
test_case_2 = SampleTestCase2("Test Case 2")

test_suite = TestSuite()
test_suite.add_test(test_case_1)
test_suite.add_test(test_case_2)

TestRunner.run(test_suite)
