# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from datetime import datetime, time
from django.http import HttpResponse
from groupFactory import PersonFactory

def test_group_letter():
	person = PersonFactory.build(
		group__name='admins')

	assert person.group_letter() == 'A'