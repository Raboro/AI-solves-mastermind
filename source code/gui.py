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
                            sg.Checkbox("Color white", pad=(10, 0), key="-COLORWHITE-"),
                            sg.Checkbox("Color black", pad=(10, 0), key="-COLORBLACK-"),
                            sg.Checkbox("Color red", pad=(10, 0), key="-COLORRED-"),
                            sg.Checkbox("Color green", pad=(10, 0), key="-COLORGREEN-"),
                            sg.Checkbox("Color yellow", pad=(10, 0), key="-COLORYELLOW-"),
                            sg.Checkbox("Color blue", pad=(10, 0), key="-COLORBLUE-"),
                            sg.Checkbox("Color lila", pad=(10, 0), key="-COLORLILA-"),
                            sg.Checkbox("Color orange", pad=(10, 0), key="-COLORORANGE-")
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
                sg.Button("", button_color="BLACK", size=(14, 8), disabled=True, pad=((80, 40), (0, 0))),
                sg.Button("", button_color="BLACK", size=(14, 8), disabled=True, pad=((40, 40), (0, 0))),
                sg.Button("", button_color="BLACK", size=(14, 8), disabled=True, pad=((40, 40), (0, 0))),
                sg.Button("", button_color="BLACK", size=(14, 8), disabled=True, pad=((40, 40), (0, 0)))
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


    def create_layout(self) -> None:
        self.layout = Layout.generate_layout()

    def create_window(self) -> None:
        self.window = sg.Window("AI solves mastermind", layout=self.layout, location=(550, 600))

    def event_loop(self) -> None:
        while True:

            event, values = self.window.read()
            print(event)

            if event == sg.WINDOW_CLOSED:
                break

        self.window.close()