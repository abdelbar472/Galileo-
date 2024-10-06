import uuid
from datetime import datetime
from django.db import models
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class BlogPost(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title = columns.Text(required=True)
    content = columns.Text()
    created_at = columns.DateTime(default=datetime.now)
    class Meta:
        app_label = 'galo'
