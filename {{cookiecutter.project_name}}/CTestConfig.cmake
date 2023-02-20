set(CTEST_PROJECT_NAME "{{ cookiecutter.project_name }}")
set(CTEST_NIGHTLY_START_TIME "3:00:00 UTC")

set(CTEST_DROP_METHOD "https")
set(CTEST_DROP_SITE "{{ cookiecutter.cdash_drop_site }}")
set(CTEST_DROP_LOCATION "/submit.php?project=${CTEST_PROJECT_NAME}")
set(CTEST_DROP_SITE_CDASH TRUE)
