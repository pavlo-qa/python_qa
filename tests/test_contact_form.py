# -*- coding: utf-8 -*-
from engine.helpers.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_happy_flow_case(app):
    app.navigator.navigate_to_contacts_page()
    # fill in and submit the contact form
    app.form.fill_in_first_name()
    app.form.fill_in_surname()
    app.form.select_topic()
    app.form.fill_in_email()
    app.form.fill_in_description()
    app.form.submit_form()
    # go back to the main page
    app.navigator.go_to(app.home)
