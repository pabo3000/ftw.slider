# -*- coding: utf-8 -*-
from ftw.slider import _
from ftw.slider.interfaces import IPane
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.directives import form
from plone.directives.form import Schema
from plone.formwidget.contenttree import ContentTreeFieldWidget
from plone.formwidget.contenttree import PathSourceBinder
from plone.namedfile.field import NamedImage
from zope import schema
from zope.interface import implements

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


alignments = SimpleVocabulary(
    [SimpleTerm(value=u'left', title=_(u'links oben')),
     SimpleTerm(value=u'right', title=_(u'rechts unten')), ]
    )


class IPaneSchema(Schema):
    image = NamedImage(
        title=_(u'label_image', default='Image'),
        description=_(u'help_align', default=u"""Bitte beachte: Alle Bilder
        eines Sliders sollten exakt die gleiche Größe haben. Zumindest muss das
        Verhältnis zwischen Breite und Höhe bei jedem Bild des Sliders
        übereinstimmen. Die Breite muss mindestens 1158 px betragen."""),
        required=True,
        )
    form.widget(link=ContentTreeFieldWidget)
    link = schema.Choice(
        title=_(u'label_link', default=u'Link'),
        description=_(u'help_link', default=u''),
        required=False,
        source=PathSourceBinder()
        )
    align = schema.Choice(
        title=_(u'label_align', default=u'Ausrichtung'),
        description=_(u'help_align', default=u"""Der Text lässt sich links oben
        oder rechts unten ausrichten."""),
        required=False,
        vocabulary=alignments,
        default=u'right',
        )


class Pane(Container):
    implements(IPane)
