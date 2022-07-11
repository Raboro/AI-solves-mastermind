from ai_logic import *

class AiControl:
    
    def __init__(self, rule: str, colors: list[str]) -> None:
        self.RULE: str = rule
        self.COLORS: list[str] = colors
        self.SYMBOLS = BaseKnowledge.create_symbols_for_colors(self.COLORS)
        self.knowledge: object = And()

    def main(self):
        self.create_base_knowledge()


    def create_base_knowledge(self):
        self.knowledge = BaseKnowledge.choose_rule(self.RULE, self.COLORS, self.knowledge)
        print(self.knowledge)


class BaseKnowledge:
    
    @staticmethod
    def create_symbols_for_colors(colors: list[str]):
        """returns a list of symbols for all combinations of every color on each of the four positions"""
        return [Symbol(f"{color}{position}") for position in range(4) for color in colors]  

    @staticmethod
    def choose_rule(rule: str, colors: list[str], knowledge: object):
        rules: dict = {
            "-RULEEVERYCOLORONE-": BaseKnowledge.rule_every_color_once,
            "-RULEONLEYONECOLOR-": BaseKnowledge.rule_one_color,
            "-RULECOLORMAXTWOTIMES-": BaseKnowledge.color_max_two_times,
            "-RULECOLORMAXTHREETIMES-": BaseKnowledge.color_max_three_times,
            "": BaseKnowledge.no_rules
        }
        
        return rules[rule](colors, knowledge)

    @staticmethod
    def rule_every_color_once(colors: list[str], knowledge: object) -> object:
        knowledge.add(BaseKnowledge.each_color_has_a_position())
        return knowledge

    @staticmethod
    def rule_one_color(colors: list[str], knowledge: object) -> object:
        knowledge.add(BaseKnowledge.each_color_has_a_position())
        return knowledge

    @staticmethod
    def color_max_two_times(colors: list[str], knowledge: object) -> object:
        knowledge.add(BaseKnowledge.each_color_has_a_position())
        return knowledge

    @staticmethod
    def color_max_three_times(colors: list[str], knowledge: object) -> object:
        knowledge = (BaseKnowledge.each_color_has_a_position(colors, knowledge))
        return knowledge

    @staticmethod
    def no_rules(colors: list[str], knowledge: object) -> object:
        knowledge = (BaseKnowledge.each_color_has_a_position(colors, knowledge))
        return knowledge

    @staticmethod
    def each_color_has_a_position(colors: list[str], knowledge: object) -> object:
        for color in colors:
            knowledge.add(Or(
                Symbol(f"{color}0"),
                Symbol(f"{color}1"),
                Symbol(f"{color}2"),
                Symbol(f"{color}3")
            ))
        return knowledge