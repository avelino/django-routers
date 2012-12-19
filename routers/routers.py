#!/usr/bin/env python
# -*- coding: utf-8 -*-

import django
from django.conf import settings

import random



class AutoRouter(object):

    index = len(settings.DATABASES.keys())

    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen slave.
        """
        if self.index == 1:
            return settings.DATABASES.keys()[0]
        print "aqui: %s" % random.choice([settings.DATABASES.keys()[i] for i in range(0, self.index)])
        return random.choice([settings.DATABASES.keys()[i] for i in range(0, self.index)])

    def db_for_write(self, model, **hints):
        """
        Writes always go to master.
        """
        return settings.DATABASES.keys()[0]

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the master/slave pool.

        Django 1.5 use obj1.state not obj1._state
        """
        if django.get_version() >= "1.5":
            obj1._state = obj1.state
            obj2._state = obj2.state

        db_list = (settings.DATABASES.keys()[i] for i in range(0, self.index))
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_syncdb(self, db, model):
        """
        All non-auth models end up in this pool.
        """
        return True
