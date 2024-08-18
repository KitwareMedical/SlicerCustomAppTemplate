import os
import shutil
import stat
import sys
from collections.abc import Callable
from pathlib import Path

import nox

nox.needs_version = ">=2024.3.2"
nox.options.sessions = ["pre-commit", "pre-commit-cookie"]
nox.options.default_venv_backend = "uv|virtualenv"


DIR = Path(__file__).parent.resolve()

JOB_FILE = """\
default_context:
  project_name: {project_name}
"""


def _remove_readonly(func: Callable[[str], None], path: str, _: object) -> None:
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rmtree_ro(path: Path) -> None:
    if sys.version_info >= (3, 12):
        shutil.rmtree(path, onexc=_remove_readonly)
    else:
        shutil.rmtree(path, onerror=_remove_readonly)


def make_cookie(session: nox.Session) -> None:
    project_name = "Awesome"
    package_dir = Path(project_name)
    if package_dir.exists():
        rmtree_ro(package_dir)

    Path("input.yml").write_text(
        JOB_FILE.format(project_name=project_name), encoding="utf-8"
    )

    session.run(
        "cookiecutter",
        "--no-input",
        f"{DIR}",
        "--config-file=input.yml",
    )

    init_git(session, package_dir)

    return package_dir


def init_git(session: nox.Session, package_dir: Path) -> None:
    session.run("git", "-C", f"{package_dir}", "init", "-q", external=True)
    session.run("git", "-C", f"{package_dir}", "add", ".", external=True)
    session.run(
        "git",
        "-C",
        f"{package_dir}",
        "-c",
        "user.name=Kitware Bot",
        "-c",
        "user.email=kwrobot@kitware.com",
        "commit",
        "-qm",
        "feat: initial version",
        external=True,
    )


@nox.session(name="pre-commit-cookie")
def pre_commit_cookie(session: nox.Session) -> None:
    session.install("cookiecutter", "jinja2-github", "pre-commit")

    tmp_dir = session.create_tmp()
    session.cd(tmp_dir)
    cookie = make_cookie(session)
    session.chdir(cookie)

    session.run(
        "pre-commit",
        "run",
        "--all-files",
        "--hook-stage=manual",
        "--show-diff-on-failure",
    )


@nox.session(name="pre-commit")
def pre_commit(session: nox.Session) -> str:
    """
    Run linters on the codebase.
    """
    session.install("pre-commit")
    session.run("pre-commit", "run", "-a")
