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

// {{cookiecutter.app_name}} includes
#include "q{{cookiecutter.app_name}}AppExport.h"
class q{{cookiecutter.app_name}}AppMainWindowPrivate;

// Slicer includes
#include "qSlicerMainWindow.h"

class Q_{{cookiecutter.app_name|upper}}_APP_EXPORT q{{cookiecutter.app_name}}AppMainWindow : public qSlicerMainWindow
{
  Q_OBJECT
public:
  typedef qSlicerMainWindow Superclass;

  q{{cookiecutter.app_name}}AppMainWindow(QWidget *parent=0);
  virtual ~q{{cookiecutter.app_name}}AppMainWindow();

public slots:
  void on_HelpAbout{{cookiecutter.app_name}}AppAction_triggered();

protected:
  q{{cookiecutter.app_name}}AppMainWindow(q{{cookiecutter.app_name}}AppMainWindowPrivate* pimpl, QWidget* parent);

private:
  Q_DECLARE_PRIVATE(q{{cookiecutter.app_name}}AppMainWindow);
  Q_DISABLE_COPY(q{{cookiecutter.app_name}}AppMainWindow);
};

#endif
