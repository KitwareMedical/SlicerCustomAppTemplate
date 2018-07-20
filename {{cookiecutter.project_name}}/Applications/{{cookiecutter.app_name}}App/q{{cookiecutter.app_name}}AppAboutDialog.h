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

#ifndef __q{{cookiecutter.app_name}}AppAboutDialog_h
#define __q{{cookiecutter.app_name}}AppAboutDialog_h

// Qt includes
#include <QDialog>

// CTK includes
#include <ctkPimpl.h>

// SlicerApp includes
#include "qSlicerAppExport.h"

class q{{cookiecutter.app_name}}AppAboutDialogPrivate;

/// Pre-request that a q{{cookiecutter.app_name}}Application has been instanced
class Q_SLICER_APP_EXPORT q{{cookiecutter.app_name}}AppAboutDialog
  : public QDialog
{
  Q_OBJECT
public:
  q{{cookiecutter.app_name}}AppAboutDialog(QWidget *parentWidget = 0);
  virtual ~q{{cookiecutter.app_name}}AppAboutDialog();

protected:
  QScopedPointer<q{{cookiecutter.app_name}}AppAboutDialogPrivate> d_ptr;

private:
  Q_DECLARE_PRIVATE(q{{cookiecutter.app_name}}AppAboutDialog);
  Q_DISABLE_COPY(q{{cookiecutter.app_name}}AppAboutDialog);
};

#endif
