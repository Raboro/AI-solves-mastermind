from ai_logic import *

class AiControl:
    
    def __init__(self, rule: str, colors: list[str], SECRET_COMBINATION: list[str]) -> None:
        self.RULE: str = rule
        self.COLORS: list[str] = colors
        self.SYMBOLS = BaseKnowledge.create_symbols_for_colors(self.COLORS)
        self.SECRET_COMBINATION = SECRET_COMBINATION
        self.knowledge: object = And()

    def main(self):
        self.create_base_knowledge()
        self.game_loop()

    def create_base_knowledge(self):
        self.knowledge = BaseKnowledge.choose_rule(self.RULE, self.COLORS, self.knowledge)
        print(self.knowledge)

    def game_loop(self):
        for round in range(12):
            
            if self.is_solved():
                return True

    def is_solved(self):
        result = []
        for symbol in self.SYMBOLS:
            if model_check(self.knowledge, symbol):
                result.append(symbol)
        
        if result == self.SECRET_COMBINATION:
            print("yes")
            return True


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
        knowledge = BaseKnowledge.each_color_has_a_position(colors, knowledge)
        knowledge = BaseKnowledge.one_color_per_position(colors, knowledge)
        knowledge = BaseKnowledge.one_position_per_color(colors, knowledge)
        knowledge = BaseKnowledge.every_color_once_combinations(colors, knowledge)
        return knowledge

    @staticmethod
    def rule_one_color(colors: list[str], knowledge: object) -> object:
        knowledge = BaseKnowledge.each_color_has_a_position(colors, knowledge)
        knowledge = BaseKnowledge.one_color_per_position(colors, knowledge)
        knowledge = BaseKnowledge.every_position_same_color(colors, knowledge)
        return knowledge

    @staticmethod
    def color_max_two_times(colors: list[str], knowledge: object) -> object:
        knowledge = BaseKnowledge.each_color_has_a_position(colors, knowledge)
        knowledge = BaseKnowledge.one_color_per_position(colors, knowledge)
        return knowledge

    @staticmethod
    def color_max_three_times(colors: list[str], knowledge: object) -> object:
        knowledge = BaseKnowledge.each_color_has_a_position(colors, knowledge)
        knowledge = BaseKnowledge.one_color_per_position(colors, knowledge)
        return knowledge

    @staticmethod
    def no_rules(colors: list[str], knowledge: object) -> object:
        knowledge = BaseKnowledge.each_color_has_a_position(colors, knowledge)
        knowledge = BaseKnowledge.one_color_per_position(colors, knowledge)
        return knowledge

    @staticmethod
    def each_color_has_a_position(colors: list[str], knowledge: object) -> object:
        """add for each color each position to the knowledge"""

        for color in colors:
            knowledge.add(Or(
                Symbol(f"{color}0"),
                Symbol(f"{color}1"),
                Symbol(f"{color}2"),
                Symbol(f"{color}3")
            ))
        return knowledge

    @staticmethod
    def one_color_per_position(colors: list[str], knowledge: object) -> object:
        """only one color per position"""

        for position in range(4):
            for color1 in colors:
                for color2 in colors:
                    if color1 != color2:
                        knowledge.add(Implication(
                            Symbol(f"{color1}{position}"), Not(Symbol(f"{color2}{position}"))
                        ))
        return knowledge

    @staticmethod
    def one_position_per_color(colors: list[str], knowledge: object) -> object:
        """each position has his own color"""
        
        for color in colors:
            for position1 in range(4):
                for position2 in range(4):
                    if position1 != position2:
                        knowledge.add(Implication(
                            Symbol(f"{color}{position1}"), Not(Symbol(f"{color}{position2}"))
                        ))
        return knowledge
    
    @staticmethod
    def every_position_same_color(colors: list[str], knowledge: object) -> object:
        """if one color is correct, this color is on every position"""

        for color in colors:
            for position1 in range(4):
                for position2 in range(4):
                    if position1 != position2:
                        knowledge.add(Implication(
                            Symbol(f"{color}{position1}"), Symbol(f"{color}{position2}")
                        ))
        return knowledge

    @staticmethod
    def every_color_once_combinations(colors: list[str], knowledge: object) -> object:
        pass