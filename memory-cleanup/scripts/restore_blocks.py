"""Read memory block files and restore them to a running agent."""
import argparse
import glob
import os
import requests


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
    parser = argparse.ArgumentParser(description="Restore agent memory blocks from files.")
    parser.add_argument("--server-url", default="http://localhost:8283")
    parser.add_argument("--agent-id", required=True)
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--labels", nargs="+", help="Only restore these labels (default: all)")
    args = parser.parse_args()
    restore(args.server_url, args.agent_id, args.input_dir, args.labels)


if __name__ == "__main__":
    main()
