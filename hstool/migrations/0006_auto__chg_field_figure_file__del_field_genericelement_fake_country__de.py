# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Figure.file'
        db.alter_column(u'hstool_figure', 'file', self.gf('hstool.models.ContentTypeRestrictedFileField')(content_types=['application/pdf', 'image/jpg', 'image/jpeg', 'image/png', 'image/gif']))
        # Deleting field 'GenericElement.fake_country'
        db.delete_column(u'hstool_genericelement', 'fake_country_id')

        # Deleting field 'GenericElement.fake_geographical_scope'
        db.delete_column(u'hstool_genericelement', 'fake_geographical_scope_id')

        # Adding field 'GenericElement.geographical_scope'
        db.add_column(u'hstool_genericelement', 'geographical_scope',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.GeographicalScope'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'GenericElement.country'
        db.add_column(u'hstool_genericelement', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Country'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'Indicator.theme'
        db.alter_column(u'hstool_indicator', 'theme_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.EnvironmentalTheme']))
        # Adding field 'DriverOfChange.uncertainty_type'
        db.add_column(u'hstool_driverofchange', 'uncertainty_type',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Figure.file'
        db.alter_column(u'hstool_figure', 'file', self.gf('hstool.models.ContentTypeRestrictedFileField')(content_types=['application/pdf', 'image/jpg', 'image/jpeg']))
        # Adding field 'GenericElement.fake_country'
        db.add_column(u'hstool_genericelement', 'fake_country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Country'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'GenericElement.fake_geographical_scope'
        db.add_column(u'hstool_genericelement', 'fake_geographical_scope',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.GeographicalScope'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'GenericElement.geographical_scope'
        db.delete_column(u'hstool_genericelement', 'geographical_scope_id')

        # Deleting field 'GenericElement.country'
        db.delete_column(u'hstool_genericelement', 'country_id')


        # Changing field 'Indicator.theme'
        db.alter_column(u'hstool_indicator', 'theme_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.EnvironmentalTheme'], null=False))
        # Deleting field 'DriverOfChange.uncertainty_type'
        db.delete_column(u'hstool_driverofchange', 'uncertainty_type')


    models = {
        u'common.country': {
            'Meta': {'object_name': 'Country'},
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'common.environmentaltheme': {
            'Meta': {'ordering': "('-pk',)", 'object_name': 'EnvironmentalTheme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'common.geographicalscope': {
            'Meta': {'ordering': "('-pk',)", 'object_name': 'GeographicalScope'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'require_country': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'hstool.assessment': {
            'Meta': {'object_name': 'Assessment'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'hstool.driverofchange': {
            'Meta': {'object_name': 'DriverOfChange', '_ormbases': [u'hstool.GenericElement']},
            u'genericelement_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hstool.GenericElement']", 'unique': 'True', 'primary_key': 'True'}),
            'steep_category': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'time_horizon': ('django.db.models.fields.IntegerField', [], {}),
            'trend_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'uncertainty_type': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'hstool.figure': {
            'Meta': {'object_name': 'Figure'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'file': ('hstool.models.ContentTypeRestrictedFileField', [], {'content_types': ['application/pdf', 'image/jpg', 'image/jpeg', 'image/png', 'image/gif']}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512'})
        },
        u'hstool.genericelement': {
            'Meta': {'object_name': 'GenericElement'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Country']", 'null': 'True', 'blank': 'True'}),
            'figures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hstool.Figure']", 'null': 'True', 'blank': 'True'}),
            'geographical_scope': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.GeographicalScope']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hstool.Source']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'hstool.indicator': {
            'Meta': {'object_name': 'Indicator', '_ormbases': [u'hstool.GenericElement']},
            u'genericelement_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hstool.GenericElement']", 'unique': 'True', 'primary_key': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.EnvironmentalTheme']"}),
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