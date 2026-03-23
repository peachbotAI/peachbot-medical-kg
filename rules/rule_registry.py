class RuleRegistry:
    """
    Collects and manages all rules before export.
    """

    def __init__(self):
        self._rules = []

    def register(self, rule):
        self._rules.append(rule)

    def get_all(self):
        return self._rules

    def to_core_json(self):
        return [rule.to_core_format() for rule in self._rules]