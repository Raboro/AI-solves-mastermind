from dataclasses import dataclass, field
import PySimpleGUI as sg


class Layout:

    @staticmethod
    def generate_layout() -> list:
        return [
            #  Rules
            [
                sg.Frame(
                    title="Rules",
                    title_location="n",
                    relief="raised",
                    border_width=4,
                    size=(900, 50),
                    layout=[
                        [
                            sg.Checkbox("Every color only one time in combination", pad=(10, 0), key="-RULEEVERYCOLORONE-"), 
                            sg.Checkbox("Only one color", pad=(10, 0), key="-RULEONLEYONECOLOR-"), 
                            sg.Checkbox("Color max two times in combo", pad=(10, 0), key="-RULECOLORMAXTWOTIMES-"), 
                            sg.Checkbox("Color max three times in combo", pad=(10, 0), key="-RULECOLORMAXTHREETIMES-")
                        ]
                    ]
                )
            ],

            #  Seperator
            [
                sg.HorizontalSeparator(pad=(0, 20))
            ],

            #  Colors
            [
                sg.Frame(
                    title="Colors",
                    title_location="n",
                    relief="raised",
                    border_width=4,
                    size=(900, 50),
                    layout=[
                        [
                            sg.Checkbox("Color white", pad=(15, 0), key="-COLORWHITE-"),
                            sg.Checkbox("Color red", pad=(15, 0), key="-COLORRED-"),
                            sg.Checkbox("Color green", pad=(15, 0), key="-COLORGREEN-"),
                            sg.Checkbox("Color yellow", pad=(15, 0), key="-COLORYELLOW-"),
                            sg.Checkbox("Color blue", pad=(15, 0), key="-COLORBLUE-"),
                            sg.Checkbox("Color pink", pad=(15, 0), key="-COLORPINK-"),
                            sg.Checkbox("Color orange", pad=(15, 0), key="-COLORORANGE-")
                        ]
                    ]
                ),
                
            ],
            
            #  Submit Rules and Colors
            [
                sg.Button(
                    "Submit rules and colors", 
                    key="-SUBMITRULESANDCOLORS-",
                    pad=((355, 355), (30,0)),
                    size=(25, 2)
                    )
            ],

            #  Seperator
            [
                sg.HorizontalSeparator(pad=(0, 20))
            ],

            

            #  Button Combination Input
            [
                sg.Button("", button_color="BLACK", size=(14, 8), disabled=True, pad=((80, 40), (0, 0)), key="-COMBINATION0-"),
                sg.Button("", button_color="BLACK", size=(14, 8), disabled=True, pad=((40, 40), (0, 0)), key="-COMBINATION1-"),
                sg.Button("", button_color="BLACK", size=(14, 8), disabled=True, pad=((40, 40), (0, 0)), key="-COMBINATION2-"),
                sg.Button("", button_color="BLACK", size=(14, 8), disabled=True, pad=((40, 40), (0, 0)), key="-COMBINATION3-")
            ],

            #  Submit
            [
                sg.Button(
                    "Submit", 
                    key="-SUBMIT-",
                    disabled=True,
                    pad=((355, 355), (50,0)),
                    size=(25, 2)
                    )
            ]
        ]

    
@dataclass(slots=True)
class GuiMastermind:

    layout: object = field(init=False)
    window: sg.Window = field(init=False)
    colors_buttons: list[str] = field(default_factory=list)


    def create_layout(self) -> None:
        self.layout = Layout.generate_layout()

    def create_window(self) -> None:
        self.window = sg.Window("AI solves mastermind", layout=self.layout, location=(550, 600))
        self.colors_buttons = ["BLACK", "BLACK", "BLACK", "BLACK"]

    def event_loop(self) -> None:
        while True:

            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == "-SUBMITRULESANDCOLORS-":
                RULES = []
                if any(value == True for value in values.values()):
                    RULES = [key for key, value in values.items() if value == True and key[1] == "R"]

                colors = [key for key, value in values.items() if value == True and key[1] == "C"]
                if colors == []:
                    raise Exception("no color")
                
                GuiLogic.update_window_for_input_combination(self.window)
                COLORS =  []
                colors = GuiLogic.get_colors_by_value_names(colors)
                COLORS.append("BLACK")
                for color in colors:
                    COLORS.append(color)

            if event in ["-COMBINATION0-", "-COMBINATION1-", "-COMBINATION2-", "-COMBINATION3-"]:
                button = [[btn, int(btn[-2])] for btn in ["-COMBINATION0-", "-COMBINATION1-", "-COMBINATION2-", "-COMBINATION3-"] if event == btn][0]
                self.colors_buttons = GuiLogic.change_button_color(button, self.window, self.colors_buttons, COLORS) 

            if event == "-SUBMIT-":
                SECRET_COMBINATION = self.colors_buttons             

        self.window.close()



class GuiLogic:

    @staticmethod
    def update_window_for_input_combination(window: sg.Window):
        window["-COMBINATION0-"].update(disabled=False)
        window["-COMBINATION1-"].update(disabled=False)
        window["-COMBINATION2-"].update(disabled=False)
        window["-COMBINATION3-"].update(disabled=False)
        window["-SUBMIT-"].update(disabled=False)

        window["-SUBMITRULESANDCOLORS-"].update(disabled=True)
        
    @staticmethod
    def get_colors_by_value_names(COLORS: list[str]):
        
        def color_switcher(color: str):
            color_switch = {
                "-COLORWHITE-": "WHITE",
                "-COLORBLACK-": "BLACK",
                "-COLORRED-": "RED",
                "-COLORGREEN-": "GREEN",
                "-COLORYELLOW-": "YELLOW",
                "-COLORBLUE-": "BLUE",
                "-COLORPINK-": "PINK",
                "-COLORORANGE-": "ORANGE"

            }

            return color_switch[color]

        return map(color_switcher, COLORS)

    @staticmethod
    def change_button_color(button, window: sg.Window, colors_button: list[str], COLORS: list[str]):
        for index, color in enumerate(COLORS):
            if color == colors_button[button[1]]:
                try:
                    colors_button[button[1]] = COLORS[index+1]
                except IndexError:
                    colors_button[button[1]] = "BLACK"
                break

        window[button[0]].update(button_color=colors_button[button[1]])

        return colors_button