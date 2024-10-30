"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from typing import Tuple, List, Dict
from rxconfig import config


# The back end of the app that holds all of the data to be displayed/changed
class State(rx.State):
    """The app state."""
    title = "Hello World"
    categories: List[Dict[str,str]] = [{"name": "Mark", "desc": "YouTuber"}, {"name": "Wade", "desc": "And Friends"}, {"name": "Bob", "desc": "And Friends"}]

# returns a row with the category name, description, and a dialog
def disperseCategories(category: Dict[str, str]) -> rx.Component:
    return rx.table.row(
        rx.table.row_header_cell(category["name"]),
        rx.table.cell(category["desc"]),
        getDialog(),
    )

# returns a dialog with an open button, a description, and a close button
# Dialog is formatted in a row format
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
        justify="row", # <- this is what makes the format into a row
        
        # min_height="85vh",
    ), # end vstack

# The front end of the app that displays/renders the data
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
                    rx.foreach(State.categories, disperseCategories) # <- this foreach component calls disperseCategories
                                                                     # for each element in State.categories and then renders them
                ), # end table body
                width="100%",
            ), # end table root

            rx.color_mode.button(position="bottom-left"), # <- this is the color mode button to turn on and off dark mode
            
        ), # end flex
    ) # end container


app = rx.App() # Creates intance of the app
app.add_page(index) # Adds the index page to the app
