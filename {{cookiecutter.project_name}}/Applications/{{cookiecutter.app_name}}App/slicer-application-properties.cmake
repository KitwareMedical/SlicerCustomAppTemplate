
set(APPLICATION_NAME
  {{cookiecutter.app_name}}
  )

set(VERSION_MAJOR
  {{cookiecutter.app_version_major}}
  )
set(VERSION_MINOR
  {{cookiecutter.app_version_minor}}
  )
set(VERSION_PATCH
  {{cookiecutter.app_version_patch}}
  )

set(DESCRIPTION_SUMMARY
  "{{cookiecutter.app_description_summary}}"
  )
set(DESCRIPTION_FILE
  ${Slicer_SOURCE_DIR}/README.txt
  )

set(LAUNCHER_SPLASHSCREEN_FILE
  "${CMAKE_CURRENT_LIST_DIR}/Resources/Images/SplashScreen.png"
  )
set(APPLE_ICON_FILE
  "${CMAKE_CURRENT_LIST_DIR}/Resources/Icons/XLarge/DesktopIcon.icns"
  )
set(WIN_ICON_FILE
  "${CMAKE_CURRENT_LIST_DIR}/Resources/App.ico"
  )

set(LICENSE_FILE
  "${Slicer_SOURCE_DIR}/License.txt"
  )

