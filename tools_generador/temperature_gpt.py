import reflex as rx

class SliderTemperature(rx.State):
    temperature: float=0.5
    
    def set_end(self, value: list[float]):
        self.temperature=value[0]
        
    def procesando_datos(self):
        print(f"Slieder temperature: {self.temperature}")        
        
def slider_intro():
    return rx.vstack(
        rx.heading("Selector de temperatura"),
        rx.slider(on_value_commit=SliderTemperature.set_end,
                custom_attrs={"step":0.1},
                min=0,
                max=1),
        width="100%"
    )