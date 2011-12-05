from zope.component import adapts
from zope.interface import implements

from Products.Zuul.interfaces import IReportable

from ZenPacks.zenoss.ZenETL.reportable \
    import Reportable, MARKER_LENGTH, DEFAULT_STRING_LENGTH

from .ExampleComponent import ExampleComponent


class BaseReportable(Reportable):
    """Abstract base class for our customer IReportable implementations."""

    def __init__(self, context):
        self.context = context


class ExampleComponentReportable(BaseReportable):
    implements(IReportable)
    adapts(ExampleComponent)

    @property
    def entity_class_name(self):
        return 'example_component'

    def reportProperties(self):
        """
        We want to export our two custom properties to the data warehouse for
        reporting.
        """
        return [
            ('attributeOne', 'int',
                self.context.attributeOne, MARKER_LENGTH),

            ('attributeTwo', 'string',
                self.context.attributeTwo, DEFAULT_STRING_LENGTH),
        ]
