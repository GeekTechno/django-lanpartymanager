# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'games_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'games', ['Game'])

        # Adding model 'Instruction'
        db.create_table(u'games_instruction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Game'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'games', ['Instruction'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'games_game')

        # Deleting model 'Instruction'
        db.delete_table(u'games_instruction')


    models = {
        u'games.game': {
            'Meta': {'ordering': "['name']", 'object_name': 'Game'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'games.instruction': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Instruction'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['games.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['games']