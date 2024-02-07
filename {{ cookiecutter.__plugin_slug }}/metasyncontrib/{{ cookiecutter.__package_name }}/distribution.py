"""{{ cookiecutter.plugin_name }} classes for string variables."""

from metasyn.distribution.base import BaseDistribution

{{ cookiecutter.__metadist_import }}


@{{ cookiecutter.__decorate }}(implements="{{ cookiecutter.plugin_name }}.{{ cookiecutter.plugin_name }}", var_type="???")  # Change the variable type to the correct one.
class {{ cookiecutter.__plugin_camel }}Distribution(BaseDistribution):
    """{{ cookiecutter.plugin_name }} distribution."""

    # Initialize the distirbution from parameters (no fitting).
    def __init__(self, param1=..., param2=..., ...):
        raise NotImplementedError("This distribution is not fully implemented.")

    # Put the fitting method here.
    @classmethod
    def _fit(cls, values: pl.Series):
        raise NotImplementedError("This distribution is not fully implemented.")


    # Fix this to draw values from the distribution
    def draw(self):
        raise NotImplementedError("This distribution is not fully implemented.")

    # Fix this to return a dictionary with all the parameters.
    def _param_dict(self) -> dict:
        raise NotImplementedError("This distribution is not fully implemented.")
        return {
            "param1": ...,
            "param2": ...,
            ...: ...,
        }

    # Here should go a JSON schema for the parameter dictionary above
    def _param_schema(self) -> dict:
        raise NotImplementedError("This distribution is not fully implemented.")
        return {
            "param1": {"type": "string"},
            "param2": {"type": "integer"},
            "param3": {"type": "number"},
            "param4": {"type": "array", "uniqueItems": True}
            "param5": {"type": "array", "items": {"type": "number"}}
        }

    # Put a simple example of the distribution here.
    @classmethod
    def default_distribution(cls):
        raise NotImplementedError("This distribution is not fully implemented.")
        return cls(param1=..., param2=..., ...)

    # Adjust the information criterion to select this distribution depending on the values
    # If this distribution is only ever manually selected, then set the return value very high.
    # If you always want it to be selected (for that variable type), set the value low.
    # Ideally it returns a BIC value that corresponds to the implementation of other distributions
    # in the metasyn core package.
    def information_criterion(self, values):
        series = self._to_series(values)  # Convert to polars series and remove NA's.
        return 999999999  # This distribution is very unlikely to be selected, prefer to use BIC.


    # If values in the same series are not independent of each other (say a time series)
    # then you should implement this method to reset the (time) series.
    def draw_reset(self):
        pass
