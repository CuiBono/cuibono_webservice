# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table('cuibono_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('raw_content', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('cuibono', ['Article'])

        # Adding model 'Quotation'
        db.create_table('cuibono_quotation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('segment', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cuibono.Article'])),
        ))
        db.send_create_signal('cuibono', ['Quotation'])

        # Adding model 'Funder'
        db.create_table('cuibono_funder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('cuibono', ['Funder'])

        # Adding model 'Ad'
        db.create_table('cuibono_ad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('transcript', self.gf('django.db.models.fields.TextField')(max_length=5000, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('ingested', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('duplicate', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('cuibono', ['Ad'])

        # Adding M2M table for field articles on 'Ad'
        db.create_table('cuibono_ad_articles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ad', models.ForeignKey(orm['cuibono.ad'], null=False)),
            ('article', models.ForeignKey(orm['cuibono.article'], null=False))
        ))
        db.create_unique('cuibono_ad_articles', ['ad_id', 'article_id'])

        # Adding M2M table for field funders on 'Ad'
        db.create_table('cuibono_ad_funders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ad', models.ForeignKey(orm['cuibono.ad'], null=False)),
            ('funder', models.ForeignKey(orm['cuibono.funder'], null=False))
        ))
        db.create_unique('cuibono_ad_funders', ['ad_id', 'funder_id'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table('cuibono_article')

        # Deleting model 'Quotation'
        db.delete_table('cuibono_quotation')

        # Deleting model 'Funder'
        db.delete_table('cuibono_funder')

        # Deleting model 'Ad'
        db.delete_table('cuibono_ad')

        # Removing M2M table for field articles on 'Ad'
        db.delete_table('cuibono_ad_articles')

        # Removing M2M table for field funders on 'Ad'
        db.delete_table('cuibono_ad_funders')


    models = {
        'cuibono.ad': {
            'Meta': {'object_name': 'Ad'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cuibono.Article']", 'symmetrical': 'False', 'blank': 'True'}),
            'duplicate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'funders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cuibono.Funder']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingested': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'transcript': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'blank': 'True'})
        },
        'cuibono.article': {
            'Meta': {'object_name': 'Article'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'raw_content': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'cuibono.funder': {
            'Meta': {'object_name': 'Funder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cuibono.quotation': {
            'Meta': {'object_name': 'Quotation'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cuibono.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'segment': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['cuibono']