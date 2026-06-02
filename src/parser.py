"""
parser.py

Módulo responsável por ler alertas do Wazuh em formato JSON
e extrair informações relevantes para o projeto Wazuh ATT&CK Mapper.

Compatível com Python 3.11+
"""

import json
from pathlib import Path


def load_alerts(file_path: str) -> list[dict]:
    """
    Lê um arquivo JSON contendo alertas do Wazuh.

    Args:
        file_path (str): Caminho para o arquivo JSON.

    Returns:
        list[dict]: Lista de alertas processados.

    Raises:
        FileNotFoundError: Se o arquivo não existir.
        json.JSONDecodeError: Se o JSON for inválido.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        alerts = json.load(file)

    parsed_alerts = []

    for alert in alerts:
        parsed_alerts.append(
            {
                "rule_id": alert.get("rule", {}).get("id"),
                "description": alert.get("rule", {}).get("description"),
                "groups": alert.get("rule", {}).get("groups", []),
                "agent": alert.get("agent", {}).get("name"),
            }
        )

    return parsed_alerts


def main():
    """
    Executa o parser diretamente para testes.
    """

    project_root = Path(__file__).parent.parent
    sample_file = project_root / "examples" / "sample_alerts.json"

    try:
        alerts = load_alerts(str(sample_file))

        print("\n=== ALERTAS PROCESSADOS ===\n")

        for alert in alerts:
            print(alert)

        print(f"\nTotal de alertas processados: {len(alerts)}")

    except FileNotFoundError:
        print(f"Erro: arquivo não encontrado: {sample_file}")

    except json.JSONDecodeError as e:
        print(f"Erro: JSON inválido. Detalhes: {e}")

    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
