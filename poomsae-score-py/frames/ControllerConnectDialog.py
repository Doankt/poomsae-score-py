# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.5 on Tue Feb 25 20:33:13 2020
#

import wx
# begin wxGlade: dependencies
# end wxGlade
import sys
sys.path.append('..')

# begin wxGlade: extracode
import serial.tools.list_ports
import sys
sys.path.append('..')
from controllers.controller import Controller
# end wxGlade



class ControllerConnectDialog(wx.Dialog):
	def __init__(self, *args, **kwds):
		# begin wxGlade: ControllerConnectDialog.__init__
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
		wx.Dialog.__init__(self, *args, **kwds)
		self.port_listbox = wx.ListBox(self, wx.ID_ANY, choices=[], style=wx.LB_HSCROLL | wx.LB_SINGLE)
		self.cancel_button = wx.Button(self, wx.ID_ANY, "Cancel")
		self.confirm_button = wx.Button(self, wx.ID_ANY, "Connect")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_LISTBOX, self.check_valid, self.port_listbox)
		self.Bind(wx.EVT_LISTBOX_DCLICK, self.select_port, self.port_listbox)
		self.Bind(wx.EVT_BUTTON, self.Close, self.cancel_button)
		self.Bind(wx.EVT_BUTTON, self.connect_button_handler, self.confirm_button)
		# end wxGlade

		self.parent = args[0]
		self.parent.Disable()
		self.c_num = args[0].last_called_button.c_num
		print(self.c_num)

	def __set_properties(self):
		# begin wxGlade: ControllerConnectDialog.__set_properties
		self.SetTitle("dialog")
		self.confirm_button.Enable(False)
		# end wxGlade

		self.ports = serial.tools.list_ports.comports()
		if len(self.ports) > 1:
			self.port_listbox.InsertItems([p.description for p in self.ports], 0)
		else:
			self.port_listbox.InsertItems(['No Devices Found'], 0)

	def __do_layout(self):
		# begin wxGlade: ControllerConnectDialog.__do_layout
		sizer_16 = wx.BoxSizer(wx.VERTICAL)
		sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_16.Add(self.port_listbox, 1, wx.ALL | wx.EXPAND, 10)
		sizer_6.Add(self.cancel_button, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 0)
		sizer_6.Add(self.confirm_button, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 0)
		sizer_16.Add(sizer_6, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 10)
		self.SetSizer(sizer_16)
		sizer_16.Fit(self)
		self.Layout()
		# end wxGlade


	def check_valid(self, event):  # wxGlade: ControllerConnectDialog.<event_handler>
		print(self.port_listbox.GetString(self.port_listbox.GetSelection()))
		if self.port_listbox.GetString(self.port_listbox.GetSelection()) == 'No Devices Found':
			self.confirm_button.Disable()
		else:
			self.confirm_button.Enable()
		
	def select_port(self, event):  # wxGlade: ControllerConnectDialog.<event_handler>
		if self.port_listbox.GetString(self.port_listbox.GetSelection()) != 'No Devices Found':
			self.connect_button_handler(event)

	def connect_button_handler(self, event):  # wxGlade: ControllerConnectDialog.<event_handler>
		controller = wx.App.Get()

		c = Controller(self.ports[self.port_listbox.GetSelection()].device, controller, self.c_num)
		c.start()

		print(controller.controller_list)
		self.Close(event)

	def Close(self, event):  # wxGlade: ControllerConnectDialog.<event_handler>
		self.parent.Enable()
		self.Destroy()
# end of class ControllerConnectDialog
