from unittest import TestCase
from unittest import mock
from unittest.mock import patch

from io import StringIO

import main as MainClass


class main_test(TestCase):
    def test_display_shows_all_fields(self):

        with patch('sys.stdout', new=StringIO()) as fake_out:
            MainClass.display_board()
            self.assertEqual(fake_out.getvalue(), "1")
