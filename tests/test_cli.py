"""This is dedicated to testing the click cli.py utility"""

from click.testing import CliRunner
from cli import add

def test_cli():
  runner = CliRunner()
  result = runner.invoke(add)
  assert result.exit_code == 0
  assert 'One + my library code = 2' in result.output