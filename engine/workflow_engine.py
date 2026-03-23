import yaml


def load_workflow_config():
    with open("configs/workflow.yaml", "r") as f:
        return yaml.safe_load(f)


def determine_routes(output, config):
    urgency = output["urgency"]

    for rule in config["triage_rules"].values():
        if rule["match"]["urgency"] == urgency:
            return rule["route_to"]

    return ["OPD"]  # fallback


def apply_workflow(safe_outputs):
    config = load_workflow_config()

    workflow_outputs = []

    for output in safe_outputs:

        urgency = output["urgency"]

        # 🔹 Determine facility routes
        routes = determine_routes(output, config)

        # 🔹 Priority mapping
        priority = config["priority_map"].get(urgency, "low")

        # 🔹 Collect next steps from facilities
        next_steps = []
        for r in routes:
            facility = config["facilities"].get(r, {})
            next_steps.extend(facility.get("next_steps", []))

        # 🔹 Monitoring plan
        monitoring = config["monitoring"].get(priority, [])

        workflow_outputs.append({
            **output,
            "routes": routes,
            "priority": priority,
            "next_steps": list(set(next_steps)),
            "monitoring_plan": monitoring
        })

    return workflow_outputs