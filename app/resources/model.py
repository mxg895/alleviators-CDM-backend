# from sqlalchemy.ext.mutable import MutableDict
import uuid
from datetime import datetime
from enum import Enum

from app.extensions import db
from sqlalchemy.dialects.postgresql import ARRAY, ENUM, JSONB, UUID


class Aspect(str, Enum):
    PHYSICAL = 'physical'
    SOCIAL = 'social'
    EMOTIONAL = 'emotional'

    def __str__(self) -> str:
        return str.__str__(self.name)

class Goal(str, Enum):
    PEER_SUPPORT = 'peer-spt'
    MANAGE_PAIN = 'manage-pain'
    PAIN_EDUCATION= 'pain-edu'

    def __str__(self) -> str:
        return str.__str__(self.name)

class SubCategory(str, Enum):
    VIDEO = 'video'
    PROGRAM = 'prgm'
    WEBSITE = 'website'
    APP = 'app'
    READING = 'reading'
    TOOL = 'tool'
    DEVICE = 'device'
    SUPPORT_LINE = 'support-line'
    COMMUNITY_PROGRAM = 'comm-prgm'
    PEER_SUPPORT = 'peer'
    PODCAST = 'pod'

    def __str__(self) -> str:
        return str.__str__(self.name)

class Resource(db.Model):
    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4)
    title = db.Column(
        db.String(150),
        nullable=False)
    description = db.Column(db.Text)
    content = db.Column(db.Text)
    aspect = db.Column(
        ARRAY(ENUM(Aspect)),
        nullable=False)
    goal = db.Column(
        ARRAY(ENUM(Goal)),
        nullable=False)
    sub_category = db.Column(
        ARRAY(ENUM(SubCategory)),
        nullable=False
    )
    image_name = db.Column(db.String(200))
    external_links = db.Column(db.Text)
    created = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False)
    last_updated = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False)

    @property
    def serialize_all(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'content': self.content,
            'aspect': map(lambda enum: enum.name, self.aspect),
            'goal': map(lambda enum: enum.name, self.goal),
            'subcategory': map(lambda enum: enum.name, self.sub_category),
            'imageName': self.image_name,
            'externalLinks': self.external_links,
            'created': self.created.__str__(),
            'lastUpdated': self.last_updated.__str__()
        }

    @property
    def serialize_cover(self):
        print("serializing....")
        return {
            'id': str(self.id),
            'title': self.title,
            # 'description': self.description,
            # 'content': self.content,
            # 'aspect':map(lambda enum: enum.name, self.aspect),
            # 'goal':map(lambda enum: enum.name, self.goal),
            # 'subcategory': map(lambda enum: enum.name, self.sub_category),
            'aspect': [str(a) for a in self.aspect],
            'goal': [str(g) for g in self.goal],
            'subcategory': [str(s) for s in self.sub_category],
            'imageName': self.image_name,
            # 'external-links': self.external_links,
            # 'created': self.created.__str__(),
            # 'last-updated': self.last_updated.__str__()
        }
