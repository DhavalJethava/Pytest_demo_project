import allure
import pytest
from allure_commons import plugin_manager
from allure_commons.lifecycle import AllureLifecycle
from allure_commons.model2 import TestResult

from mains.driver_utils import DriverUtils
from mains import config_utils
driver_utils = DriverUtils()


def pytest_configure():
    config_utils.clear_report_dir()


def pytest_bdd_after_scenario(request, feature, scenario):

    allure.attach.file(driver_utils.take_screenshot(), "screenshot: " + scenario.name, allure.attachment_type.PNG)
    driver_utils.teardown_driver()


def custom_write_test_case(self, uuid=None):
    test_result = self._pop_item(uuid=uuid, item_type=TestResult)
    if test_result:
        if test_result.parameters:
            adj_parameters = []
            for param in test_result.parameters:
                if param.name != '_pytest_bdd_example':
                    adj_parameters.append(param)
            test_result.parameters = adj_parameters

        plugin_manager.hook.report_result(result=test_result)


AllureLifecycle.write_test_case = custom_write_test_case
