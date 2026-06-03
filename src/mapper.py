"""
mapper.py

Módulo responsável por associar alertas do Wazuh
às técnicas MITRE ATT&CK definidas no arquivo
data/mitre_mapping.json.

Compatível com Python 3.11+
"""

import json
from pathlib import Path

from parser import load_alerts


def load_mapping(mapping_file: str) -> dict:
    """
    Carrega o arquivo de mapeamento MITRE ATT&CK.

    Args:
        mapping_file (str): Caminho para o arquivo JSON.

    Returns:
        dict: Dicionário contendo os mapeamentos.
    """

    with open(mapping_file, "r", encoding="utf-8") as file:
        mapping = json.load(file)

    if not isinstance(mapping, dict):
        raise ValueError(
            "O arquivo de mapeamento deve conter um objeto JSON."
        )

    return mapping


def enrich_alerts(alerts: list[dict], mapping: dict) -> list[dict]:
    """
    Enriquece os alertas com informações MITRE ATT&CK.

    Args:
        alerts (list): Lista de alertas processados.
        mapping (dict): Dicionário de mapeamentos MITRE.

    Returns:
        list[dict]: Lista enriquecida.
    """

    enriched_alerts = []

    for alert in alerts:
        rule_id = str(alert.get("rule_id"))

        mitre_info = mapping.get(
            rule_id,
            {
                "mitre_id": "Unknown",
                "mitre_name": "Unknown",
                "tactic": "Unknown"
            }
        )

        enriched_alert = {
            **alert,
            "mitre_id": mitre_info.get("mitre_id", "Unknown"),
            "mitre_name": mitre_info.get("mitre_name", "Unknown"),
            "tactic": mitre_info.get("tactic", "Unknown")
        }

        enriched_alerts.append(enriched_alert)

    return enriched_alerts


def main():
    """
    Executa o mapeamento para testes.
    """

    project_root = Path(__file__).parent.parent

    alerts_file = (
        project_root / "examples" / "sample_alerts.json"
    )

    mapping_file = (
        project_root / "data" / "mitre_mapping.json"
    )

    try:
        alerts = load_alerts(str(alerts_file))

        mapping = load_mapping(str(mapping_file))

        enriched_alerts = enrich_alerts(
            alerts,
            mapping
        )

        print("\n=== ALERTAS ENRIQUECIDOS ===\n")

        for alert in enriched_alerts:
            print(alert)

        print(
            f"\nTotal de alertas enriquecidos: "
            f"{len(enriched_alerts)}"
        )

    except FileNotFoundError as e:
        print(f"Arquivo não encontrado: {e}")

    except json.JSONDecodeError as e:
        print(f"JSON inválido: {e}")

    except ValueError as e:
        print(f"Erro de validação: {e}")

    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
