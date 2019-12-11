"""This is dedicated to testing the click cli.py utility"""

from click.testing import CliRunner
from scli import search

def test_scli():
  runner = CliRunner()
  result = runner.invoke(search, ['--path', '.'])
  assert result.exit_code == 0
  assert '.py' in result.output