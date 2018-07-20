/*==============================================================================

  Copyright (c) Kitware, Inc.

  See http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Julien Finet, Kitware, Inc.
  and was partially funded by NIH grant 3P41RR013218-12S1

==============================================================================*/

// Qt includes
#include <QDebug>
#include <QDesktopWidget>

// Slicer includes
#include "qSlicerModuleSelectorToolBar.h"

// SlicerApp includes
#include "q{{cookiecutter.app_name}}AppAboutDialog.h"
#include "q{{cookiecutter.app_name}}AppMainWindow_p.h"
#include "qSlicerApplication.h"

//-----------------------------------------------------------------------------
// q{{cookiecutter.app_name}}AppMainWindowPrivate methods

q{{cookiecutter.app_name}}AppMainWindowPrivate::q{{cookiecutter.app_name}}AppMainWindowPrivate(q{{cookiecutter.app_name}}AppMainWindow& object)
  : Superclass(object)
{
}

//-----------------------------------------------------------------------------
q{{cookiecutter.app_name}}AppMainWindowPrivate::~q{{cookiecutter.app_name}}AppMainWindowPrivate()
{
}

//-----------------------------------------------------------------------------
void q{{cookiecutter.app_name}}AppMainWindowPrivate::init()
{
  Q_Q(q{{cookiecutter.app_name}}AppMainWindow);
  this->Superclass::init();
}

//-----------------------------------------------------------------------------
void q{{cookiecutter.app_name}}AppMainWindowPrivate::setupUi(QMainWindow * mainWindow)
{
  this->Superclass::setupUi(mainWindow);

  qSlicerApplication * app = qSlicerApplication::application();

  mainWindow->setWindowTitle(app->applicationName());
  this->HelpAboutSlicerAppAction->setText("About " + app->applicationName());
  this->HelpAboutSlicerAppAction->setToolTip("");

  QPixmap logo(":/LogoFull.png");
#if (QT_VERSION >= QT_VERSION_CHECK(5, 0, 0))
  qreal dpr = sqrt(q{{cookiecutter.app_name}}App->desktop()->logicalDpiX()*qreal(q{{cookiecutter.app_name}}App->desktop()->logicalDpiY()) / (q{{cookiecutter.app_name}}App->desktop()->physicalDpiX()*q{{cookiecutter.app_name}}App->desktop()->physicalDpiY()));
  logo.setDevicePixelRatio(dpr);
#endif
  this->LogoLabel->setPixmap(logo);

  // Hide the toolbars
  this->MainToolBar->setVisible(false);
  //this->ModuleSelectorToolBar->setVisible(false);
  this->ModuleToolBar->setVisible(false);
  this->ViewToolBar->setVisible(false);
  this->MouseModeToolBar->setVisible(false);
  this->CaptureToolBar->setVisible(false);
  this->ViewersToolBar->setVisible(false);
  this->DialogToolBar->setVisible(false);

  // Hide the menus
  //this->menubar->setVisible(false);
  //this->FileMenu->setVisible(false);
  //this->EditMenu->setVisible(false);
  //this->ViewMenu->setVisible(false);
  //this->LayoutMenu->setVisible(false);
  //this->HelpMenu->setVisible(false);

  // Hide the modules panel
  //this->PanelDockWidget->setVisible(false);
  this->DataProbeCollapsibleWidget->setCollapsed(true);
  this->DataProbeCollapsibleWidget->setVisible(false);
  this->StatusBar->setVisible(false);
}

//-----------------------------------------------------------------------------
// q{{cookiecutter.app_name}}AppMainWindow methods

//-----------------------------------------------------------------------------
q{{cookiecutter.app_name}}AppMainWindow::q{{cookiecutter.app_name}}AppMainWindow(QWidget* windowParent)
  : Superclass(new q{{cookiecutter.app_name}}AppMainWindowPrivate(*this), windowParent)
{
  Q_D(q{{cookiecutter.app_name}}AppMainWindow);
  d->init();
}

//-----------------------------------------------------------------------------
q{{cookiecutter.app_name}}AppMainWindow::~q{{cookiecutter.app_name}}AppMainWindow()
{
}

//-----------------------------------------------------------------------------
void q{{cookiecutter.app_name}}AppMainWindow::on_HelpAboutSlicerAppAction_triggered()
{
  q{{cookiecutter.app_name}}AppAboutDialog about(this);
  about.exec();
}
