import pytest
from madlib import file_open, collect_answer, final_product


@pytest.mark.skip('pending')
def test_file_open():
    expected = """Make Me A Video Game!
I the {} and {} {} have {} {}'s {} sister and plan to steal her {} {}!
What are a {} and backpacking {} to do? Before you can help {}, you'll have
to collect the {} {} and {} {} that open up the {} worlds connected to A {}
Lair. There are {} {} and {} {} in the game, along with hundreds of other
goodies for you to find."""
    actual = file_open('madlib.txt')
    assert expected == actual


def test_collect_answer():
    expected = ['pretty', 'violent', 'Lily', 'ran', 'Mel', 'large', 'sad',
                'tables', 'hippo', 'mouse', 'Annie', 'happy', 'books', 'small',
                'rings', '44', 'Andy', '3', 'pens', '5', 'tabs']
    actual = collect_answer()
    assert expected == actual


@pytest.mark.skip('pending')
def test_final_product():
    expected = """Make Me A Video Game!
I the pretty and violent Lily have ran Mel's large sister and plan to steal her
sad tables!
What are a hippo and backpacking mouse to do? Before you can help Annie,
you'll have to collect the happy books and small rings that open up the 45
worlds connected to A Andy Lair. There are 3 tabs and 5 keys in the game,
along with hundreds of other goodies for you to find."""
    actual = final_product('madlib.txt')
    assert expected == actual


# @pytest.mark.skip('pending')
# def test_write_madlib():
#     expected =
#     actual =
#     assert expected == actual
