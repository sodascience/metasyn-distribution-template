# Metasyn distribution plugin template 

Template for creating distrubion plugins for the metasyn library. If you want to define new distributions
for the [metasyn](https://github.com/sodascience/metasyn) and provide them as a plugin, then this is the
template for you. If instead you want to create a privacy plugin using existing distributions, then use the [metasyn-privacy](https://github.com/sodascience/metasyn-plugin-template) template.

Follow these steps to create a new plugin from this template:

- Install cookiecutter: `pip install cookiecutter` on the command line.
- Use the template: `cookiecutter https://github.com/sodascience/metasyn-distribution-template`

The template is now ready to use. To finish your plugin, edit the following modules:

- `metasyncontrib.{plugin_name}.base`: Change the `privacy` class variable if necessary.
- `metasyncontrib.{plugin_name}.distribution`: Implement distributions here.
- `metasyncontrib.{plugin_name}.provider`: Add the newly implemented distributions.

Your plugin should now be ready to go. GitHub actions is part of the template, so after pushing your new plugin to GitHub it should automatically start testing your code.

<!-- CONTRIBUTING -->
## Contributing
You can contribute to this template by giving feedback in the "Issues" tab, or by creating a pull request.

To create a pull request:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact
**Metasyn** is a project by the [ODISSEI Social Data Science (SoDa)](https://odissei-data.nl/nl/soda/) team.
Do you have questions, suggestions, or remarks on the technical implementation? File an issue in the issue tracker or feel free to contact [Raoul Schram](https://github.com/qubixes).

<img src="soda.png" alt="SoDa logo" width="250px"/> 
