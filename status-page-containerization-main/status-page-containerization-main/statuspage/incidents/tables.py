import django_tables2 as tables

from statuspage.tables import StatusPageTable, columns, TruncatedTextColumn
from .models import Incident, IncidentUpdate, IncidentTemplate


class IncidentTable(StatusPageTable):
    title = tables.Column(
        linkify=True,
    )
    status = tables.Column()
    impact = columns.ChoiceFieldColumn()
    visibility = columns.BooleanColumn()
    user = tables.Column()

    class Meta(StatusPageTable.Meta):
        model = Incident
        fields = ('pk', 'id', 'title', 'status', 'impact', 'visibility', 'user', 'created', 'last_updated')
        default_columns = ('id', 'title', 'status', 'impact', 'visibility', 'user')


class IncidentUpdateTable(StatusPageTable):
    text = TruncatedTextColumn(
        linkify=True,
    )
    new_status = columns.BooleanColumn()
    status = tables.Column()
    user = tables.Column()

    class Meta(StatusPageTable.Meta):
        model = IncidentUpdate
        fields = ('pk', 'id', 'text', 'new_status', 'status', 'user', 'created', 'last_updated')
        default_columns = ('id', 'text', 'new_status', 'status', 'user')


class IncidentTemplateTable(StatusPageTable):
    template_name = tables.Column(
        linkify=True,
    )
    title = tables.Column()
    status = tables.Column()
    impact = columns.ChoiceFieldColumn()
    visibility = columns.BooleanColumn()
    update_component_status = columns.BooleanColumn()

    class Meta(StatusPageTable.Meta):
        model = IncidentTemplate
        fields = ('pk', 'id', 'template_name', 'title', 'status', 'impact', 'visibility', 'update_component_status',
                  'created', 'last_updated')
        default_columns = ('id', 'template_name', 'status', 'impact', 'visibility')
