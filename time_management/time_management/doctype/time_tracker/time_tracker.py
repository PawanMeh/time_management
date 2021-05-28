# -*- coding: utf-8 -*-
# Copyright (c) 2021, hello@openetech.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class TimeTracker(Document):
	def validate(self):
		time_sheet = frappe.db.sql('''
						select
							'X'
						from
							`tabTime Tracker`
						where
							user = %s and tt_date = %s and name != %s
						''', (self.user, self.tt_date, self.name))
		if time_sheet:
			frappe.throw(_("Timesheet already exists for the user with same date."))
