"""
config.py
Handles reading and writing the plugin configuration (layer IDs and field names)
to/from a config.json file stored at the plugin root.
"""

import json
import os

_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

_DEFAULTS = {
    "troncon_layer_id": "",
    "troncon_field": "",
    "branchement_layer_id": "",
    "branchement_field": "",
}


def load_config():
    """Return the current config dict. Missing keys fall back to defaults."""
    if not os.path.exists(_CONFIG_PATH):
        return dict(_DEFAULTS)
    try:
        with open(_CONFIG_PATH, encoding="utf-8") as f:
            data = json.load(f)
        for k, v in _DEFAULTS.items():
            data.setdefault(k, v)
        return data
    except Exception:
        return dict(_DEFAULTS)


def save_config(cfg):
    """Persist the config dict to config.json."""
    with open(_CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
