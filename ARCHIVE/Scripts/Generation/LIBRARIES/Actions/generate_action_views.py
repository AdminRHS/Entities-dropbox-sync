import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
MASTER_PATH = BASE_DIR / "Actions_Master.json"

COMMAND_OUT = BASE_DIR / "Actions_Master_Command_Verbs.json"
PROCESS_OUT = BASE_DIR / "Actions_Master_Process_Verbs.json"
RESULT_OUT = BASE_DIR / "Actions_Master_Result_Verbs.json"


def load_master():
    with MASTER_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_command_view(data: dict) -> dict:
    actions = data.get("actions", [])
    return {
        "entity_type": data.get("entity_type", "LIBRARIES"),
        "library": data.get("library", "Actions"),
        "source_file": MASTER_PATH.name,
        "view_type": "command_verbs",
        "total_actions": len(actions),
        "actions": [
            {
                "action_id": a.get("action_id"),
                "verb": a.get("action"),
            }
            for a in actions
        ],
    }


def build_process_view(data: dict) -> dict:
    actions = data.get("actions", [])
    items = []
    seen = set()

    for a in actions:
        action_id = a.get("action_id")
        base = a.get("action")
        forms = (a.get("forms") or {}).get("processes") or []
        for form in forms:
            key = (form, base)
            if key in seen:
                continue
            seen.add(key)
            items.append(
                {
                    "process": form,
                    "base_action": base,
                    "action_id": action_id,
                }
            )

    return {
        "entity_type": data.get("entity_type", "LIBRARIES"),
        "library": data.get("library", "Actions"),
        "source_file": MASTER_PATH.name,
        "view_type": "process_verbs",
        "total_items": len(items),
        "processes": items,
    }


def build_result_view(data: dict) -> dict:
    actions = data.get("actions", [])
    items = []
    seen = set()

    for a in actions:
        action_id = a.get("action_id")
        base = a.get("action")
        forms = (a.get("forms") or {}).get("results") or []
        for form in forms:
            key = (form, base)
            if key in seen:
                continue
            seen.add(key)
            items.append(
                {
                    "result": form,
                    "base_action": base,
                    "action_id": action_id,
                }
            )

    return {
        "entity_type": data.get("entity_type", "LIBRARIES"),
        "library": data.get("library", "Actions"),
        "source_file": MASTER_PATH.name,
        "view_type": "result_verbs",
        "total_items": len(items),
        "results": items,
    }


def main() -> None:
    data = load_master()

    command_view = build_command_view(data)
    process_view = build_process_view(data)
    result_view = build_result_view(data)

    COMMAND_OUT.write_text(json.dumps(command_view, indent=2, ensure_ascii=False), encoding="utf-8")
    PROCESS_OUT.write_text(json.dumps(process_view, indent=2, ensure_ascii=False), encoding="utf-8")
    RESULT_OUT.write_text(json.dumps(result_view, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Wrote {COMMAND_OUT}")
    print(f"Wrote {PROCESS_OUT}")
    print(f"Wrote {RESULT_OUT}")


if __name__ == "__main__":
    main()
