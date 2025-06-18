import json
import os

import allure
import pytest


def parse_failed_tests_from_json():
    if not os.path.exists('pytest_log.json'):
        print('File pytest_log.json not found. Run tests first with --report-log option.')
        return []

    with open('pytest_log.json') as f:
        log_data = [json.loads(line) for line in f if line.strip()]

    failed_tests = []
    for item in log_data:
        if item.get('when') == 'call' and item.get('outcome') == 'failed':
            nodeid = item.get('nodeid')
            if nodeid:
                failed_tests.append(nodeid)

    return failed_tests


def create_reruns_file(failed_tests):
    with open('failed_tests.txt', 'w') as f:
        for test in failed_tests:
            f.write(f"{test}\n")


def remove_temp_files():
    if os.path.exists('./scripts/failed_tests.txt'):
        os.remove('./scripts/failed_tests.txt')
    if os.path.exists('./scripts/pytest_log.json'):
        os.remove('./scripts/pytest_log.json')


def run_failed_tests():
    with allure.step('Перезапуск упавших тестов'):
        failed_tests = parse_failed_tests_from_json()

        if not failed_tests:
            print('No failed tests found in pytest_log.json')
            return

        create_reruns_file(failed_tests)

        with open('failed_tests.txt', 'r') as f:
            tests_to_run = [line.strip() for line in f if line.strip()]

        if not tests_to_run:
            print('No tests found in failed_tests.txt')
            return

        print(f'Running {len(tests_to_run)} tests from failed_tests.txt')

        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.chdir(project_root)

        pytest_args = [
            '-v',
            '--tb=short',
            '-o', 'addopts=',
            '-p', 'no:logging',
            '--alluredir=./scripts/allure-rerun-results',
            '--clean-alluredir',
            *tests_to_run
        ]

        exit_code = pytest.main(pytest_args)
        print(f'Failed tests run completed with exit code: "{exit_code}: {exit_code.name}"')

        remove_temp_files()


if __name__ == '__main__':
    run_failed_tests()
