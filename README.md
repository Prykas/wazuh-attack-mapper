# Wazuh ATT&CK Mapper

## Overview

The Wazuh ATT&CK Mapper is an open-source cybersecurity artifact developed to automatically enrich Wazuh security alerts with MITRE ATT&CK framework information.

Security Operations Center (SOC) analysts often need to manually correlate Wazuh alerts with MITRE ATT&CK tactics and techniques to understand adversarial behavior and support incident investigation. This process is repetitive, error-prone, and time-consuming.

The Wazuh ATT&CK Mapper addresses this problem by automatically associating Wazuh rule identifiers with MITRE ATT&CK techniques and generating structured reports suitable for security analysis and research.

This artifact was developed as part of the Master's Degree in Software Engineering and follows the scientific artifact evaluation principles of availability, functionality, sustainability, and reproducibility.

---

## Problem Statement

Wazuh generates security alerts containing rule identifiers, descriptions, and contextual information. However, these alerts do not always provide an explicit and consolidated mapping to MITRE ATT&CK techniques.

As a result, SOC analysts must manually interpret alerts to determine:

* Which adversarial technique is involved.
* Which ATT&CK tactic is being executed.
* The security relevance of the event.
* The potential stage of the attack lifecycle.

This manual process increases analysis time and may introduce inconsistencies.

---

## Objectives

The main objective of this project is to:

* Parse Wazuh alert files in JSON format.
* Associate Wazuh Rule IDs with MITRE ATT&CK techniques.
* Enrich alerts with ATT&CK metadata.
* Generate structured CSV reports.
* Demonstrate the use of Generative AI in the assisted development of cybersecurity software artifacts.

---

## Architecture

```text
Wazuh Alert JSON
        │
        ▼
    parser.py
        │
        ▼
 Processed Alerts
        │
        ▼
    mapper.py
        │
        ▼
 MITRE-Enriched Alerts
        │
        ▼
report_generator.py
        │
        ▼
 MITRE Report CSV
```

---

## Repository Structure

```text
wazuh-attack-mapper/
│
├── data/
│   └── mitre_mapping.json
│
├── docs/
│
├── examples/
│   └── sample_alerts.json
│
├── reports/
│   └── mitre_report.csv
│
├── src/
│   ├── parser.py
│   ├── mapper.py
│   └── report_generator.py
│
├── tests/
│   ├── test_parser.py
│   └── test_mapper.py
│
├── README.md
│
└── requirements.txt
```

---

## Components

### parser.py

Responsible for:

* Reading Wazuh alert files.
* Validating JSON structure.
* Extracting relevant fields.

Extracted fields:

* rule_id
* description
* groups
* agent

---

### mapper.py

Responsible for:

* Loading MITRE ATT&CK mappings.
* Associating Wazuh Rule IDs with ATT&CK techniques.
* Enriching alerts with:

  * mitre_id
  * mitre_name
  * tactic

Unknown rules are mapped as:

```text
mitre_id   = Unknown
mitre_name = Unknown
tactic     = Unknown
```

---

### report_generator.py

Responsible for:

* Creating the reports directory automatically.
* Exporting enriched alerts to CSV.
* Producing analyst-friendly reports.

Output:

```text
reports/mitre_report.csv
```

---

## Requirements

### Software

* Python 3.11 or newer

### Python Packages

* pytest

Install dependencies:

```bash
python -m pip install pytest
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/SEU_USUARIO/wazuh-attack-mapper.git
```

Enter the project directory:

```bash
cd wazuh-attack-mapper
```

---

## Execution

### Execute the Parser

```bash
python src/parser.py
```

Expected output:

```text
=== ALERTAS PROCESSADOS ===
...
Total de alertas processados: 5
```

---

### Execute the MITRE Mapper

```bash
python src/mapper.py
```

Expected output:

```text
=== ALERTAS ENRIQUECIDOS ===
...
Total de alertas enriquecidos: 5
```

---

### Generate the CSV Report

```bash
python src/report_generator.py
```

Expected output:

```text
Relatório CSV gerado com sucesso!
```

Generated file:

```text
reports/mitre_report.csv
```

---

## Automated Tests

Run all tests:

```bash
python -m pytest
```

Expected result:

```text
6 passed
```

Current test coverage includes:

### Parser Tests

* JSON loading validation
* Alert count validation
* Alert structure validation

### Mapper Tests

* MITRE mapping validation
* Specific Rule ID mapping validation
* Unknown Rule ID handling validation

---

## Example Output

```csv
rule_id,description,agent,mitre_id,mitre_name,tactic
5710,sshd: authentication failed,linux-server,T1110,Brute Force,Credential Access
5712,Multiple authentication failures detected,linux-server,T1110,Brute Force,Credential Access
5763,Successful SSH login,linux-server,T1078,Valid Accounts,Defense Evasion
554,Possible privilege escalation detected,web-server,T1068,Exploitation for Privilege Escalation,Privilege Escalation
31533,SQL Injection attempt detected,apache-server,T1190,Exploit Public-Facing Application,Initial Access
```

---

## Reproducibility

This artifact was designed to be reproducible by independent evaluators.

To reproduce the results:

1. Clone the repository.
2. Install Python 3.11+.
3. Install pytest.
4. Execute the provided scripts.
5. Run automated tests.
6. Compare generated CSV reports.

All required datasets and mappings are included in the repository.

---

## Sustainability

The project adopts a modular architecture:

* parser.py
* mapper.py
* report_generator.py

This design allows future extensions such as:

* Native MITRE ATT&CK API integration
* ATT&CK Navigator export
* Additional Wazuh rule coverage
* Dashboard generation
* SIEM integration

---

## Availability

The artifact is publicly available through GitHub and includes:

* Source code
* Sample dataset
* Documentation
* Tests
* Usage instructions

---

## AI-Assisted Development

This artifact was developed using Generative Artificial Intelligence assistance.

AI was used for:

* Code generation
* Refactoring
* Documentation generation
* Test generation
* Artifact review

All generated outputs were reviewed, validated, tested, and refined by the author.

---

## References

MITRE ATT&CK Framework

https://attack.mitre.org

Wazuh Documentation

https://documentation.wazuh.com

Python Documentation

https://docs.python.org

Pytest Documentation

https://docs.pytest.org

