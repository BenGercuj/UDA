# -*- coding: utf-8 -*-

###########################################################################
## Form code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## Plots, histograms, etc. are displayed using Matplotlib and Pandas
##
## Application made by Bence Gercuj
###########################################################################
import os
from pathlib import Path
import sys

import numpy

import wx
import wx.adv
import wx.grid
from numpy import std

from pandas import DataFrame
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

import math

###########################################################################
## Class importFrame
###########################################################################

class importFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Import", pos=wx.DefaultPosition, size=wx.Size(720, 480),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.previewHappened = False
        self.header = []

        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(resource_path("app.ico"), wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        importBoxSizer = wx.BoxSizer(wx.VERTICAL)

        self.importPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.importPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        importPanelFlexGSizer = wx.FlexGridSizer(0, 2, 0, 0)
        importPanelFlexGSizer.SetFlexibleDirection(wx.BOTH)
        importPanelFlexGSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.datasetPathTxt = wx.StaticText(self.importPanel, wx.ID_ANY, u"Dataset path:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.datasetPathTxt.Wrap(-1)

        importPanelFlexGSizer.Add(self.datasetPathTxt, 0, wx.ALL, 5)

        self.datasetPathFilePickerCtrl = wx.FilePickerCtrl(self.importPanel, wx.ID_ANY, wx.EmptyString,
                                                           u"Select a dataset",
                                                           u"Text files (*.txt)|*.txt|All files (*.*)|*.*",
                                                           wx.DefaultPosition, wx.DefaultSize,
                                                           wx.FLP_DEFAULT_STYLE)
        importPanelFlexGSizer.Add(self.datasetPathFilePickerCtrl, 0, wx.ALL, 5)

        self.delimiterTxt = wx.StaticText(self.importPanel, wx.ID_ANY, u"Delimiter:", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.delimiterTxt.Wrap(-1)

        importPanelFlexGSizer.Add(self.delimiterTxt, 0, wx.ALL, 5)

        self.delimiterStr = wx.TextCtrl(self.importPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0)
        importPanelFlexGSizer.Add(self.delimiterStr, 0, wx.ALL, 5)

        self.headerChkBox = wx.CheckBox(self.importPanel, wx.ID_ANY, u"First row is header", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        importPanelFlexGSizer.Add(self.headerChkBox, 0, wx.ALL, 5)

        self.decorStaticLine = wx.StaticLine(self.importPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        importPanelFlexGSizer.Add(self.decorStaticLine, 0, wx.EXPAND | wx.ALL, 5)

        self.previewBtn = wx.Button(self.importPanel, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0)
        importPanelFlexGSizer.Add(self.previewBtn, 0, wx.ALL, 5)

        self.clearBtn = wx.Button(self.importPanel, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0)
        importPanelFlexGSizer.Add(self.clearBtn, 0, wx.ALL, 5)

        self.importPanel.SetSizer(importPanelFlexGSizer)
        self.importPanel.Layout()
        importPanelFlexGSizer.Fit(self.importPanel)
        importBoxSizer.Add(self.importPanel, 1, wx.EXPAND | wx.ALL, 5)

        self.gridPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.gridPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.gridPanelBoxSizer = wx.BoxSizer()

        self.previewGrid = wx.grid.Grid(self.gridPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.previewGrid.CreateGrid(1, 1)
        self.previewGrid.EnableEditing(True)
        self.previewGrid.EnableGridLines(True)
        self.previewGrid.EnableDragGridSize(False)
        self.previewGrid.SetMargins(0, 0)

        # Columns
        self.previewGrid.EnableDragColMove(False)
        self.previewGrid.EnableDragColSize(True)
        self.previewGrid.SetColLabelSize(30)
        self.previewGrid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.previewGrid.EnableDragRowSize(True)
        self.previewGrid.SetRowLabelSize(80)
        self.previewGrid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.previewGrid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.gridPanelBoxSizer.Add(self.previewGrid, 0, wx.EXPAND | wx.ALL, 5)

        self.gridPanel.SetSizer(self.gridPanelBoxSizer)
        self.gridPanel.Layout()
        self.gridPanelBoxSizer.Fit(self.gridPanel)
        importBoxSizer.Add(self.gridPanel, 1, wx.EXPAND | wx.ALL, 5)

        self.columnChkList = wx.CheckListBox(self.gridPanel, choices=self.header)
        self.gridPanelBoxSizer.Add(self.columnChkList, 0, wx.EXPAND | wx.ALL, 5)

        self.importBtn = wx.Button(self.gridPanel, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.DefaultSize, 0)
        self.gridPanelBoxSizer.Add(self.importBtn, 0, wx.ALL, 5)
        self.importBtn.Enable(False)

        self.SetSizer(importBoxSizer)

        self.importStatusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.importStatusBar.SetStatusText("Select a file and set the delimiter, then press Preview")

        self.Layout()
        self.Centre(wx.BOTH)

        # Event binds
        self.previewBtn.Bind(wx.EVT_BUTTON, self.BeginPreview)
        self.clearBtn.Bind(wx.EVT_BUTTON, self.ClearPreview)
        self.importBtn.Bind(wx.EVT_BUTTON, self.BeginImport)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def __del__(self):
        pass

    # Events
    def BeginPreview(self, event):
        self.WipePreviewGrid()

        self._path = self.datasetPathFilePickerCtrl.GetPath()
        _header = self.headerChkBox.IsChecked()
        _delimiter = self.delimiterStr.GetValue()

        self._data = []
        _temp = []

        if _delimiter == "":
            self.importStatusBar.SetStatusText("Empty delimiter!")

        elif not os.path.exists(self._path) or not os.path.isfile(self._path):
            self.importStatusBar.SetStatusText("File not found!")

        else:
            _sr = open(self._path, "rt")

            for x in _sr:
                _temp.append(x.split())

            _sr.close()

            for x in _temp:
                self._data.append(x[0].split(_delimiter))

            self.previewGrid.AppendCols(len(self._data[0]) - 1)
            self.previewGrid.AppendRows(len(self._data) - 1)

            for i in range(len(self._data)):
                for j in range(len(self._data[i])):
                    if self.headerChkBox.GetValue() and i == 0:
                        self.header.append(self._data[i][j])
                    else:
                        if self.headerChkBox.GetValue():
                            self.previewGrid.SetCellValue(i - 1, j, self._data[i][j])
                        else:
                            self.previewGrid.SetCellValue(i, j, self._data[i][j])

            if self.headerChkBox.GetValue():
                for i in range(len(self._data[0])):
                    self.previewGrid.SetColLabelValue(i, f"{self.header[i]}")

            else:
                for i in range(len(self._data[0])):
                    self.previewGrid.SetColLabelValue(i, f"Column {i + 1}")

            self.previewGrid.AutoSize()
            self.gridPanelBoxSizer.Fit(self.gridPanel)  # Doesn't seem to actually do much but I'll keep it in

            # Have to "jerk" the window so that the grid is properly fitting
            self.SetSize(360, 144)
            self.SetSize(720, 480)

            self.importStatusBar.SetStatusText("Select the columns to be imported from the checklist, "
                                               "then press Import")

            # Get the column and row count for the OnClose & ClearPreview events,
            # I cannot find a function for wx.Grid to do so
            self.previewcolumnCount = len(self._data[0])
            self.previewrowCount = len(self._data)

            # Update the checklist
            if self.headerChkBox.GetValue():
                self.columnChkList.AppendItems(self.header)
                for i in range(len(self.header)):
                    self.columnChkList.Check(i)
            else:
                for i in range(self.previewcolumnCount):
                    self.columnChkList.Append(f"Column {i + 1}")
                    self.columnChkList.Check(i)

            self.previewHappened = True
            self.importBtn.Enable(True)

    def ClearPreview(self, event):
        self.WipePreview()

    def BeginImport(self, event):
        _purge = []
        _purgeReady = False
        _anySelected = False

        for i in range(self.previewcolumnCount):
            if not self.columnChkList.IsChecked(i):
                _purge.append(i)
                _purgeReady = True
            else:
                _anySelected = True

        if _anySelected:
            if _purgeReady:
                for i in range(len(self._data)):
                    for j in range(len(_purge) - 1, -1, -1):
                        try:
                            self._data[i].pop(_purge[j])
                        except IndexError:
                            pass

            mainFrame._data = self._data
            self.importStatusBar.SetStatusText("Import done, check main window status bar. Select preview again to "
                                               "import a new dataset.")
            mainFrame.InitData()
            self.importBtn.Enable(False)

        else:
            self.importStatusBar.SetStatusText("Select at least one column to import!")

    def OnClose(self, event): # Same as ClearPreview, hides the frame additionally
        importFrame.Show(False)
        self.WipePreview()

    def WipePreview(self): # Needed a separate method for this because this is needed outside events
        # Other elements reset
        self.datasetPathFilePickerCtrl.SetPath("")
        self.delimiterStr.SetValue("")
        self.headerChkBox.SetValue(False)

        # Grid reset - only occurs if grid is not empty, otherwise the interpreter presents me with the Great Red Wall
        # of AttributeError for trying to delete nothing
        if self.previewHappened:
            self.previewGrid.ClearGrid()
            self.previewGrid.DeleteCols(1, self.previewcolumnCount - 1)
            self.previewGrid.DeleteRows(1, self.previewrowCount - 1)
            self.previewGrid.SetColLabelValue(0, "A")
            self.columnChkList.Clear()

        # Status bar reset
        self.importStatusBar.SetStatusText("Select a file and set the delimiter, then press Preview")

        self.previewHappened = False
        self.header = []
        self.importBtn.Enable(False)

    def WipePreviewGrid(self): # Only used in BeginPreview
        # Grid reset - only occurs if grid is not empty, otherwise the interpreter presents me with the Great Red Wall
        # of AttributeError for trying to delete nothing
        if self.previewHappened:
            self.previewGrid.ClearGrid()
            self.previewGrid.DeleteCols(1, self.previewcolumnCount - 1)
            self.previewGrid.DeleteRows(1, self.previewrowCount - 1)
            self.previewGrid.SetColLabelValue(0, "A")
            self.columnChkList.Clear()

        # Status bar reset
        self.importStatusBar.SetStatusText("Select a file and set the delimiter, then press Preview")

        self.previewHappened = False
        self.header = []

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame(wx.Frame):

    def __init__(self, parent):

        # Not form-specific vars
        self._data = []
        self.finalHeader = []

        # Frame init
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Universal Data Analysis", pos=wx.DefaultPosition,
                          size=wx.Size(1280, 720), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(resource_path("app.ico"), wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.mainBar = wx.MenuBar(0)
        self.mainMenu = wx.Menu()
        self.exitMenuItem = wx.MenuItem(self.mainMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.mainMenu.Append(self.exitMenuItem)

        self.mainBar.Append(self.mainMenu, u"Main")

        self.dataMenu = wx.Menu()
        self.importMenuItem = wx.MenuItem(self.dataMenu, wx.ID_ANY, u"Import", wx.EmptyString, wx.ITEM_NORMAL)
        self.dataMenu.Append(self.importMenuItem)

        self.mainBar.Append(self.dataMenu, u"Data")

        self.SetMenuBar(self.mainBar)

        self.mainStatusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.mainStatusBar.SetStatusText("Select 'Data' in the toolbar, then select 'Import' to start")

        mainBoxSizer = wx.BoxSizer(wx.VERTICAL)

        self.mainNotebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.basicPanel = wx.Panel(self.mainNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        basicFlexGSizer = wx.FlexGridSizer(0, 2, 0, 0)
        basicFlexGSizer.SetFlexibleDirection(wx.BOTH)
        basicFlexGSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.datasetNameTxt = wx.StaticText(self.basicPanel, wx.ID_ANY, u"Dataset name:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.datasetNameTxt.Wrap(-1)

        basicFlexGSizer.Add(self.datasetNameTxt, 0, wx.ALL, 5)

        self.datasetNameStr = wx.StaticText(self.basicPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0)
        self.datasetNameStr.Wrap(-1)

        basicFlexGSizer.Add(self.datasetNameStr, 0, wx.ALL, 5)

        self.rowCountTxt = wx.StaticText(self.basicPanel, wx.ID_ANY, u"Row count:", wx.DefaultPosition, wx.DefaultSize,
                                         0)
        self.rowCountTxt.Wrap(-1)

        basicFlexGSizer.Add(self.rowCountTxt, 0, wx.ALL, 5)

        self.rowCountStr = wx.StaticText(self.basicPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0)
        self.rowCountStr.Wrap(-1)

        basicFlexGSizer.Add(self.rowCountStr, 0, wx.ALL, 5)

        self.columnCountTxt = wx.StaticText(self.basicPanel, wx.ID_ANY, u"Column count:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.columnCountTxt.Wrap(-1)

        basicFlexGSizer.Add(self.columnCountTxt, 0, wx.ALL, 5)

        self.columnCountStr = wx.StaticText(self.basicPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0)
        self.columnCountStr.Wrap(-1)

        basicFlexGSizer.Add(self.columnCountStr, 0, wx.ALL, 5)

        self.basicPanel.SetSizer(basicFlexGSizer)
        self.basicPanel.Layout()
        basicFlexGSizer.Fit(self.basicPanel)
        self.mainNotebook.AddPage(self.basicPanel, u"Basic", False)
        self.stat1Panel = wx.Panel(self.mainNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        stat1FlexGSizer = wx.FlexGridSizer(0, 2, 0, 0)
        stat1FlexGSizer.SetFlexibleDirection(wx.BOTH)
        stat1FlexGSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.stat1Grid = wx.grid.Grid(self.stat1Panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.stat1Grid.CreateGrid(3, 1)
        self.stat1Grid.EnableEditing(False)
        self.stat1Grid.EnableGridLines(True)
        self.stat1Grid.EnableDragGridSize(False)
        self.stat1Grid.SetMargins(0, 0)

        # Columns
        self.stat1Grid.EnableDragColMove(False)
        self.stat1Grid.EnableDragColSize(True)
        self.stat1Grid.SetColLabelSize(30)
        self.stat1Grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.stat1Grid.EnableDragRowSize(True)
        self.stat1Grid.SetRowLabelSize(80)
        self.stat1Grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance
        self.stat1Grid.SetRowLabelValue(0, "Average")
        self.stat1Grid.SetRowLabelValue(1, "Mode")
        self.stat1Grid.SetRowLabelValue(2, "SD")

        # Cell Defaults
        self.stat1Grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        stat1FlexGSizer.Add(self.stat1Grid, 0, wx.ALL, 5)

        self.stat1Panel.SetSizer(stat1FlexGSizer)
        self.stat1Panel.Layout()
        stat1FlexGSizer.Fit(self.stat1Panel)
        self.mainNotebook.AddPage(self.stat1Panel, u"Stat1", True)
        self.graphsPanel = wx.Panel(self.mainNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        graphsFlexGSizer = wx.FlexGridSizer(0, 2, 0, 0)
        graphsFlexGSizer.SetFlexibleDirection(wx.BOTH)
        graphsFlexGSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        graphtypeChoiceChoices = [u"Line", u"Box", u"Histogram", u"Scatter matrix"]
        self.graphtypeChoice = wx.Choice(self.graphsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         graphtypeChoiceChoices, 0)
        self.graphtypeChoice.SetSelection(0)
        graphsFlexGSizer.Add(self.graphtypeChoice, 0, wx.ALL, 5)

        self.columnChoiceChkLB = wx.CheckListBox(self.graphsPanel, choices=[])
        graphsFlexGSizer.Add(self.columnChoiceChkLB, 0, wx.EXPAND | wx.ALL, 5)

        self.showBtn = wx.Button(self.graphsPanel)
        self.showBtn.SetLabelText("Show")
        self.showBtn.Disable()
        graphsFlexGSizer.Add(self.showBtn, 1, wx.EXPAND | wx.ALL, 5)

        self.graphsPanel.SetSizer(graphsFlexGSizer)
        self.graphsPanel.Layout()
        graphsFlexGSizer.Fit(self.graphsPanel)
        self.mainNotebook.AddPage(self.graphsPanel, u"Graphs", False)

        mainBoxSizer.Add(self.mainNotebook, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(mainBoxSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.ExitApp, id=self.exitMenuItem.GetId())
        self.Bind(wx.EVT_MENU, self.OpenImport, id=self.importMenuItem.GetId())
        self.Bind(wx.EVT_BUTTON, self.ShowGraph, id=self.showBtn.GetId())
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def __del__(self):
        pass

    # Events
    def ExitApp(self, event):
        importFrame.Destroy()
        self.Destroy()

    def OpenImport(self, event):
        importFrame.Show()

    def ShowGraph(self, event):
        # Convert string to float
        for i in range(len(self._data)):
            for j in range(len(self._data[i])):
                try:
                    self._data[i][j] = float(self._data[i][j])
                except ValueError:
                    self._data[i][j] = 0.0

        # Check what columns are checked
        checked = []

        for i in range(len(self._data[0])):
            if self.columnChoiceChkLB.IsChecked(i):
                checked.append(i)
            else:
                pass

        # Include the selected columns only - apparently just one attribute in read_csv, not in the bloody DataFrame
        _temp = [[] for x in range(len(self._data))]

        for i in range(len(self._data)):
            for j in range(len(self._data[i])):
                if j in checked:
                    _temp[i].append(self._data[i][j])

        # Include the headers needed for the selected columns only
        _tempHeader = []
        for i in range(len(self.finalHeader)):
            if i in checked:
                _tempHeader.append(self.finalHeader[i])

        dataset = DataFrame(_temp, columns=_tempHeader)

        if self.graphtypeChoice.GetSelection() == 0:  # Line
            dataset.plot(subplots=True, layout=(len(checked), 1))
            pyplot.show()

        elif self.graphtypeChoice.GetSelection() == 1:  # Box
            dataset.plot(kind='box', subplots=True, layout=(len(checked), 1))
            pyplot.show()

        elif self.graphtypeChoice.GetSelection() == 2:  # Histogram
            dataset.hist()
            pyplot.show()

        elif self.graphtypeChoice.GetSelection() == 3:  # Scatter matrix
            scatter_matrix(dataset)
            pyplot.show()

    def OnClose(self, event):
        importFrame.Destroy()
        self.Destroy()

    # Other functions

    # Set up the grid and calculate values
    def InitData(self):
        # Purge phase
        self.stat1Grid.ClearGrid()
        if not len(self.finalHeader) == 0:
            if not self.stat1Grid.GetNumberCols() <= 1:
                self.stat1Grid.DeleteCols(1, len(self.finalHeader) - 1)
            self.finalHeader = []
            self.columnChoiceChkLB.Clear()

        self.datasetNameStr.SetLabel(f"{Path(importFrame._path).name}")
        self.rowCountStr.SetLabel(f"{len(self._data)}")
        self.columnCountStr.SetLabel(f"{len(self._data[0])}")

        self.stat1Grid.AppendCols(len(self._data[0]) - 1)

        # Calc average and prep mode calc for each column (assume all values are numbers for now)
        self.mainStatusBar.SetStatusText("Calculating average..")

        _nanFound = False
        _nanFoundWhere = []

        _dataArray = numpy.array(self._data)

        _separated = [[0.0 for x in range(len(self._data))] for y in
                      range(len(self._data[0]))]  # Predefined 2D array; each array inside is one column
        for i in range(len(self._data[0])):
            _sum = 0
            for j in range(len(self._data)):
                try:
                    _sum += float(self._data[j][i])
                    _separated[i][j] = float(self._data[j][i])
                except ValueError:
                    _nanFound = True
                    _nanFoundWhere.append([j + 1, i + 1])

            _value = _sum / len(self._data)
            _value2 = numpy.mean(_separated[i])
            self.stat1Grid.SetCellValue(0, i, f"{_value}")

        # Mode and standard dev calculation
        self.mainStatusBar.SetStatusText("Calculating mode and standard deviation.. This will take a while!")

        for i in range(len(_separated)):
            _mode = 0.0
            _modeMax = 0

            _sumSD = 0
            for j in range(len(_separated[i])):
                if _separated[i].count(_separated[i][j]) > _modeMax:
                    _mode = _separated[i][j]
                    _modeMax = _separated[i].count(_separated[i][j])

                if math.isnan(_separated[i][j]):
                    pass
                else:
                    _sumSD += math.pow((_separated[i][j] - float(self.stat1Grid.GetCellValue(0, i))), 2)
            self.stat1Grid.SetCellValue(1, i, f"{_mode}; {_modeMax}")
            self.stat1Grid.SetCellValue(2, i, f"{math.sqrt((_sumSD / len(self._data)))}")
            self.stat1Grid.SetCellValue(2, i, f"{std(_separated[i])}")

        # Fit the grid size and send log if NaN found
        self.stat1Grid.Fit()
        if _nanFound == False:
            self.mainStatusBar.SetStatusText("All ready!")
        else:
            self.mainStatusBar.SetStatusText(
                "Warning, NaN found in dataset! Check warningLog.txt! Stat values are inaccurate as a result!")
            _sw = open("warningLog.txt", "wt")

            _sw.write("NaN (Not a Number) warning [row; column]:")
            for x in _nanFoundWhere:
                _sw.write(f"\n{x}")
            _sw.close()

        # Under Graphs tab add each column to checkbox-list and enable Graphs
        if importFrame.headerChkBox.GetValue():
            self.columnChoiceChkLB.AppendItems(importFrame.header)

            for i in range(len(importFrame.header)):
                self.finalHeader.append(importFrame.header[i])
                self.stat1Grid.SetColLabelValue(i, importFrame.header[i])

        else:
            for i in range(len(self._data[0])):
                self.columnChoiceChkLB.Append(f"Column {i + 1}")
                self.finalHeader.append(f"Column {i + 1}")
                self.stat1Grid.SetColLabelValue(i, f"Column {i + 1}")

        for i in range(len(self._data[0])):
            self.columnChoiceChkLB.Check(i)

        self.showBtn.Enable()

# Retrieve path of app icon - credits to https://stackoverflow.com/a/13790741
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Firing up the app
mainApp = wx.App()
mainFrame = mainFrame(None)
importFrame = importFrame(None)

mainFrame.Show()
mainApp.MainLoop()