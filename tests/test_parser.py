from pathlib import Path

from src.parser import load_alerts


def test_load_alerts_returns_list():
    """
    Verifica se o parser retorna uma lista.
    """

    project_root = Path(__file__).parent.parent
    sample_file = project_root / "examples" / "sample_alerts.json"

    alerts = load_alerts(str(sample_file))

    assert isinstance(alerts, list)


def test_load_alerts_count():
    """
    Verifica se foram carregados 5 alertas.
    """

    project_root = Path(__file__).parent.parent
    sample_file = project_root / "examples" / "sample_alerts.json"

    alerts = load_alerts(str(sample_file))

    assert len(alerts) == 5


def test_alert_structure():
    """
    Verifica se o primeiro alerta possui os campos esperados.
    """

    project_root = Path(__file__).parent.parent
    sample_file = project_root / "examples" / "sample_alerts.json"

    alerts = load_alerts(str(sample_file))

    first_alert = alerts[0]

    assert "rule_id" in first_alert
    assert "description" in first_alert
    assert "groups" in first_alert
    assert "agent" in first_alert
