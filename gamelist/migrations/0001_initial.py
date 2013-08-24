# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'gamelist_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'gamelist', ['Game'])

        # Adding model 'Connection'
        db.create_table(u'gamelist_connection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gamelist.Game'])),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'gamelist', ['Connection'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'gamelist_game')

        # Deleting model 'Connection'
        db.delete_table(u'gamelist_connection')


    models = {
        u'gamelist.connection': {
            'Meta': {'object_name': 'Connection'},
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gamelist.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'gamelist.game': {
            'Meta': {'object_name': 'Game'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['gamelist']