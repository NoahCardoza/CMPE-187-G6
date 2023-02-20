import io
from unittest.mock import patch

from main import Result, consider_student


def join_lines(lines):
    return '\n'.join(lines) + '\n'

def join_stdin_lines(*lines):
    return io.StringIO(join_lines(lines))

@patch('sys.stdin', join_stdin_lines('17'))
def test_consider_student_1():
    assert consider_student() == Result.INELIGIBLE

@patch('sys.stdin', join_stdin_lines('20', 'y'))
def test_consider_student_2():
    assert consider_student() == Result.ELIGIBLE

@patch('sys.stdin', join_stdin_lines('20', 'n', 'y'))
def test_consider_student_3():
    assert consider_student() == Result.ELIGIBLE

@patch('sys.stdin', join_stdin_lines('20', 'n', 'n', 'y'))
def test_consider_student_4():
    assert consider_student() == Result.ELIGIBLE

@patch('sys.stdin', join_stdin_lines('20', 'n', 'n', 'n', 'y'))
def test_consider_student_5():
    assert consider_student() == Result.ELIGIBLE

@patch('sys.stdin', join_stdin_lines('20', 'n', 'n', 'n', 'n', '3000'))
def test_consider_student_6():
    assert consider_student() == Result.DEAN

@patch('sys.stdin', join_stdin_lines('20', 'n', 'n', 'n', 'n', '8000'))
def test_consider_student_7():
    assert consider_student() == Result.INELIGIBLE