import reflex as rx

class SliderMaxTokens(rx.State):
    slider: int= 750
    
    def set_end(self, value: list[int]):
        self.slider=value[0]
        
    def procesado_datos(self):
        print(f"Slider: {self.slider}")
        
def slider_max_token():
    return rx.vstack(
        rx.heading("Selector de tokens"),
        rx.heading("Selector de tokens aproximados para usar"),
        rx.slider(on_value_commit=SliderMaxTokens.set_end),
        width="100%"
    )