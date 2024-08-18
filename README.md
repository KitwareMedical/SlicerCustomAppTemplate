# SlicerCustomAppTemplate by Kitware

This project is a template to be used as a starting point for creating a custom 3D Slicer application.

[3D Slicer](https://slicer.org) is an open-source and extensible application for visualization and medical image
analysis. 3D Slicer works with optical imaging, MRI, CT, and ultrasound data.

At [Kitware](https://www.kitware.com), we help customers develop commercial products based on 3D Slicer and we have used the platform to rapidly prototype solutions in nearly every aspect of medical imaging.

## Getting Started

The following will get a custom 3D Slicer application started in a new repository:

```bash
pip install cookiecutter jinja2-github
cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate
# Fill in the information requested at the prompts
```

We suggest to use the following commit message for checking in the results of these commands:

```
ENH: Add <custom name> application sources

This commit adds source files generated using KitwareMedical/SlicerCustomAppTemplate@<SHA of main>
and referencing Slicer/Slicer@<SHA of main>.

Features and improvements specific to the custom application will be integrated
in follow-up commits.
```

This will mark the version of the template file used and the Slicer version in the git history

## FAQ

### Which version of Slicer do the generated application build against ?

Leveraging the ``jinja2-github`` plugin, the ``cookiecutter`` template generator will retrieve the latest commit associated with the Slicer repository default branch and it will set it as ``GIT_TAG`` value in the generated ``CMakeLists.txt``.



## License

This project template is distributed under the Apache 2.0 license. Please see
the *LICENSE* file for details.

## Authors

* Julien Finet
* Jean-Christophe Fillion-Robin
* Dženan Zukić
* Johan Andruejol
* Alexis Girault
* Cory Quammen
* Jamie Snape
