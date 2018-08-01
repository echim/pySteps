import datetime, json

from _pytest.runner import TestReport

from core.default_settings import DefaultSettings
from core.enums.pytest_outcome import TestOutcome
from core.helpers.os_helpers import get_project_root_path, os


def send_result_to_log_file(test_result):
    run_log_file = os.path.join(get_project_root_path(), 'tests', DefaultSettings.LOG_FILE_NAME.value)
    with open(run_log_file, mode='a', encoding='utf-8') as prev_content:
        json.dump(test_result, prev_content, indent=4)


def send_result_to_endpoint(test_result, endpoint):
    pass


def collect_test_results(report: TestReport):
    if report.when == 'call':
        test_result = {
            'timestamp': datetime.datetime.now().timestamp(),
            'test': report.nodeid,
            'status': report.outcome,
            'duration': report.duration
        }
        if report.outcome == TestOutcome.FAILED.value:
            test_result['error'] = str(report.longrepr)

        send_result_to_log_file(test_result)
