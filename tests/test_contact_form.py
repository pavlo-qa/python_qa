# -*- coding: utf-8 -*-
from engine.helpers.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_happy_flow_case(app):
    app.navigate_to_contacts_page()
    # fill in and submit the contact form
    app.fill_in_first_name()
    app.fill_in_surname()
    app.select_topic()
    app.fill_in_email()
    app.fill_in_description()
    app.submit_form()
