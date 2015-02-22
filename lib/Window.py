"""
This module provides the glade gui helper classes for windows (Gtk.Window)
"""

from gi.repository import Gtk
import util

class Window(Gtk.Window):
    """
    Helper base class for Gtk.Window glade GUI definitions.
    
    Parameters
    ----------
    glade_filename : str
        File name of glade file
    title : str, optional
        Window title

    Usage
    -----

    class MainWindow(GladeWindow.Window.Window):
        def __init__(self):
            GladeWindow.Window.__init__(self, "MainWindow.glade")
            # you have direct access to the widgets defined in the 
            # glade file
            self.buttonMyButton.set_label("My button")
            #
            self.show_all()

        def on_buttonMyButton_clicked(self, data):
            # this method is automatically connected to the clicked event of
            # self.buttonMyButton
            print("click on buttonMyButton")
    """

    def __init__(self, glade_filename, title=""):
        """
        Constructor. All the magic happens here.

        Parameters
        ----------
        glade_filename : str
            File name of glade file
        title : str, optional
            Window title
        """
        Gtk.Window.__init__(self, title=title)

        self._builder = Gtk.Builder()
        self._builder.add_from_file(glade_filename)
        window_id = type(self).__name__
        window = self._builder.get_object(window_id)
        if (window is None):
            raise Exception("Did not find any object with id '%s'." % window_id)
        if (not isinstance(window, Gtk.Container)):
            raise Exception("Object with id '%s' is not a subclass of Gtk.Container." % window_id)
        # reparent all children
        window.foreach(lambda x: x.reparent(self))
        # copy window properties
        for prop in window.props:
            name = prop.name.replace('-', '_')
            # TODO: are these all properties we want to exclude???
            if (name not in ['parent', 'window', 'child', 'type', 'type_hint']):
                try:
                    self.set_property(name, window.get_property(name))
                except:
                    # ignore read-only properties
                    pass
        # add children objects as attributes
        # TODO: if there are two windows in a glade file this adds to much
        for widget in self._builder.get_objects():
            id = Gtk.Buildable.get_name(widget)
            if (id != window_id):
                setattr(self, id, widget)
        # auto connect events
        util.auto_bind(self)
        
        #self._builder.connect_signals(self)
        self.show_all()
