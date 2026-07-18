import allure
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tools.assertions.base import assert_status_code
from http import HTTPStatus
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
import pytest
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity



@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)

@pytest.mark.authentication
@pytest.mark.regression
class TestAuthentication:
    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.LOGIN)
    @allure.sub_suite(AllureStory.LOGIN)
    @allure.title("Login with correct email and password")
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):

        request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
        )

        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate_json_schema(response.json(), LoginResponseSchema.model_json_schema())


