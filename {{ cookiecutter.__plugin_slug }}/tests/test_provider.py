from pytest import mark

from metasyn.provider import get_distribution_provider
from metasyn.testutils import check_distribution, check_distribution_provider


def test_{{ cookiecutter.__package_name }}_provider():
    check_distribution_provider("{{ cookiecutter.__package_name }}")


@mark.parametrize(
    "distribution", get_distribution_provider("{{ cookiecutter.__package_name }}").distributions
)
@mark.parametrize(
    "privacy_kwargs", ({},) # {"epsilon": 0.1 }, ...) 
)
def test_dist_validation(distribution, privacy_kwargs):
    check_distribution(distribution, privacy="{{ cookiecutter.privacy }}",
                       provenance="{{ cookiecutter.__package_name }}",
                       **privacy_kwargs)
