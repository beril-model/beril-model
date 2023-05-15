# Auto generated from beril_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-05-05T21:39:24
# Schema: beril-model
#
# id: https://w3id.org/beril-model/beril-model
# description: A proposed LinkML schema for sample interoperability in the Department of Energy's Biological and Environmental Research program
# license: BSD-3

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BERIL_MODEL = CurieNamespace('beril_model', 'https://w3id.org/beril-model/beril-model/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = BERIL_MODEL


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class NonProcessId(NamedThingId):
    pass


class MaterialEntityId(NonProcessId):
    pass


class InformationArtifactId(NonProcessId):
    pass


class ProcessId(NamedThingId):
    pass


class PersonId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Observation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.Observation
    class_class_curie: ClassVar[str] = "beril_model:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.Observation

    raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.raw_value is not None and not isinstance(self.raw_value, str):
            self.raw_value = str(self.raw_value)

        super().__post_init__(**kwargs)


@dataclass
class NonProcess(NamedThing):
    """
    A grouping for any named thing that is not a process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.NonProcess
    class_class_curie: ClassVar[str] = "beril_model:NonProcess"
    class_name: ClassVar[str] = "NonProcess"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.NonProcess

    id: Union[str, NonProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonProcessId):
            self.id = NonProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NonProcess):
    """
    something that is made of matter
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.MaterialEntity
    class_class_curie: ClassVar[str] = "beril_model:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    observations: Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        if not isinstance(self.observations, list):
            self.observations = [self.observations] if self.observations is not None else []
        self.observations = [v if isinstance(v, Observation) else Observation(**as_dict(v)) for v in self.observations]

        super().__post_init__(**kwargs)


@dataclass
class InformationArtifact(NonProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.InformationArtifact
    class_class_curie: ClassVar[str] = "beril_model:InformationArtifact"
    class_name: ClassVar[str] = "InformationArtifact"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.InformationArtifact

    id: Union[str, InformationArtifactId] = None
    size_in_bytes: Optional[int] = None
    md5: Optional[str] = None
    url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationArtifactId):
            self.id = InformationArtifactId(self.id)

        if self.size_in_bytes is not None and not isinstance(self.size_in_bytes, int):
            self.size_in_bytes = int(self.size_in_bytes)

        if self.md5 is not None and not isinstance(self.md5, str):
            self.md5 = str(self.md5)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        super().__post_init__(**kwargs)


@dataclass
class Process(NamedThing):
    """
    Something that unfolds over time
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.Process
    class_class_curie: ClassVar[str] = "beril_model:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.Process

    id: Union[str, ProcessId] = None
    inputs: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()
    outputs: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessId):
            self.id = ProcessId(self.id)

        if not isinstance(self.inputs, list):
            self.inputs = [self.inputs] if self.inputs is not None else []
        self.inputs = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.inputs]

        if not isinstance(self.outputs, list):
            self.outputs = [self.outputs] if self.outputs is not None else []
        self.outputs = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.outputs]

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    Represents a Person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.Person
    class_class_curie: ClassVar[str] = "beril_model:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.Person

    id: Union[str, PersonId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass
class PersonCollection(YAMLRoot):
    """
    A holder for Person objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.PersonCollection
    class_class_curie: ClassVar[str] = "beril_model:PersonCollection"
    class_name: ClassVar[str] = "PersonCollection"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.PersonCollection

    entries: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=BERIL_MODEL.id, domain=None, range=URIRef,
                   pattern=re.compile(r'[a-zA-Z0-9_]+:[a-zA-Z0-9_]+'))

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=BERIL_MODEL.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=BERIL_MODEL.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=BERIL_MODEL.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=BERIL_MODEL.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=BERIL_MODEL.age_in_years, name="age_in_years", curie=BERIL_MODEL.curie('age_in_years'),
                   model_uri=BERIL_MODEL.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=BERIL_MODEL.vital_status, name="vital_status", curie=BERIL_MODEL.curie('vital_status'),
                   model_uri=BERIL_MODEL.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.raw_value = Slot(uri=BERIL_MODEL.raw_value, name="raw_value", curie=BERIL_MODEL.curie('raw_value'),
                   model_uri=BERIL_MODEL.raw_value, domain=None, range=Optional[str])

slots.observations = Slot(uri=BERIL_MODEL.observations, name="observations", curie=BERIL_MODEL.curie('observations'),
                   model_uri=BERIL_MODEL.observations, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.size_in_bytes = Slot(uri=BERIL_MODEL.size_in_bytes, name="size_in_bytes", curie=BERIL_MODEL.curie('size_in_bytes'),
                   model_uri=BERIL_MODEL.size_in_bytes, domain=None, range=Optional[int])

slots.md5 = Slot(uri=BERIL_MODEL.md5, name="md5", curie=BERIL_MODEL.curie('md5'),
                   model_uri=BERIL_MODEL.md5, domain=None, range=Optional[str])

slots.url = Slot(uri=BERIL_MODEL.url, name="url", curie=BERIL_MODEL.curie('url'),
                   model_uri=BERIL_MODEL.url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.inputs = Slot(uri=BERIL_MODEL.inputs, name="inputs", curie=BERIL_MODEL.curie('inputs'),
                   model_uri=BERIL_MODEL.inputs, domain=None, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.outputs = Slot(uri=BERIL_MODEL.outputs, name="outputs", curie=BERIL_MODEL.curie('outputs'),
                   model_uri=BERIL_MODEL.outputs, domain=None, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.personCollection__entries = Slot(uri=BERIL_MODEL.entries, name="personCollection__entries", curie=BERIL_MODEL.curie('entries'),
                   model_uri=BERIL_MODEL.personCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])

slots.Person_primary_email = Slot(uri=SCHEMA.email, name="Person_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=BERIL_MODEL.Person_primary_email, domain=Person, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))