import datetime, json

from _pytest.runner import TestReport

from core.default_settings import DefaultSettings
from core.enums.pytest_outcome import TestOutcome
from core.helpers.os_helpers import get_project_root_path, os


def send_result_to_log_file(test_result):
    run_log_file = os.path.join(get_project_root_path(), 'tests', DefaultSettings.LOG_FILE_NAME.value)

    if not os.path.exists(run_log_file):
        with open(run_log_file, 'a'):
            os.utime(run_log_file, None)
    else:
        with open(run_log_file) as json_file:
            try:
                new_data = json.load(json_file)
            except Exception:
                new_data = {'tests': []}

            new_data['tests'].append(test_result)
            with open(run_log_file, mode='w', encoding='utf-8') as prev_content:
                json.dump(new_data, prev_content, indent=4, ensure_ascii=False)


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

        for extra_infos in report.user_properties:
            if extra_infos and extra_infos[0]:
                test_result[extra_infos[0]] = extra_infos[1]

        send_result_to_log_file(test_result)
