"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    title = "Hello World"


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.flex(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.cell("Name"),
                        rx.table.cell("Description"),
                        rx.table.cell("Parent"),
                    ), # end row
                ), # end header
                rx.table.body(
                    rx.table.row(
                        rx.table.row_header_cell("Mr. Yeet"),
                        rx.table.cell("Bruh"),
                        rx.table.cell(
                            rx.vstack(
                                rx.dialog.root(
                                    rx.dialog.trigger(
                                        rx.button("Open Dialog")
                                    ),
                                    rx.dialog.content(
                                        rx.dialog.title(State.title),
                                        rx.dialog.description("This is a dialog lmao"),
                                        rx.dialog.close(
                                            rx.button("Close Dialog", size="3"),
                                        ),
                                    ),
                                    

                                ),
                                spacing="5",
                                justify="row",
                                min_height="85vh",
                            ), # end vstack
                        ),
                    ),
                ), # end table body
                width="100%",
            ), # end table root

            rx.color_mode.button(position="bottom-left"),
            
        ), # end flex
    ) # end container


app = rx.App()
app.add_page(index)
