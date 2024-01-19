"""Base class for all {{ cookiecutter.plugin_name|lower }} distributions."""


def metadist_{{ cookiecutter.__package_name }}():
    """Decorate class to create a distribution with disclosure control.

    Returns
    -------
    cls:
        Class with the appropriate class variables.
    """
    def _wrap(cls):
        cls.provenance = "{{ cookiecutter.__plugin_slug }}"
        cls.privacy = "{{ cookiecutter.privacy }}"
        return cls
    return _wrap
