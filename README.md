# Thesis-Supplementary-Information
Supplementary information related to the software described in 
the Thesis titled 
***"Quality Improvement in the Mapping Process required
for Linked Data publication"*** by Alex Randles and Declan
O'Sullivan at Trinity College Dublin.

## /Chapter-4
This chapter in the thesis details the design and implementation 
of the **Mapping Quality Improvement (MQI) Framework**.
### /First-Iteration-Implementation
This directory contains software related to the 
**Mapping Quality Assessment and Refinement  Component**  
of the MQI framework. The SPARQL query templates used to 
assess and refine the quality 
of R2[RML] mappings. In addition, software associated 
with the demonstration walkthrough
of this iteration in **Section 4.2.2**.
##### /SPARQL-Templates
This directory contains the following two sub-directories:

| Sub-Directory        | Description| 
| :-------------:|:-------------:| 
| [/Quality-Metrics](./Chapter-4/First-Iteration-Implementation/SPARQL-Templates/Quality-Metrics)| This directory contains the query templates used to execute quality metrics | 
| [/Quality-Refinements](./Chapter-4/First-Iteration-Implementation/SPARQL-Templates/Quality-Refinements)| This directory contains the query templates used to execute quality refinements | 


The following abbreviations are used in these queries: 
`?sm` is the identifier of a subject map. 
`?pom` is the identifier of a predicate object map. 
`?om` is the identifier of an object map. 



##### /Demonstration-Walkthrough
This directory contains the R2RML mapping 
([demo_mapping.ttl](Chapter-4/First-Iteration-Implementation/Demonstration-Walkthrough/demo_mapping.ttl)) 
which was used during the demonstration in **Section 4.2.2**.
In addition, the quality report 
([demo_quality_report.ttl](Chapter-4/First-Iteration-Implementation/Demonstration-Walkthrough/demo_quality_report.ttl)) 
generated by the framework and a sample 
refined mapping
([demo_refined_mapping..ttl](Chapter-4/First-Iteration-Implementation/Demonstration-Walkthrough/demo_refined_mapping.ttl)) 
and validation report 
([demo_validation_report.ttl](Chapter-4/First-Iteration-Implementation/Demonstration-Walkthrough/demo_validation_report.ttl)).
 
 
### /Second-Iteration-Implementation
This directory contains software related to the 
**Change Detection Component** of the MQI framework described in **Section 4.2.3**. 
An R2RML mapping
([change_detection_mapping.ttl](./Chapter-4/Second-Iteration-Implementation/change_detection_mapping.ttl)) 
is used to transform detected changes. 
SPARQL queries in the directory are used to process and link the resulting graphs. 

The [/Sample-Graphs](./Chapter-4/Sample-Graphs) folder contains a sample RDF graph represented in the Mapping Quality Improvement Ontology (MQIO)
and Ontology for Source Change Detection (OSCD).

&nbsp;
&nbsp;
&nbsp;
&nbsp;

## /Chapter-5
This chapter in the thesis details the evaluation of the MQI Framework. 
#### /Experiment-1
This directory contains sub-directories
containing the input R2RML mappings and associated quality reports 
(validation_report.ttl) generated by MQI framework. In addition, 
the quality reports have been output into named graphs 
([experiment_1_reports.trig](./Chapter-5/Experiment-1/experiment_1_reports.trig)).
This experiment is described in **Section 5.3**. 
#### /Experiment-2
This directory contains the R2RML mapping 
([evaluation_mapping.ttl](./Chapter-5/Experiment-2/evaluation_mapping.ttl)) 
with 3 quality violations, which 
was used to test the **effectiveness** of the MQI Framework. 
In addition, the quality report 
([evaluation_quality_report.ttl](./Chapter-5/Experiment-2/evaluation_quality_report.ttl)) 
generated by the framework and a sample 
refined mapping
([sample_refined_mapping..ttl](./Chapter-5/Experiment-2/sample_refined_mapping.ttl)) 
and validation report 
([sample_validation_report..ttl](./Chapter-5/Experiment-2/sample_validation_report.ttl)).
This experiment is described in **Section 5.4**. 

#### /Experiment-3
This directory contains the RML mapping 
([evaluation_mapping.ttl](./Chapter-5/Experiment-3/evaluation_mapping.ttl)) 
related to the input source data ([evaluation_source_data-1.ttl](./Chapter-5/Experiment-3/evaluation_source_data-1.csv), [evaluation_source_data-2.ttl](./Chapter-5/Experiment-3/evaluation_source_data-2.csv))
, which was used to test the **understanding** of the MQI Framework. 
In addition, the change report
([evaluation_change_log.ttl](./Chapter-5/Experiment-3/evaluation_change_log.ttl)) 
generated by the framework detecting changes in the source data.
This experiment is described in **Section 5.5**. 

#### /Experiment-4
This directory contains the direct responses ([MQIO_Feedback.csv](./Chapter-5/Experiment-4/MQIO_Feedback.csv)) 
from the questionnaire ([MQIO_Questionnaire.pdf](./Chapter-5/Experiment-4/MQIO_Questionnaire.pdf)) 
which asked ontology design experts about the design of the 
**Mapping Quality Improvement Ontology (MQIO)**. 
The results of this experiment are described in **Section 5.6**. 


#### /Experiment-5
This directory contains the direct responses ([OSCD_Feedback.csv](./Chapter-5/Experiment-5/OSCD_Feedback.csv)) 
from the questionnaire ([OSCD_Questionnaire.pdf](./Chapter-5/Experiment-5/OSCD_Questionnaire.pdf)) 
which asked ontology design experts about the design of the 
**Ontology for Source Change Detection (OSCD)**. 
The results of this experiment are described in **Section 5.6**. 

#### /Ontology-Versions
All versions of the **MQIO** and **OSCD** are stored in the following two sub-directories:

| Sub-Directory        | Description| 
| :-------------:|:-------------:| 
| [/MQIO-Versions](./Chapter-5/Ontology-Versions/MQIO-Versions)| Version 1.0 - 1.3 of the [Mapping Quality Improvement Ontology (MQIO)](https://w3id.org/MQIO)| 
| [/OSCD-Versions](./Chapter-5/Ontology-Versions/OSCD-Versions)| Version 1.0 - 1.2 of the [Ontology for Source Change Detection (OSCD)](https://w3id.org/OSCD)| 
 

#### /Application-Study
This directory relates to **Section 5.7** and contains the following two sub-directories:

| Sub-Directory        | Description| 
| :-------------:|:-------------:| 
| [/OSi](./Chapter-5/Application-Study/OSi) [^1]| [Quality Reports](./Chapter-5/Application-Study/OSi) and Refined Mappings involved in the OSi use case described in **Section 5.7.1** | 
| [/Ericsson](./Chapter-5/Application-Study/Ericsson) [^2]| [Quality Reports](./Chapter-5/Application-Study/Ericsson/Mappings) , [Change Logs](./Chapter-5/Application-Study/Ericsson/Change-Logs) and resulting refined mappings involved in the Ericsson use case described in **Section 5.7.2** | 

#### /Improvements
This directory contains files associated with the SHACL[^3] shape generation proposed in **Section 5.8**,
including a sample shape ([sample_shacl_shape.ttl](./Chapter-5/Improvements/sample_shacl_shape.ttl)) 
and associated validation report ([sample_shacl_report.ttl](./Chapter-5/Improvements/sample_shacl_report.ttl)). 


[^1]: https://osi.ie/
[^2]: https://www.ericsson.com/en
[^3]: https://www.w3.org/TR/shacl/
