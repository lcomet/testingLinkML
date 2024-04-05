# Auto generated from testing_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-11-14T11:45:41
# Schema: NAP
#
# id: https://w3id.org/napcore/model
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

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
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NAP = CurieNamespace('nap', 'https://w3id.org/nap')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://example.org/UNKNOWN/skos/')
VANN = CurieNamespace('vann', 'http://purl.org/vocab/vann/')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NAP


# Types
class Kind(Uriorcurie):
    """ type of objects to be represented by a vcard, same as vcard:Kind """
    type_class_uri = VCARD.Kind
    type_class_curie = "vcard:Kind"
    type_name = "kind"
    type_model_uri = NAP.Kind


class Literal(Uriorcurie):
    """ literal values, same as rdfs:Literal """
    type_class_uri = RDFS.Literal
    type_class_curie = "rdfs:Literal"
    type_name = "literal"
    type_model_uri = NAP.Literal


# Class references
class NapMetadataUid(Literal):
    pass


class NAPCORE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF.Organization
    class_class_curie: ClassVar[str] = "foaf:Organization"
    class_name: ClassVar[str] = "NAPCORE"
    class_model_uri: ClassVar[URIRef] = NAP.NAPCORE


@dataclass
class NapMetadata(YAMLRoot):
    """
    Metadata about the NAP (national access point) itself
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Catalog
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "NapMetadata"
    class_model_uri: ClassVar[URIRef] = NAP.NapMetadata

    uid: Union[str, NapMetadataUid] = None
    pointOfContact: Union[str, Kind] = None
    name: Optional[Union[str, Literal]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.uid):
            self.MissingRequiredField("uid")
        if not isinstance(self.uid, NapMetadataUid):
            self.uid = NapMetadataUid(self.uid)

        if self._is_empty(self.pointOfContact):
            self.MissingRequiredField("pointOfContact")
        if not isinstance(self.pointOfContact, Kind):
            self.pointOfContact = Kind(self.pointOfContact)

        if self.name is not None and not isinstance(self.name, Literal):
            self.name = Literal(self.name)

        super().__post_init__(**kwargs)


@dataclass
class CatalogueRecord(YAMLRoot):
    """
    Metadata about the metadata entry in a NAP
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.CatalogRecord
    class_class_curie: ClassVar[str] = "dcat:CatalogRecord"
    class_name: ClassVar[str] = "CatalogueRecord"
    class_model_uri: ClassVar[URIRef] = NAP.CatalogueRecord

    pointOfContact: Union[str, Kind] = None
    date: Optional[str] = None
    language: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.pointOfContact):
            self.MissingRequiredField("pointOfContact")
        if not isinstance(self.pointOfContact, Kind):
            self.pointOfContact = Kind(self.pointOfContact)

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, str) else str(v) for v in self.language]

        super().__post_init__(**kwargs)


# Enumerations
class Obligation(EnumDefinitionImpl):

    Mandatory = PermissibleValue(text="Mandatory")
    Recommended = PermissibleValue(text="Recommended")
    Optional = PermissibleValue(text="Optional")

    _defn = EnumDefinition(
        name="Obligation",
    )

# Slots
class slots:
    pass

slots.uid = Slot(uri=DCT.identifier, name="uid", curie=DCT.curie('identifier'),
                   model_uri=NAP.uid, domain=None, range=URIRef)

slots.name = Slot(uri=DCAT.title, name="name", curie=DCAT.curie('title'),
                   model_uri=NAP.name, domain=None, range=Optional[Union[str, Literal]])

slots.pointOfContact = Slot(uri=DCAT.contactPoint, name="pointOfContact", curie=DCAT.curie('contactPoint'),
                   model_uri=NAP.pointOfContact, domain=None, range=Union[str, Kind])

slots.date = Slot(uri=XSD.dateTime, name="date", curie=XSD.curie('dateTime'),
                   model_uri=NAP.date, domain=None, range=Optional[str])

slots.language = Slot(uri=DCT.language, name="language", curie=DCT.curie('language'),
                   model_uri=NAP.language, domain=None, range=Optional[Union[str, List[str]]])

slots.usageNote = Slot(uri=VANN.usageNote, name="usageNote", curie=VANN.curie('usageNote'),
                   model_uri=NAP.usageNote, domain=None, range=Optional[Union[str, "Obligation"]])