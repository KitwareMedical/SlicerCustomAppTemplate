import qt

import slicer
from slicer.ScriptedLoadableModule import (
    ScriptedLoadableModule,
    ScriptedLoadableModuleLogic,
    ScriptedLoadableModuleWidget,
)
from slicer.util import VTKObservationMixin

import SlicerCustomAppUtilities

# Import to ensure the files are available through the Qt resource system
from Resources import HomeResources


class Home(ScriptedLoadableModule):
    """The home module allows to orchestrate and style the overall application workflow.

    It is a "special" module in the sense that its role is to customize the application and
    coordinate a workflow between other "regular" modules.

    Associated widget and logic are not intended to be initialized multiple times.
    """

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Home"
        self.parent.categories = [""]
        self.parent.dependencies = []
        self.parent.contributors = ["Sam Horvath (Kitware Inc.)", "Jean-Christophe Fillion-Robin (Kitware Inc.)"]
        self.parent.helpText = """This module orchestrates and styles the overall application workflow."""
        self.parent.helpText += self.getDefaultModuleDocumentationLink()
        self.parent.acknowledgementText = """..."""  # replace with organization, grant and thanks.


class HomeWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
    """Uses ScriptedLoadableModuleWidget base class, available at:
    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
        """Called when the application opens the module the first time and the widget is initialized."""
        ScriptedLoadableModuleWidget.__init__(self, parent)
        VTKObservationMixin.__init__(self)

    def setup(self):
        """Called when the application opens the module the first time and the widget is initialized."""
        ScriptedLoadableModuleWidget.setup(self)

        # Load widget from .ui file (created by Qt Designer)
        self.uiWidget = slicer.util.loadUI(self.resourcePath("UI/Home.ui"))
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

    def cleanup(self):
        """Called when the application closes and the module widget is destroyed."""
        pass

    def setSlicerUIVisible(self, visible):
        slicer.util.setDataProbeVisible(visible)
        slicer.util.setMenuBarsVisible(visible, ignore=["MainToolBar", "ViewToolBar"])
        slicer.util.setModuleHelpSectionVisible(visible)
        slicer.util.setModulePanelTitleVisible(visible)
        slicer.util.setPythonConsoleVisible(visible)
        slicer.util.setApplicationLogoVisible(visible)
        keepToolbars = [
            slicer.util.findChild(slicer.util.mainWindow(), "MainToolBar"),
            slicer.util.findChild(slicer.util.mainWindow(), "ViewToolBar"),
            slicer.util.findChild(slicer.util.mainWindow(), "CustomToolBar"),
        ]
        slicer.util.setToolbarsVisible(visible, keepToolbars)

    def modifyWindowUI(self):

        # Custom toolbar
        mainToolBar = slicer.util.findChild(slicer.util.mainWindow(), "MainToolBar")
        self.CustomToolBar = qt.QToolBar("CustomToolBar")
        self.CustomToolBar.name = "CustomToolBar"
        slicer.util.mainWindow().insertToolBar(mainToolBar, self.CustomToolBar)

        # Settings dialog
        gearIcon = qt.QIcon(self.resourcePath("Icons/Gears.png"))
        self.settingsAction = self.CustomToolBar.addAction(gearIcon, "")
        self.settingsDialog = slicer.util.loadUI(self.resourcePath("UI/Settings.ui"))
        self.settingsUI = slicer.util.childWidgetVariables(self.settingsDialog)
        self.settingsUI.CustomUICheckBox.toggled.connect(self.setCustomUIVisible)
        self.settingsUI.CustomStyleCheckBox.toggled.connect(self.toggleStyle)
        self.settingsAction.triggered.connect(self.raiseSettings)

    def toggleStyle(self, visible):
        if visible:
            self.applyApplicationStyle()
        else:
            slicer.app.styleSheet = ""

    def raiseSettings(self, unused):
        self.settingsDialog.exec()

    def setCustomUIVisible(self, visible):
        self.setSlicerUIVisible(not visible)

    def applyApplicationStyle(self):
        SlicerCustomAppUtilities.applyStyle([slicer.app], self.resourcePath("Home.qss"))


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

    def setup3DView(self):
        layoutManager = slicer.app.layoutManager()
        # layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)
        # controller = slicer.app.layoutManager().threeDWidget(0).threeDController()
        # controller.setBlackBackground()
        # controller.set3DAxisVisible(False)
        # controller.set3DAxisLabelVisible(False)
        # controller.setOrientationMarkerType(3)  # Axis marker
        # controller.setStyleSheet("background-color: #000000")

    def setupSliceViewers(self):
        for name in slicer.app.layoutManager().sliceViewNames():
            sliceWidget = slicer.app.layoutManager().sliceWidget(name)
            self.setupSliceViewer(sliceWidget)

    def setupSliceViewer(self, sliceWidget):
        controller = sliceWidget.sliceController()
        # controller.setStyleSheet("background-color: #000000")
        # controller.sliceViewLabel = ""
        # slicer.util.findChild(sliceWidget, "PinButton").visible = False
        # slicer.util.findChild(sliceWidget, "ViewLabel").visible = False
        # slicer.util.findChild(sliceWidget, "FitToWindowToolButton").visible = False
        # slicer.util.findChild(sliceWidget, "SliceOffsetSlider").spinBoxVisible = False
