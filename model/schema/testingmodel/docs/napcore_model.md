
# NAP


**metamodel version:** 1.7.0

**version:** 0.0.1





### Classes

 * [CatalogueRecord](CatalogueRecord.md) - Metadata about the metadata entry in a NAP
 * [NapMetadata](NapMetadata.md) - Metadata about the NAP (national access point) itself

### Mixins


### Slots

 * [date](date.md)
 * [language](language.md)
 * [name](name.md)
 * [pointOfContact](pointOfContact.md)
 * [uid](uid.md)
 * [usageNote](usageNote.md) - Indication of the use of the metadata. Possible values Mandatory, Recommended, Optional

### Enums

 * [Obligation](Obligation.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Kind](types/Kind.md)  ([Uriorcurie](types/Uriorcurie.md))  - type of objects to be represented by a vcard, same as vcard:Kind
 * [Literal](types/Literal.md)  ([Uriorcurie](types/Uriorcurie.md))  - literal values, same as rdfs:Literal
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
