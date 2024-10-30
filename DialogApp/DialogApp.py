"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from typing import Tuple, List, Dict
from rxconfig import config


class State(rx.State):
    """The app state."""
    title = "Hello World"
    categories: List[Dict[str,str]] = [{"name": "Mark", "desc": "YouTuber"}, {"name": "Wade", "desc": "And Friends"}]

    # @staticmethod
def disperseCategories(category: Dict[str, str]) -> rx.Component:
    return rx.table.row(
        rx.table.row_header_cell(category["name"]),
        rx.table.cell(category["desc"]),
        getDialog(),
    )

def getDialog() -> rx.Component:
    return rx.vstack(
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
        # min_height="85vh",
    ), # end vstack



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
                    # rx.table.row(
                    #     rx.table.row_header_cell("Mr. Yeet"),
                    #     rx.table.cell("Bruh"),
                        
                        
                    # ),
                    # rx.foreach(State.categories, lambda category: State.disperseCategories(category)),
                    rx.foreach(State.categories, disperseCategories)
                ), # end table body
                width="100%",
            ), # end table root

            rx.color_mode.button(position="bottom-left"),
            
        ), # end flex
    ) # end container


app = rx.App()
app.add_page(index)
