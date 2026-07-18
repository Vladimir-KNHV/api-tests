import pytest
from clients.exercises.exercises_client import ExercisesClient
from fixtures.courses import CourseFixture
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, GetExercisesQuerySchema, \
GetExercisesResponseSchema
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema
from fixtures.exercises import ExerciseFixture
from clients.errors_schema import InternalErrorResponseSchema
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity



@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
@allure.suite(AllureFeature.EXERCISES)
@pytest.mark.regression
@pytest.mark.exercises
class TestExercises:
    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.title("Create exercise")
    def test_create_exercise(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture
    ):
        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), CreateExerciseResponseSchema.model_json_schema())

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.title("Get exercise")
    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(response.json(), GetExerciseResponseSchema.model_json_schema())

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.title("Update exercise")
    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(exercise_id=function_exercise.response.exercise.id, request=request)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), UpdateExerciseResponseSchema.model_json_schema())

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    @allure.title("Delete exercise")
    def test_delete_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        delete_response = exercises_client.delete_exercise_api(exercise_id=function_exercise.response.exercise.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_exercise_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), InternalErrorResponseSchema.model_json_schema())

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    @allure.title("Get exercises")
    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture,
            function_exercise: ExerciseFixture
    ):
        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(query)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_get_exercises_response(response_data, [function_exercise.response])
        validate_json_schema(response.json(), GetExercisesResponseSchema.model_json_schema())