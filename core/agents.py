class StrategyAgent:
    def evaluate(self, scores):
        return scores["stability"]


class RiskAgent:
    def evaluate(self, scores):
        return scores["risk"]


class SkepticAgent:
    def evaluate(self, scores):
        return scores["uncertainty"]


class GovernanceAgent:
    def evaluate(self, scores):
        return scores["compliance"]
