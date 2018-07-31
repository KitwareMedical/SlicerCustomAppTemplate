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

#ifndef __q{{cookiecutter.app_name}}AppMainWindow_h
#define __q{{cookiecutter.app_name}}AppMainWindow_h

// Slicer includes
#include "qSlicerAppExport.h"
#include "qSlicerAppMainWindow.h"
class q{{cookiecutter.app_name}}AppMainWindowPrivate;

class Q_SLICER_APP_EXPORT q{{cookiecutter.app_name}}AppMainWindow
  : public qSlicerAppMainWindow
{
  Q_OBJECT
public:

  typedef qSlicerAppMainWindow Superclass;
  q{{cookiecutter.app_name}}AppMainWindow(QWidget *parent=0);
  virtual ~q{{cookiecutter.app_name}}AppMainWindow();

public:
  /// Reimplemented to use q{{cookiecutter.app_name}}AppAboutDialog instead of qSlicerAppAboutDialog.
  virtual void on_HelpAboutSlicerAppAction_triggered();

private:
  Q_DECLARE_PRIVATE(q{{cookiecutter.app_name}}AppMainWindow);
  Q_DISABLE_COPY(q{{cookiecutter.app_name}}AppMainWindow);
};

#endif
