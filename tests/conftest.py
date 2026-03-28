import pytest

@pytest.fixture
def example_fixture():
    """
    An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
    """

    # place any setup you want to do before any test function that uses this fixture is run

    yield  # at the yield point, the test function will run and do its business

    # place with any teardown you want to do after any test function that uses this fixture has compl