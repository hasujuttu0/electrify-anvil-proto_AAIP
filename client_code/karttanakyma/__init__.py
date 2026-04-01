from ._anvil_designer import karttanakymaTemplate
from anvil import *

class karttanakyma(karttanakymaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("map", "bounds_changed")
  def map_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""
    pass
