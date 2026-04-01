from ._anvil_designer import karttanakymaTemplate
from anvil import *

class karttanakyma(karttanakymaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.map.center = GoogleMap.LatLng(61.055441, 28.1889914) # Lappeenrannan keskusta
    marker = GoogleMap.Marker(
      animation=GoogleMap.Animation.DROP,
      position=GoogleMap.LatLng(61.0664555, 28.090938)
    )
    marker.add_event_handler("click", marker_click)
    self.map.add_component(marker) # Lisää merkin Lutin parkkipaikalle
    # Kartan dokumentaatio:
    # https://anvil.works/docs/components/standard-components/maps

    # Any code you write here will run before the form opens.

  @handle("map", "bounds_changed")
  def map_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""
    pass

def marker_click(sender, **event_args):
  i =GoogleMap.InfoWindow(content=Label(text="Esimerkkikatu tai jtn"))
  i.open(map, sender)
