"""Fetch all core memory blocks for an agent and write to files."""
import argparse
import os
import sys
import requests


def get_agent_name(server_url: str, agent_id: str) -> str:
    url = f"{server_url}/v1/agents/{agent_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["name"]


def fetch_blocks(server_url: str, agent_id: str) -> list[dict]:
    url = f"{server_url}/v1/agents/{agent_id}/core-memory/blocks"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def write_blocks(blocks: list[dict], output_dir: str, labels: list[str] | None = None) -> None:
    backup_dir = os.path.join(output_dir, "Backup")
    os.makedirs(backup_dir, exist_ok=True)
    for block in blocks:
        label, value = block["label"], block["value"]
        if labels and label not in labels:
            continue
        for target_dir in (output_dir, backup_dir):
            with open(os.path.join(target_dir, f"{label}.txt"), "w") as f:
                f.write(value)


def dump(server_url: str, agent_id: str, output_dir: str, labels: list[str] | None = None) -> None:
    blocks = fetch_blocks(server_url, agent_id)
    if labels:
        blocks = [b for b in blocks if b["label"] in labels]
    write_blocks(blocks, output_dir)
    print(f"Dumped {len(blocks)} blocks to {output_dir}")


def main() -> None:
    agent_id = os.environ.get("AGENT_ID")
    if not agent_id:
        print("Error: AGENT_ID environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Dump agent memory blocks to files.")
    parser.add_argument("--server-url", default="http://localhost:8283")
    parser.add_argument("--output-dir", default="./memory_dump")
    parser.add_argument("--labels", nargs="+", help="Only dump these labels (default: all)")
    args = parser.parse_args()

    agent_name = get_agent_name(args.server_url, agent_id)
    print(f"Dumping blocks for: {agent_name} ({agent_id})")

    dump(args.server_url, agent_id, args.output_dir, args.labels)


if __name__ == "__main__":
    main()
