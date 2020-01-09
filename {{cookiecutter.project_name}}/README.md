{{cookiecutter.project_name}} by {{cookiecutter.org_name}}
================================

{{cookiecutter.app_description_summary}}

![{{cookiecutter.project_name}} by {{cookiecutter.org_name}}](Applications/App/Resources/Images/LogoFull.png?raw=true)

Prerequisites
-------------

* Microsoft Windows 7 or above recommended

* Supported Microsoft Visual Studio versions:
    * Visual Studio 2015

* [CMake](http://cmake.org/cmake/resources/software.html), version 3.11 or above

* Qt, version 5.10 or above

* [Git](http://git-scm.com/downloads)

* [Subversion](http://www.sliksvn.com/en/download)

* Setting up your git account:

    * Create a [Github](https://github.com) account.

    * Setup your SSH keys following [these](https://help.github.com/articles/generating-ssh-keys) instructions at the
    exception of `step 2` where you should __NOT__ enter a passphrase.

    * Setup [your git username](https://help.github.com/articles/setting-your-username-in-git) and [your git email](https://help.github.com/articles/setting-your-email-in-git).

    * If not already done, email `FirstName LastName <firstname.lastname@{{cookiecutter.github_organization}}.com>` to be granted access to
    the [{{cookiecutter.github_organization}}/{{cookiecutter.github_project}}](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.github_project}}) repository.

Checkout
--------

1. Start [Git Bash](https://help.github.com/articles/set-up-git#need-a-quick-lesson-about-terminalterminalgit-bashthe-command-line)
2. Checkout the source code into a directory `C:\W\` by typing the following commands:

```bat
cd /c
mkdir W
cd /c/W
git clone https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.github_project}}.git {{cookiecutter.github_project}}
```

Note: use short source and build directory names to avoid the [maximum path length limitation](http://msdn.microsoft.com/en-us/library/windows/desktop/aa365247%28v=vs.85%29.aspx#maxpath).

Build
-----
Note: The build process will take approximately 3 hours.

<b>Option 1: CMake GUI and Visual Studio (Recommended)</b>

1. Start [CMake GUI](https://cmake.org/runningcmake/), select source directory `C:\W\{{cookiecutter.github_project}}` and set build directory to `C:\W\{{cookiecutter.github_project}}-rel`.
2. Add an entry `QT_QMAKE_EXECUTABLE` pointing to `C:\D\Support\qt-4.8.7-64-vs2013-rel`.
2. Generate the project.
3. Open `C:\W\{{cookiecutter.github_project}}-rel\{{cookiecutter.project_name}}.sln`, select `Release` and build the project.

<b>Option 2: Command Line</b>

1. Start the [Command Line Prompt](http://windows.microsoft.com/en-us/windows/command-prompt-faq)
2. Configure and build the project in `C:\W\{{cookiecutter.github_project}}-rel` by typing the following commands:

```bat
cd C:\W\
mkdir {{cookiecutter.github_project}}-rel
cd {{cookiecutter.github_project}}-rel
cmake -G "Visual Studio 14 2015 Win64" -DQT_QMAKE_EXECUTABLE:PATH=C:\Qt\5.9.1\msvc2015_64\bin\qmake.exe ..\{{cookiecutter.github_project}}
cmake --build . --config Release
```

Package
-------

Install [NSIS 2](http://sourceforge.net/projects/nsis/files/)

<b>Option 1: CMake and Visual Studio (Recommended)</b>

1. In the `C:\W\{{cookiecutter.github_project}}-rel\Slicer-build` directory, open `Slicer.sln` and build the `PACKAGE` target

<b>Option 2: Command Line</b>

1. Start the [Command Line Prompt](http://windows.microsoft.com/en-us/windows/command-prompt-faq)
2. Build the `PACKAGE` target by typing the following commands:

```bat
cd C:\W\{{cookiecutter.github_project}}-rel\Slicer-build
cmake --build . --config Release --target PACKAGE
```

Resources
---------
* [3D Slicer Developer Wiki](http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Developers)
