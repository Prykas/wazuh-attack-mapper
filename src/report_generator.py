"""
report_generator.py

Módulo responsável por gerar relatórios CSV contendo
alertas enriquecidos com informações MITRE ATT&CK.

Compatível com Python 3.11+
"""

import csv
from pathlib import Path

try:
    from mapper import enrich_alerts, load_mapping
    from parser import load_alerts
except ImportError:
    from src.mapper import enrich_alerts, load_mapping
    from src.parser import load_alerts


def generate_csv(alerts: list[dict], output_file: str) -> None:
    """
    Gera um relatório CSV a partir dos alertas enriquecidos.

    Args:
        alerts (list[dict]): Lista de alertas enriquecidos.
        output_file (str): Caminho do arquivo CSV.
    """

    fieldnames = [
        "rule_id",
        "description",
        "agent",
        "mitre_id",
        "mitre_name",
        "tactic",
    ]

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for alert in alerts:
            writer.writerow(
                {
                    "rule_id": alert.get("rule_id"),
                    "description": alert.get("description"),
                    "agent": alert.get("agent"),
                    "mitre_id": alert.get("mitre_id"),
                    "mitre_name": alert.get("mitre_name"),
                    "tactic": alert.get("tactic"),
                }
            )


def main():
    """
    Executa a geração do relatório CSV.
    """

    project_root = Path(__file__).parent.parent

    alerts_file = (
        project_root / "examples" / "sample_alerts.json"
    )

    mapping_file = (
        project_root / "data" / "mitre_mapping.json"
    )

    reports_dir = (
        project_root / "reports"
    )

    output_file = (
        reports_dir / "mitre_report.csv"
    )

    try:

        # Cria a pasta reports caso não exista
        reports_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        alerts = load_alerts(
            str(alerts_file)
        )

        mapping = load_mapping(
            str(mapping_file)
        )

        enriched_alerts = enrich_alerts(
            alerts,
            mapping
        )

        generate_csv(
            enriched_alerts,
            str(output_file)
        )

        print(
            "\nRelatório CSV gerado com sucesso!"
        )

        print(
            f"Arquivo: {output_file}"
        )

        print(
            f"Total de alertas exportados: "
            f"{len(enriched_alerts)}"
        )

    except FileNotFoundError as e:
        print(
            f"Arquivo não encontrado: {e}"
        )

    except PermissionError as e:
        print(
            f"Erro de permissão: {e}"
        )

    except Exception as e:
        print(
            f"Erro inesperado: {e}"
        )


if __name__ == "__main__":
    main()
