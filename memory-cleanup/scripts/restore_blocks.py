"""Read memory block files and restore them to a running agent."""
import argparse
import glob
import os
import sys
import requests


def get_agent_name(server_url: str, agent_id: str) -> str:
    url = f"{server_url}/v1/agents/{agent_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["name"]


def read_blocks(input_dir: str, labels: list[str] | None = None) -> list[tuple[str, str]]:
    paths = glob.glob(os.path.join(input_dir, "*.txt"))
    result = []
    for p in paths:
        label = os.path.splitext(os.path.basename(p))[0]
        if labels and label not in labels:
            continue
        with open(p) as f:
            result.append((label, f.read()))
    return result


def patch_block(server_url: str, agent_id: str, label: str, value: str) -> None:
    url = f"{server_url}/v1/agents/{agent_id}/core-memory/blocks/{label}"
    response = requests.patch(url, json={"value": value})
    response.raise_for_status()


def restore(server_url: str, agent_id: str, input_dir: str, labels: list[str] | None = None) -> None:
    for label, value in read_blocks(input_dir, labels):
        patch_block(server_url, agent_id, label, value)
        print(f"Restored: {label}")


def main() -> None:
    agent_id = os.environ.get("AGENT_ID")
    if not agent_id:
        print("Error: AGENT_ID environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Restore agent memory blocks from files.")
    parser.add_argument("--server-url", default="http://localhost:8283")
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--labels", nargs="+", help="Only restore these labels (default: all)")
    args = parser.parse_args()

    agent_name = get_agent_name(args.server_url, agent_id)
    print(f"Restoring blocks for: {agent_name} ({agent_id})")

    restore(args.server_url, agent_id, args.input_dir, args.labels)


if __name__ == "__main__":
    main()
