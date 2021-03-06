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

#ifndef __q{{cookiecutter.app_name}}AppMainWindow_p_h
#define __q{{cookiecutter.app_name}}AppMainWindow_p_h

// {{cookiecutter.app_name}} includes
#include "q{{cookiecutter.app_name}}AppMainWindow.h"

// Slicer includes
#include "qSlicerMainWindow_p.h"

//-----------------------------------------------------------------------------
class Q_{{cookiecutter.app_name|upper}}_APP_EXPORT q{{cookiecutter.app_name}}AppMainWindowPrivate
  : public qSlicerMainWindowPrivate
{
  Q_DECLARE_PUBLIC(q{{cookiecutter.app_name}}AppMainWindow);
public:
  typedef qSlicerMainWindowPrivate Superclass;
  q{{cookiecutter.app_name}}AppMainWindowPrivate(q{{cookiecutter.app_name}}AppMainWindow& object);
  virtual ~q{{cookiecutter.app_name}}AppMainWindowPrivate();

  virtual void init();
  /// Reimplemented for custom behavior
  virtual void setupUi(QMainWindow * mainWindow);
};

#endif
