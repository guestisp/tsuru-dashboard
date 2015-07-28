from django.test import TestCase
from django.core.urlresolvers import reverse

from mock import patch


class IndexTestCase(TestCase):
    @patch("auth.views.token_is_valid")
    def test_index(self, token_is_valid):
        token_is_valid.return_value = True
        with self.settings(SESSION_ENGINE='django.contrib.sessions.backends.file'):
            session = self.client.session
            session['tsuru_token'] = "beare token"
            session.save()

            response = self.client.get(reverse("autoscale"))
            self.assertTemplateUsed(response, "autoscale/index.html")
