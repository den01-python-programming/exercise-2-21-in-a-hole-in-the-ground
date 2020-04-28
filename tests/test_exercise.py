import pytest
from src.exercise import main

def test_exercise(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "In a hole in the ground there lived a method\n", "Should read 'In a hole in the ground there lived a method'"
