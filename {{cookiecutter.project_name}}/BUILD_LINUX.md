# Build and Package {{cookiecutter.project_name}}

This document summarizes how to build and package {{cookiecutter.project_name}} on Linux.

{{cookiecutter.project_name}} is a custom Slicer application. Reading the [3D Slicer Developer Documentation](https://slicer.readthedocs.io/en/latest/developer_guide/index.html) may help answer additional questions.

The initial source files were created using [KitwareMedical/SlicerCustomAppTemplate](https://github.com/KitwareMedical/SlicerCustomAppTemplate).

## Clone

```sh
git clone https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.github_project}}.git
```

## Prerequisites

Install the prerequisites as described in the [Slicer documentation for building on Linux](https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html). This includes development tools, support libraries, and Qt.

## Build

Note: The build process can take hours.

Assuming that Qt 5.15.2 was installed to `/opt/qt/` (if not then adjust the command accordingly):

```sh
cmake \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DQt5_DIR:PATH=/opt/qt/5.15.2/gcc_64/lib/cmake/Qt5 \
  -S {{cookiecutter.github_project}} \
  -B {{cookiecutter.github_project}}-SuperBuild-Release

make -j<N>
```

where `<N>` is the number of parallel builds. As a rule of thumb, many use the `number of CPU threads - 1` as the number of parallel builds.

Once the application is built, there will be an _inner build_ inside the _superbuild_ folder, located at `{{cookiecutter.app_name}}-SuperBuild-Release/Slicer-build`. The application executable is contained in this _inner build_ folder.

## Package

From the _inner build_ folder:

```sh
make package
```
