Build and Package {{cookiecutter.project_name}}
==============================

This document summarizes how to build and package {{cookiecutter.project_name}} on Windows.

{{cookiecutter.project_name}} is a custom Slicer application. Reading the [3D Slicer Developer Documentation](https://slicer.readthedocs.io/en/latest/developer_guide/index.html) may help answer additional questions.

The initial source files were created using [KitwareMedical/SlicerCustomAppTemplate](https://github.com/KitwareMedical/SlicerCustomAppTemplate).

Prerequisites
-------------

* Setting up your git account:

    * Create a [Github](https://github.com) account.

    * Setup your SSH keys following [these](https://help.github.com/articles/generating-ssh-keys) instructions at the
    exception of `step 2` where you should __NOT__ enter a passphrase.

    * Setup [your git username](https://help.github.com/articles/setting-your-username-in-git) and [your git email](https://help.github.com/articles/setting-your-email-in-git).

    * If not already done, email `FirstName LastName <firstname.lastname@{{cookiecutter.github_organization}}.com>` to be granted access to
    the [{{cookiecutter.github_organization}}/{{cookiecutter.github_project}}](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.github_project}}) repository.

Checkout
--------

1. Start `Git Bash`
2. Checkout the source code into a directory `C:\W\` by typing the following commands:

```bat
cd /c
mkdir W
cd /c/W
git clone https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.github_project}}.git {{cookiecutter.github_project|first}}
```

Note: use short source and build directory names to avoid the [maximum path length limitation](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file#maximum-path-length-limitation).

Build
-----
Note: The build process will take approximately 3 hours.

<b>Option 1: CMake GUI and Visual Studio (Recommended)</b>

1. Start [CMake GUI](https://cmake.org/runningcmake/), select source directory `C:\W\{{cookiecutter.github_project|first}}` and set build directory to `C:\W\{{cookiecutter.github_project|first}}R`.
2. Add an entry `Qt5_DIR` pointing to `C:/Qt/${QT_VERSION}/${COMPILER}/lib/cmake/Qt5`.
2. Generate the project.
3. Open `C:\W\{{cookiecutter.github_project|first}}R\{{cookiecutter.project_name}}.sln`, select `Release` and build the project.

<b>Option 2: Command Line</b>

1. Start the [Command Line Prompt](http://windows.microsoft.com/en-us/windows/command-prompt-faq)
2. Configure and build the project in `C:\W\{{cookiecutter.github_project|first}}R` by typing the following commands:

```bat
cd C:\W\
mkdir {{cookiecutter.github_project|first}}R
cd {{cookiecutter.github_project|first}}R
cmake -G "Visual Studio 17 2022" -A x64 -DQt5_DIR:PATH=`C:/Qt/${QT_VERSION}/${COMPILER}/lib/cmake/Qt5 ..\{{cookiecutter.github_project|first}}
cmake --build . --config Release -- /maxcpucount:4
```

Package
-------

Install [NSIS 2](http://sourceforge.net/projects/nsis/files/)

<b>Option 1: CMake and Visual Studio</b>

1. In the `C:\W\{{cookiecutter.github_project|first}}R\Slicer-build` directory, open `Slicer.sln` and build the `PACKAGE` target

<b>Option 2: Command Line</b>

1. Start the [Command Line Prompt](http://windows.microsoft.com/en-us/windows/command-prompt-faq)
2. Build the `PACKAGE` target by typing the following commands:

```bat
cd C:\W\{{cookiecutter.github_project|first}}R\Slicer-build
cmake --build . --config Release --target PACKAGE
```

