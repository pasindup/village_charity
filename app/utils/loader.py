import yaml
import importlib
from flask import jsonify

def load_routes_from_yaml(app, yaml_file):
    with open(yaml_file, "r") as f:
        routes_config = yaml.safe_load(f)

    for route in routes_config.get("routes", []):
        path = route["path"]
        method = route["method"]
        handler_str = route["handler"]

        module_name, func_name = handler_str.rsplit(".", 1)
        module = importlib.import_module(module_name)
        handler_func = getattr(module, func_name)

        app.add_url_rule(path, func_name, handler_func, methods=[method])
