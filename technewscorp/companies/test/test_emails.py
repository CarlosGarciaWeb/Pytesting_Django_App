from unittest.mock import patch
from django.test import TestCase, Client
from django.core import mail
import json
import os

class EmailUnitTest(TestCase):
    def test_send_email_should_succeed(self) -> None:
        with self.settings (
            EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend"
        ):
            self.assertEqual(len(mail.outbox), 0)
            # send email
            mail.send_mail(
                subject="Test subject here",
                message="test message here",
                from_email="testemail@gmail.com",
                recipient_list=["testemail2@gmail.com"],
                fail_silently=False,
            )
            # ensure one email was sent
            self.assertEqual(len(mail.outbox), 1)

            # verify subject of email
            self.assertEqual(mail.outbox[0].subject, "Test subject here")


    def test_send_email_without_arguments_should_send_empty_email(self) -> None:
        client = Client()
        with patch(
            "companies.views.send_company_email"
        ) as mocked_send_email:
            response = client.post(path='/send-email')
            response_content = json.loads(response.content)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_content['status'], 'success')
            self.assertEqual(response_content['info'], 'email sent successfully')
            mocked_send_email(
                subject=None,
                message=None,
                from_email=os.environ.get("TEST_EMAIL"),
                recipient_list=[os.environ.get("TEST_EMAIL")]
            )

    def test_send_email_with_get_verb_should_fail(self) -> None:
        client = Client()
        response = client.get(path="/send_email")
        assert response.status_code == 405
        assert json.loads(response.content) == {
    "detail": "Method \"GET\" not allowed."
}