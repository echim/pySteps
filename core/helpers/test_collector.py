from core.enums.pytest_outcome import TestOutcome
from _pytest.runner import TestReport


def collect_test_results(report: TestReport):
    if report.when == 'call':
        test_results = {
            'test': report.nodeid,
            'status': report.outcome,
            'duration': report.duration
        }
        if report.outcome == TestOutcome.FAILED.value:
            test_results['error'] = report.longrepr
        print(test_results)
