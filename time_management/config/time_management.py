# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	data = [
		{	
			"module_name": "Time Management",
			"label": _("Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Client Name",
					"description": _("Client Name")
				},
				{
					"type": "doctype",
					"name": "Task Group",
					"description": _("Task Group")
				},
				{
					"type": "doctype",
					"name": "Engagement Task",
					"description": _("Engagement Task")
				}
			]
		},
		{	
			"module_name": "Time Management",
			"label": _("Time Entry"),
			"items": [
				{
					"type": "doctype",
					"name": "Time Tracker",
					"description": _("Time Tracker")
				}
			]
		}
	]

	return data