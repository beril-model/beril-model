# Auto generated from beril_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-05-15T19:32:38
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
from linkml_runtime.linkml_model.types import Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
BERIL_MODEL = CurieNamespace('beril_model', 'https://w3id.org/turbomam/beril-model/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BERIL_MODEL


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class PersonId(URIorCURIE):
    pass


class MaterialEntityId(NamedThingId):
    pass


class SoilSampleId(MaterialEntityId):
    pass


class DnaExtractId(MaterialEntityId):
    pass


class InformationArtifactId(NamedThingId):
    pass


class ProcessId(NamedThingId):
    pass


class SplittingId(ProcessId):
    pass


class PoolingId(ProcessId):
    pass


@dataclass
class NamedThingCollection(YAMLRoot):
    """
    A multi-valued, inlined-as-list grouping of instances from any class, provided a suitable linking slot is provided
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.NamedThingCollection
    class_class_curie: ClassVar[str] = "beril_model:NamedThingCollection"
    class_name: ClassVar[str] = "NamedThingCollection"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.NamedThingCollection

    material_entities: Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]] = empty_dict()
    processes: Optional[Union[Dict[Union[str, ProcessId], Union[dict, "Process"]], List[Union[dict, "Process"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="material_entities", slot_type=MaterialEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="processes", slot_type=Process, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


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
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.Person
    class_class_curie: ClassVar[str] = "beril_model:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.Person

    id: Union[str, PersonId] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        super().__post_init__(**kwargs)


@dataclass
class PersonCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.PersonCollection
    class_class_curie: ClassVar[str] = "beril_model:PersonCollection"
    class_name: ClassVar[str] = "PersonCollection"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.PersonCollection

    people: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="people", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    """
    An entity that consists of matter. Has an identity that persists over time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.MaterialEntity
    class_class_curie: ClassVar[str] = "beril_model:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    mass_g: Optional[float] = None
    color: Optional[Union[str, "ColorEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        if self.mass_g is not None and not isinstance(self.mass_g, float):
            self.mass_g = float(self.mass_g)

        if self.color is not None and not isinstance(self.color, ColorEnum):
            self.color = ColorEnum(self.color)

        super().__post_init__(**kwargs)


@dataclass
class SoilSample(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.SoilSample
    class_class_curie: ClassVar[str] = "beril_model:SoilSample"
    class_name: ClassVar[str] = "SoilSample"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.SoilSample

    id: Union[str, SoilSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoilSampleId):
            self.id = SoilSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DnaExtract(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.DnaExtract
    class_class_curie: ClassVar[str] = "beril_model:DnaExtract"
    class_name: ClassVar[str] = "DnaExtract"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.DnaExtract

    id: Union[str, DnaExtractId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DnaExtractId):
            self.id = DnaExtractId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InformationArtifact(NamedThing):
    """
    Anything that informs, or reduces uncertainty. Can be about a material entity or a process.
    """
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
    An entity that unfolds over time. Not composed of matter.
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
class Splitting(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.Splitting
    class_class_curie: ClassVar[str] = "beril_model:Splitting"
    class_name: ClassVar[str] = "Splitting"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.Splitting

    id: Union[str, SplittingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SplittingId):
            self.id = SplittingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Pooling(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BERIL_MODEL.Pooling
    class_class_curie: ClassVar[str] = "beril_model:Pooling"
    class_name: ClassVar[str] = "Pooling"
    class_model_uri: ClassVar[URIRef] = BERIL_MODEL.Pooling

    id: Union[str, PoolingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PoolingId):
            self.id = PoolingId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class ColorEnum(EnumDefinitionImpl):

    RED = PermissibleValue(
        text="RED",
        description="red")
    GREEN = PermissibleValue(
        text="GREEN",
        description="gree")
    BLUE = PermissibleValue(
        text="BLUE",
        description="blue")

    _defn = EnumDefinition(
        name="ColorEnum",
    )

# Slots
class slots:
    pass

slots.first_name = Slot(uri=BERIL_MODEL.first_name, name="first_name", curie=BERIL_MODEL.curie('first_name'),
                   model_uri=BERIL_MODEL.first_name, domain=None, range=Optional[str])

slots.last_name = Slot(uri=BERIL_MODEL.last_name, name="last_name", curie=BERIL_MODEL.curie('last_name'),
                   model_uri=BERIL_MODEL.last_name, domain=None, range=Optional[str])

slots.people = Slot(uri=BERIL_MODEL.people, name="people", curie=BERIL_MODEL.curie('people'),
                   model_uri=BERIL_MODEL.people, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=BERIL_MODEL.id, domain=None, range=URIRef,
                   pattern=re.compile(r'[a-zA-Z0-9_]+:[a-zA-Z0-9_]+'))

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=BERIL_MODEL.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=BERIL_MODEL.description, domain=None, range=Optional[str])

slots.mass_g = Slot(uri=BERIL_MODEL.mass_g, name="mass_g", curie=BERIL_MODEL.curie('mass_g'),
                   model_uri=BERIL_MODEL.mass_g, domain=None, range=Optional[float])

slots.color = Slot(uri=BERIL_MODEL.color, name="color", curie=BERIL_MODEL.curie('color'),
                   model_uri=BERIL_MODEL.color, domain=None, range=Optional[Union[str, "ColorEnum"]])

slots.inputs = Slot(uri=BERIL_MODEL.inputs, name="inputs", curie=BERIL_MODEL.curie('inputs'),
                   model_uri=BERIL_MODEL.inputs, domain=None, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.outputs = Slot(uri=BERIL_MODEL.outputs, name="outputs", curie=BERIL_MODEL.curie('outputs'),
                   model_uri=BERIL_MODEL.outputs, domain=None, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.material_entities = Slot(uri=BERIL_MODEL.material_entities, name="material_entities", curie=BERIL_MODEL.curie('material_entities'),
                   model_uri=BERIL_MODEL.material_entities, domain=None, range=Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, MaterialEntity]], List[Union[dict, MaterialEntity]]]])

slots.processes = Slot(uri=BERIL_MODEL.processes, name="processes", curie=BERIL_MODEL.curie('processes'),
                   model_uri=BERIL_MODEL.processes, domain=None, range=Optional[Union[Dict[Union[str, ProcessId], Union[dict, Process]], List[Union[dict, Process]]]])

slots.size_in_bytes = Slot(uri=BERIL_MODEL.size_in_bytes, name="size_in_bytes", curie=BERIL_MODEL.curie('size_in_bytes'),
                   model_uri=BERIL_MODEL.size_in_bytes, domain=None, range=Optional[int])

slots.md5 = Slot(uri=BERIL_MODEL.md5, name="md5", curie=BERIL_MODEL.curie('md5'),
                   model_uri=BERIL_MODEL.md5, domain=None, range=Optional[str])

slots.url = Slot(uri=BERIL_MODEL.url, name="url", curie=BERIL_MODEL.curie('url'),
                   model_uri=BERIL_MODEL.url, domain=None, range=Optional[Union[str, URIorCURIE]])