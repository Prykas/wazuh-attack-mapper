from pathlib import Path

from src.parser import load_alerts
from src.mapper import load_mapping, enrich_alerts


def test_known_mapping_5710():
    """
    Verifica o mapeamento da regra 5710.
    """

    project_root = Path(__file__).parent.parent

    alerts_file = (
        project_root / "examples" / "sample_alerts.json"
    )

    mapping_file = (
        project_root / "data" / "mitre_mapping.json"
    )

    alerts = load_alerts(str(alerts_file))
    mapping = load_mapping(str(mapping_file))

    enriched = enrich_alerts(alerts, mapping)

    alert = next(
        a for a in enriched
        if a["rule_id"] == "5710"
    )

    assert alert["mitre_id"] == "T1110"


def test_known_mapping_31533():
    """
    Verifica o mapeamento da regra 31533.
    """

    project_root = Path(__file__).parent.parent

    alerts_file = (
        project_root / "examples" / "sample_alerts.json"
    )

    mapping_file = (
        project_root / "data" / "mitre_mapping.json"
    )

    alerts = load_alerts(str(alerts_file))
    mapping = load_mapping(str(mapping_file))

    enriched = enrich_alerts(alerts, mapping)

    alert = next(
        a for a in enriched
        if a["rule_id"] == "31533"
    )

    assert alert["mitre_id"] == "T1190"


def test_unknown_mapping():
    """
    Verifica regras sem mapeamento.
    """

    alerts = [
        {
            "rule_id": "99999",
            "description": "teste",
            "groups": [],
            "agent": "lab"
        }
    ]

    mapping = {}

    enriched = enrich_alerts(alerts, mapping)

    assert enriched[0]["mitre_id"] == "Unknown"
    assert enriched[0]["mitre_name"] == "Unknown"
    assert enriched[0]["tactic"] == "Unknown"
