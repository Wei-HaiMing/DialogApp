"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from typing import Tuple, List, Dict
from rxconfig import config


# The back end of the app that holds all of the data to be displayed/changed
class State(rx.State):
    """The app state."""
    title = "Hello World"
    categories: List[Dict[str, str]] = [{"name": "Mark", "desc": "YouTuber", "id": "23462364", "parent": ""}, {"name": "Wade", "desc": "And Friends", "id": "23454", "parent": ""}, {"name": "Bob", "desc": "And Friends", "id": "6532", "parent": ""}]
    parent_categories: List[str] = ["Utilities", "Automobile", "Rent"]
    dialog_open: bool = False
    select_val = "Utilities"

    # STILL A WORK IN PROGRESS TO ACTUALLY CHANGE THE PARENT CATEGORY DISPLAY
    def change_select_value(self, value: str):
        self.select_val = value

    # handles the submit for the form for the name, description, and id of the category and displays the changes accordingly
    def handle_submit(self, data: Dict[str, str]):
        """
        This functions works based on the premise that the key values of dictionary data are corresponding to
        some dictionary value in self.categories. It loops through all of the categories present to find a match 
        of the data dictionary to the self.categories[n] dictionary where n is an integer 0 <= n <= len(self.categories) - 1.
        Once a match is found, that category index is saved and then looped through to compare with values to be changed
        based on if the values in data does not equal to the format of empty_{val} where val is the literal string of the 
        value of the chosen category. The purpose of this format is to ensure that unique changes are able to be made as other 
        form submissions can apply to other categories. The change is then made. If there is no change and the submit button is 
        simply pressed, then no change is made. 
        """
        # print(category1)
        # print(data)
        index = -1 # variable to determine the index of the selected category to edit
        
        for i in range(len(self.categories)): # loop to actually compare changed data to categories
            cat_name = self.categories[i]["name"] # takes the name of the category's name value
            cat_desc = self.categories[i]["desc"] # etc. etc.
            cat_id = self.categories[i]["id"]
            data_name = "" 
            data_desc = ""
            data_id = ""
            # print(cat_name, cat_desc, cat_id)

            # checking to see if the category value is in the data dictionary before assigning values
            if cat_name in data: 
                if data[cat_name] == "": # assigns empty values to the empty_{val} format for checking
                    data[cat_name] = f"empty_{cat_name}"
                    data_name = getKey(data, data[cat_name])
                else:
                    data_name = getKey(data, data[cat_name])
                    
            # etc. etc.
            if cat_desc in data:
                if data[cat_desc] == "":
                    data[cat_desc] = f"empty_{cat_desc}"
                    data_desc = getKey(data, data[cat_desc])
                else:
                    data_desc = getKey(data, data[cat_desc])
                    
            if cat_id in data:
                if data[cat_id] == "":
                    data[cat_id] = f"empty_{cat_id}"
                    data_id = getKey(data, data[cat_id])
                else:
                    data_id = getKey(data, data[cat_id])

            # print(self.categories[i]["name"], self.categories[i]["desc"], self.categories[i]["id"])
            # print(data_name, data_desc, data_id)

            # final check of each key pair value of data to compare against category
            if self.categories[i]["name"] == data_name and self.categories[i]["desc"] == data_desc and self.categories[i]["id"] == data_id:
                print(self.categories[i]["name"], self.categories[i]["desc"], self.categories[i]["id"])
                print(data_name, data_desc, data_id)
                index = i
                break
        
        # assigns corresponding category
        category = self.categories[index]
        
        # print(data)
        # print(category)
        # assigns values to be changed to actual self.categories
        for key, val in category.items():
            if not key == "parent":
                if not data[val] == f"empty_{val}":
                    category[key] = data[val]
                

def getKey(my_dict: Dict[str, str], val: str) -> str:
    # Code taken from Geeks for Geeks' way of retrieving dictionary keys

    for key, value in my_dict.items():
        if val == value:
            return key

    return "Key not found"



# returns a row with the category name, description, and a dialog
def disperseCategories(category: Dict[str, str]) -> rx.Component:
    return rx.table.row(
        rx.table.row_header_cell(category["name"]),
        rx.table.cell(category["desc"]),
        rx.table.cell(category["parent"]),
        rx.vstack(
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(rx.icon("ellipsis-vertical"))
                ),
                rx.dialog.content(
                    rx.dialog.title("Edit Category"),
                    rx.vstack(
                        rx.form( # start of the form for each dialog, they are unique dialogs for each category
                            rx.vstack(
                                rx.text("Edit the category's info"),

                                rx.text("Name"),
                                rx.input(
                                    placeholder = category["name"],
                                    name = category["name"],
                                ),
                                rx.text("Description"),
                                rx.input(
                                    placeholder = category["desc"],
                                    name = category["desc"],
                                ),
                                rx.text("id"),
                                rx.input(
                                    placeholder = category["id"],
                                    name = category["id"],
                                ),

                                rx.text("Select Parent Category"),
                                rx.select(
                                    State.parent_categories,
                                    value = State.select_val,
                                    on_change = State.change_select_value,
                                ),
                                rx.badge(State.select_val),
                                rx.button("Submit", type="submit"),
                            ),
                            on_submit = State.handle_submit, 
                            reset_on_submit = False,
                        ),
                        # rx.divider(),
                        # rx.text(State.categories.to_string())
                    ),
                    rx.dialog.close(
                        rx.button("Close Dialog", size="3"),
                    ),
                ),
            ),
            spacing="10",
            justify="row", # <- this is what makes the format into a row
            # min_height="85vh",
        ), # end vstack
    )

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


