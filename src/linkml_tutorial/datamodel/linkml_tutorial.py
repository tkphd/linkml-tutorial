# Auto generated from linkml_tutorial.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-09T00:03:27
# Schema: linkml-tutorial
#
# id: https://w3id.org/tkphd/linkml-tutorial
# description: Learning how to use LinkML
# license: MIT

import dataclasses
import sys
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
BIO = CurieNamespace('BIO', 'https://w3id.org/biolink/')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
TUT = CurieNamespace('TUT', 'https://w3id.org/tkphd/linkml-tutorial/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ORCID = CurieNamespace('orcid', 'https://orcid.org/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
WD = CurieNamespace('wd', 'http://www.wikidata.org/entity/')
DEFAULT_ = TUT


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class PersonId(NamedThingId):
    pass


class AnimalId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic entity that has its own name
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = TUT.NamedThing

    id: Union[str, NamedThingId] = None
    age_in_years: Optional[int] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    A specific person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Person
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = TUT.Person

    id: Union[str, PersonId] = None
    vital_status: Union[str, "PersonStatus"] = None
    primary_email: Optional[str] = None
    pets: Optional[Union[dict, "AnimalCollection"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.vital_status):
            self.MissingRequiredField("vital_status")
        if not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.pets is not None and not isinstance(self.pets, AnimalCollection):
            self.pets = AnimalCollection(**as_dict(self.pets))

        super().__post_init__(**kwargs)


@dataclass
class Animal(NamedThing):
    """
    A specific animal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TUT.Animal
    class_class_curie: ClassVar[str] = "TUT:Animal"
    class_name: ClassVar[str] = "Animal"
    class_model_uri: ClassVar[URIRef] = TUT.Animal

    id: Union[str, AnimalId] = None
    species: Optional[Union[str, URIorCURIE]] = None
    breed: Optional[Union[str, URIorCURIE]] = None
    color: Optional[str] = None
    weight_in_mgs: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnimalId):
            self.id = AnimalId(self.id)

        if self.species is not None and not isinstance(self.species, URIorCURIE):
            self.species = URIorCURIE(self.species)

        if self.breed is not None and not isinstance(self.breed, URIorCURIE):
            self.breed = URIorCURIE(self.breed)

        if self.color is not None and not isinstance(self.color, str):
            self.color = str(self.color)

        if self.weight_in_mgs is not None and not isinstance(self.weight_in_mgs, int):
            self.weight_in_mgs = int(self.weight_in_mgs)

        super().__post_init__(**kwargs)


@dataclass
class PersonCollection(YAMLRoot):
    """
    A group of people
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TUT.PersonCollection
    class_class_curie: ClassVar[str] = "TUT:PersonCollection"
    class_name: ClassVar[str] = "PersonCollection"
    class_model_uri: ClassVar[URIRef] = TUT.PersonCollection

    entities: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entities", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class AnimalCollection(YAMLRoot):
    """
    A group of animals
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TUT.AnimalCollection
    class_class_curie: ClassVar[str] = "TUT:AnimalCollection"
    class_name: ClassVar[str] = "AnimalCollection"
    class_model_uri: ClassVar[URIRef] = TUT.AnimalCollection

    animals: Optional[Union[Dict[Union[str, AnimalId], Union[dict, Animal]], List[Union[dict, Animal]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="animals", slot_type=Animal, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):
    """
    Vital status of a person
    """
    alive = PermissibleValue(text="alive",
                                 description="The person is alive",
                                 meaning=PATO["0001421"])
    dead = PermissibleValue(text="dead",
                               description="The person is deceased",
                               meaning=PATO["0001422"])
    unknown = PermissibleValue(text="unknown",
                                     description="The vital status of this person is unknown")

    _defn = EnumDefinition(
        name="PersonStatus",
        description="Vital status of a person",
    )

class Breeds(EnumDefinitionImpl):
    """
    Collection of known breeds
    """
    _defn = EnumDefinition(
        name="Breeds",
        description="Collection of known breeds",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=TUT.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=TUT.name, domain=None, range=Optional[str])

slots.age_in_years = Slot(uri=TUT.age_in_years, name="age_in_years", curie=TUT.curie('age_in_years'),
                   model_uri=TUT.age_in_years, domain=None, range=Optional[int])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=TUT.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.pets = Slot(uri=TUT.pets, name="pets", curie=TUT.curie('pets'),
                   model_uri=TUT.pets, domain=None, range=Optional[Union[dict, AnimalCollection]])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=TUT.primary_email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.vital_status = Slot(uri=TUT.vital_status, name="vital_status", curie=TUT.curie('vital_status'),
                   model_uri=TUT.vital_status, domain=None, range=Union[str, "PersonStatus"])

slots.species = Slot(uri=TUT.species, name="species", curie=TUT.curie('species'),
                   model_uri=TUT.species, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.breed = Slot(uri=TUT.breed, name="breed", curie=TUT.curie('breed'),
                   model_uri=TUT.breed, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.color = Slot(uri=TUT.color, name="color", curie=TUT.curie('color'),
                   model_uri=TUT.color, domain=None, range=Optional[str])

slots.weight_in_mgs = Slot(uri=TUT.weight_in_mgs, name="weight_in_mgs", curie=TUT.curie('weight_in_mgs'),
                   model_uri=TUT.weight_in_mgs, domain=None, range=Optional[int])

slots.household_members = Slot(uri=TUT.household_members, name="household_members", curie=TUT.curie('household_members'),
                   model_uri=TUT.household_members, domain=None, range=Optional[Union[str, NamedThingId]])

slots.entities = Slot(uri=TUT.entities, name="entities", curie=TUT.curie('entities'),
                   model_uri=TUT.entities, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])

slots.animals = Slot(uri=TUT.animals, name="animals", curie=TUT.curie('animals'),
                   model_uri=TUT.animals, domain=None, range=Optional[Union[Dict[Union[str, AnimalId], Union[dict, Animal]], List[Union[dict, Animal]]]])

slots.Person_id = Slot(uri=SCHEMA.identifier, name="Person_id", curie=SCHEMA.curie('identifier'),
                   model_uri=TUT.Person_id, domain=Person, range=Union[str, PersonId])