from ._anvil_designer import Valitse_pistokepaikkaTemplate
from anvil import *
import plotly.graph_objects as go


class Valitse_pistokepaikka(Valitse_pistokepaikkaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("peruuta_btn", "click")
  def peruuta_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass


