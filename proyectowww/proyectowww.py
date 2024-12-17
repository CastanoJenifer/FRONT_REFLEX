import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.fragment(
        rx.center(
            rx.vstack(
                    rx.heading(
                        "¡Bienvenid@ a tu gestor de lecturas! 📚", 
                        align="center",
                        font_size="4em", 
                        font_weight="bold",
                        color_scheme="gold",
                        background_color="rgba(255, 255, 255, 0.3)",
                        padding="25px", 
                        border_radius="15px",                         
                    ),
                rx.spacer(height="7rem"),
                rx.center(
                    rx.button(
                        "Empieza aquí",
                        color_scheme="gold",
                        size="4",
                        radius="medium",
                        #on_click="si",
                        style={"marginTop": "2rem"},
                        ),
                    spacing="5",
                    align_items="center",
                    justify_content="center",
                    width="100%",
                ),
            ),
            background_image="url('https://microteatro.es/wp-content/uploads/Portada-newsletter-microlab-15.png')",  # Ruta de la imagen
            background_size="cover",
            background_position="center",
            height="100vh",
        ),
)

app = rx.App()
app.add_page(index)   