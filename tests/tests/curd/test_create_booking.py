import allure
import pytest


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that created booking status and Booking id should not be Null")
    @allure.description("Creating a Booking from the payload and verify that booking id should not be null")
    def test_create_booking_positive(self):
        # 1,2,3,4,5
        pass
