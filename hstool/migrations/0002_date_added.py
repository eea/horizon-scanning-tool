# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Figure.added'
        db.add_column(u'hstool_figure', 'added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'GenericElement.added'
        db.add_column(u'hstool_genericelement', 'added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Source.added'
        db.add_column(u'hstool_source', 'added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Assessment.added'
        db.add_column(u'hstool_assessment', 'added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Figure.added'
        db.delete_column(u'hstool_figure', 'added')

        # Deleting field 'GenericElement.added'
        db.delete_column(u'hstool_genericelement', 'added')

        # Deleting field 'Source.added'
        db.delete_column(u'hstool_source', 'added')

        # Deleting field 'Assessment.added'
        db.delete_column(u'hstool_assessment', 'added')


    models = {
        u'hstool.assessment': {
            'Meta': {'object_name': 'Assessment'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'hstool.country': {
            'Meta': {'object_name': 'Country'},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'hstool.driverofchange': {
            'Meta': {'object_name': 'DriverOfChange', '_ormbases': [u'hstool.GenericElement']},
            u'genericelement_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hstool.GenericElement']", 'unique': 'True', 'primary_key': 'True'}),
            'steep_category': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'time_horizon': ('django.db.models.fields.IntegerField', [], {}),
            'trend_type': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'hstool.environmentaltheme': {
            'Meta': {'ordering': "('-pk',)", 'object_name': 'EnvironmentalTheme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'hstool.figure': {
            'Meta': {'object_name': 'Figure'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'file': ('hstool.models.ContentTypeRestrictedFileField', [], {'content_types': ['application/pdf', 'image/jpg', 'image/jpeg']}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512'})
        },
        u'hstool.genericelement': {
            'Meta': {'object_name': 'GenericElement'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hstool.Country']", 'null': 'True', 'blank': 'True'}),
            'figures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hstool.Figure']", 'null': 'True', 'blank': 'True'}),
            'geographical_scope': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hstool.GeographicalScope']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hstool.Source']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'hstool.geographicalscope': {
            'Meta': {'ordering': "('-pk',)", 'object_name': 'GeographicalScope'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'require_country': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'hstool.indicator': {
            'Meta': {'object_name': 'Indicator', '_ormbases': [u'hstool.GenericElement']},
            u'genericelement_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hstool.GenericElement']", 'unique': 'True', 'primary_key': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hstool.EnvironmentalTheme']"}),
            'timeline': ('django.db.models.fields.IntegerField', [], {}),
            'year_base': ('django.db.models.fields.IntegerField', [], {}),
            'year_end': ('django.db.models.fields.IntegerField', [], {})
        },
        u'hstool.relation': {
            'Meta': {'object_name': 'Relation'},
            'assessment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relations'", 'to': u"orm['hstool.Assessment']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2048'}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dest_relations'", 'to': u"orm['hstool.GenericElement']"}),
            'figures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hstool.Figure']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship_type': ('django.db.models.fields.IntegerField', [], {}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_relations'", 'to': u"orm['hstool.GenericElement']"})
        },
        u'hstool.source': {
            'Meta': {'object_name': 'Source'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_year': ('django.db.models.fields.IntegerField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {'max_length': '2048'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'title_original': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['hstool']