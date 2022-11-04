from unittest.mock import patch
from django.test import TestCase, Client
from django.core import mail
import json
import os
import pytest


def test_send_email_should_succeed(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    assert len(mailoutbox) == 0
    # send email
    mail.send_mail(
        subject="Test subject here",
        message="test message here",
        from_email="testemail@gmail.com",
        recipient_list=["testemail2@gmail.com"],
        fail_silently=False,
    )
    # ensure one email was sent
    assert len(mailoutbox) == 1

    # verify subject of email
    assert mailoutbox[0].subject == "Test subject here"


def test_send_email_without_arguments_should_send_empty_email(client) -> None:
    with patch("companies.views.send_company_email") as mocked_send_email:
        response = client.post(path="/send-email")
        response_content = json.loads(response.content)
        assert response.status_code == 200
        assert response_content["status"] == "success"
        assert response_content["info"] == "email sent successfully"
        mocked_send_email(
            subject=None,
            message=None,
            from_email=os.environ.get("TEST_EMAIL"),
            recipient_list=[os.environ.get("TEST_EMAIL")],
        )


def test_send_email_with_get_verb_should_fail(client) -> None:
    response = client.get(path="/send-email")
    assert response.status_code == 405
    assert json.loads(response.content) == {"detail": 'Method "GET" not allowed.'}
