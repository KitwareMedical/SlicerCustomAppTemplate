from typing import Optional

import qt
import slicer
import SlicerCustomAppUtilities
from slicer.ScriptedLoadableModule import (
    ScriptedLoadableModule,
    ScriptedLoadableModuleLogic,
    ScriptedLoadableModuleWidget,
)
from slicer.util import VTKObservationMixin

# Import to ensure the files are available through the Qt resource system
from Resources import HomeResources  # noqa: F401


class Home(ScriptedLoadableModule):
    """The home module allows to orchestrate and style the overall application workflow.

    It is a "special" module in the sense that its role is to customize the application and
    coordinate a workflow between other "regular" modules.

    Associated widget and logic are not intended to be initialized multiple times.
    """

    def __init__(self, parent: Optional[qt.QWidget]):
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

    def __init__(self, parent: Optional[qt.QWidget]):
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

        # Get references to relevant underlying modules
        # NA

        # Create logic class
        self.logic = HomeLogic()

        # Dark palette does not propagate on its own?
        self.uiWidget.setPalette(slicer.util.mainWindow().style().standardPalette())

        # Remove unneeded UI elements
        self.modifyWindowUI()
        self.setCustomUIVisible(True)

        # Apply style
        self.applyApplicationStyle()

    def cleanup(self):
        """Called when the application closes and the module widget is destroyed."""
        pass

    def setSlicerUIVisible(self, visible: bool):
        exemptToolbars = [
            "MainToolBar",
            "ViewToolBar",
            "CustomToolBar",
        ]
        slicer.util.setDataProbeVisible(visible)
        slicer.util.setMenuBarsVisible(visible, ignore=exemptToolbars)
        slicer.util.setModuleHelpSectionVisible(visible)
        slicer.util.setModulePanelTitleVisible(visible)
        slicer.util.setPythonConsoleVisible(visible)
        slicer.util.setApplicationLogoVisible(visible)
        keepToolbars = [slicer.util.findChild(slicer.util.mainWindow(), toolbarName) for toolbarName in exemptToolbars]
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

    def toggleStyle(self, visible: bool):
        if visible:
            self.applyApplicationStyle()
        else:
            slicer.app.styleSheet = ""

    def raiseSettings(self, _):
        self.settingsDialog.exec()

    def setCustomUIVisible(self, visible: bool):
        self.setSlicerUIVisible(not visible)

    def applyApplicationStyle(self):
        SlicerCustomAppUtilities.applyStyle([slicer.app], self.resourcePath("Home.qss"))
        self.styleThreeDWidget()
        self.styleSliceWidgets()

    def styleThreeDWidget(self):
        viewNode = slicer.app.layoutManager().threeDWidget(0).mrmlViewNode()  # noqa: F841
        # viewNode.SetBackgroundColor(0.0, 0.0, 0.0)
        # viewNode.SetBackgroundColor2(0.0, 0.0, 0.0)
        # viewNode.SetBoxVisible(False)
        # viewNode.SetAxisLabelsVisible(False)
        # viewNode.SetOrientationMarkerType(slicer.vtkMRMLViewNode.OrientationMarkerTypeAxes)

    def styleSliceWidgets(self):
        for name in slicer.app.layoutManager().sliceViewNames():
            sliceWidget = slicer.app.layoutManager().sliceWidget(name)
            self.styleSliceWidget(sliceWidget)

    def styleSliceWidget(self, sliceWidget: slicer.qMRMLSliceWidget):
        controller = sliceWidget.sliceController()  # noqa: F841
        # controller.sliceViewLabel = ""
        # slicer.util.findChild(sliceWidget, "PinButton").visible = False
        # slicer.util.findChild(sliceWidget, "ViewLabel").visible = False
        # slicer.util.findChild(sliceWidget, "FitToWindowToolButton").visible = False
        # slicer.util.findChild(sliceWidget, "SliceOffsetSlider").spinBoxVisible = False


class HomeLogic(ScriptedLoadableModuleLogic):
    """
    Implements underlying logic for the Home module.
    """

    pass
