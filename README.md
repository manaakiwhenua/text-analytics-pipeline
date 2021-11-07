Please note, this student project was completed and the repository is archived.

The resources in this repository are associated with the following publication:

Scott, Jamie, Kristin Stock, Fraser Morgan, Brandon Whitehead, and David Medyckyj-Scott. “Automated Georeferencing of Antarctic Species.” In 11th International Conference on Geographic Information Science (GIScience 2021) - Part II, edited by Krzysztof Janowicz and Judith A. Verstegen, 208:13:1-13:16. Leibniz International Proceedings in Informatics (LIPIcs). Dagstuhl, Germany: Schloss Dagstuhl – Leibniz-Zentrum für Informatik, 2021. https://doi.org/10.4230/LIPIcs.GIScience.2021.II.13.


### notes
The project had three main facets:
1) Extracting a clean text stream from legacy documents
2) Recognising mentions of species and locations within a document
3) Matching species and loactions mentions and modelling which pairs repesented a genuine species-was-found-at-location relationship

Notebooks contained in this repo and which step they belong to:
 ExtractingText.ipynb (1)
 GeoNames.ipynb (2) (intermediate preparation of GeoNames data)
 RecognisingSpeciesAndLocations.ipynb (2)
 NER Metrics and Matrix Creation.ipynb (2, 3)
 FeatureEngineering.ipynb (3)
 Building Models.ipynb (3)
 Visualisation.ipynb (reporting)

Due to time and scope, step was was paused and steps 2 and 3 were progressed using clean text streams copied directly from the docuemnts in the training set. 
