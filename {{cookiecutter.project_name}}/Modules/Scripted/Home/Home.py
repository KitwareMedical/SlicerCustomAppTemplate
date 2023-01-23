import logging

import qt

import slicer
from slicer.ScriptedLoadableModule import (
  ScriptedLoadableModule,
  ScriptedLoadableModuleLogic,
  ScriptedLoadableModuleWidget,
)
from slicer.util import VTKObservationMixin


class Home(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Home"  # TODO make this more human readable by adding spaces
    self.parent.categories = [""]
    self.parent.dependencies = []
    self.parent.contributors = ["Sam Horvath (Kitware Inc.)"]
    self.parent.helpText = """This is the Home module for the custom application"""
    self.parent.helpText += self.getDefaultModuleDocumentationLink()
    self.parent.acknowledgementText = """..."""  # replace with organization, grant and thanks.


class HomeWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModuleWidget.__init__(self, parent)
    VTKObservationMixin.__init__(self)

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    # Load widget from .ui file (created by Qt Designer)
    self.uiWidget = slicer.util.loadUI(self.resourcePath('UI/Home.ui'))
    self.layout.addWidget(self.uiWidget)
    self.ui = slicer.util.childWidgetVariables(self.uiWidget)

    # Remove unneeded UI elements
    self.modifyWindowUI()

    # Create logic class
    self.logic = HomeLogic()

    # Setup scene defaults
    self.setupNodes()

    # Dark palette does not propagate on its own?
    self.uiWidget.setPalette(slicer.util.mainWindow().style().standardPalette())

    self.setCustomUIVisible(True)

    # Apply style
    self.applyApplicationStyle()

  def setupNodes(self):
    self.logic.setup3DView()
    self.logic.setupSliceViewers()

  def onClose(self, unusedOne, unusedTwo):
    pass

  def cleanup(self):
    pass

  def setSlicerUIVisible(self, visible):
    slicer.util.setDataProbeVisible(visible)
    slicer.util.setMenuBarsVisible(visible, ignore=['MainToolBar', 'ViewToolBar'])
    slicer.util.setModuleHelpSectionVisible(visible)
    slicer.util.setModulePanelTitleVisible(visible)
    slicer.util.setPythonConsoleVisible(visible)
    slicer.util.setApplicationLogoVisible(visible)
    keepToolbars = [
      slicer.util.findChild(slicer.util.mainWindow(), 'MainToolBar'),
      slicer.util.findChild(slicer.util.mainWindow(), 'ViewToolBar'),
      slicer.util.findChild(slicer.util.mainWindow(), 'CustomToolBar'),
      ]
    slicer.util.setToolbarsVisible(visible, keepToolbars)

  def modifyWindowUI(self):
    slicer.util.setModuleHelpSectionVisible(False)
    mainToolBar = slicer.util.findChild(slicer.util.mainWindow(), 'MainToolBar')

    self.CustomToolBar = qt.QToolBar("CustomToolBar")
    self.CustomToolBar.name = "CustomToolBar"
    slicer.util.mainWindow().insertToolBar(mainToolBar, self.CustomToolBar)

#     central = slicer.util.findChild(slicer.util.mainWindow(), name='CentralWidget')
#     central.setStyleSheet("background-color: #464449")

    gearIcon = qt.QIcon(self.resourcePath('Icons/Gears.png'))
    self.settingsAction = self.CustomToolBar.addAction(gearIcon, "")

    self.settingsDialog = slicer.util.loadUI(self.resourcePath('UI/Settings.ui'))
    self.settingsUI = slicer.util.childWidgetVariables(self.settingsDialog)

    self.settingsUI.CustomUICheckBox.toggled.connect(self.setCustomUIVisible)
    self.settingsUI.CustomStyleCheckBox.toggled.connect(self.toggleStyle)

    self.settingsAction.triggered.connect(self.raiseSettings)

  def toggleStyle(self,visible):
    if visible:
      self.applyApplicationStyle()
    else:
      slicer.app.styleSheet = ''

  def raiseSettings(self, unused):
    self.settingsDialog.exec()

  def setCustomUIVisible(self, visible):
    self.setSlicerUIVisible(not visible)

  def applyApplicationStyle(self):
    self.applyStyle([slicer.app], 'Home.qss')

  def applyStyle(self, widgets, styleSheetName):
    stylesheetfile = self.resourcePath(styleSheetName)
    with open(stylesheetfile,"r") as fh:
      style = fh.read()
      for widget in widgets:
        widget.styleSheet = style


class HomeLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def run(self, inputVolume, outputVolume, imageThreshold, enableScreenshots=0):
    """
    Run the actual algorithm
    """
    pass

  def exitApplication(self,status=slicer.util.EXIT_SUCCESS, message=None):
    """Exit application.
    If ``status`` is ``slicer.util.EXIT_SUCCESS``, ``message`` is logged using ``logging.info(message)``
    otherwise it is logged using ``logging.error(message)``.
    """
    def _exitApplication():
      if message:
        if status == slicer.util.EXIT_SUCCESS:
          logging.info(message)
        else:
          logging.error(message)
      slicer.util.mainWindow().hide()
      slicer.util.exit(slicer.util.EXIT_FAILURE)
    qt.QTimer.singleShot(0, _exitApplication)

  def setup3DView(self):
    layoutManager = slicer.app.layoutManager()
    # layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)
    # controller = slicer.app.layoutManager().threeDWidget(0).threeDController()
    # controller.setBlackBackground()
    # controller.set3DAxisVisible(False)
    # controller.set3DAxisLabelVisible(False)
    # controller.setOrientationMarkerType(3)  #Axis marker
    # controller.setStyleSheet("background-color: #000000")

  def setupSliceViewers(self):
    for name in slicer.app.layoutManager().sliceViewNames():
        sliceWidget = slicer.app.layoutManager().sliceWidget(name)
        self.setupSliceViewer(sliceWidget)

    # Set linked slice views  in all existing slice composite nodes and in the default node
    sliceCompositeNodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')
    defaultSliceCompositeNode = slicer.mrmlScene.GetDefaultNodeByClass('vtkMRMLSliceCompositeNode')
    if not defaultSliceCompositeNode:
      defaultSliceCompositeNode = slicer.mrmlScene.CreateNodeByClass('vtkMRMLSliceCompositeNode')
      defaultSliceCompositeNode.UnRegister(None)  # CreateNodeByClass is factory method, need to unregister the result to prevent memory leaks
      slicer.mrmlScene.AddDefaultNode(defaultSliceCompositeNode)
    sliceCompositeNodes.append(defaultSliceCompositeNode)
    for sliceCompositeNode in sliceCompositeNodes:
      sliceCompositeNode.SetLinkedControl(True)

  def setupSliceViewer(self, sliceWidget):
    controller = sliceWidget.sliceController()
    # controller.setOrientationMarkerType(3)  #Axis marker
    # controller.setRulerType(1)  #Thin ruler
    # controller.setRulerColor(0) #White ruler
    # controller.setStyleSheet("background-color: #000000")
    # controller.sliceViewLabel = ''
