from ._anvil_designer import LuoKayttaja_KirjauduTemplate
from anvil import *


class LuoKayttaja_Kirjaudu(LuoKayttaja_KirjauduTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
