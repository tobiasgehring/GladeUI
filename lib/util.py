"""
This module defines utility functions.
"""

def auto_bind(window, prefix='on', excludes=[]):
    """
    Function to automatically connect signals.

    Parameters
    ----------
    window : Gtk.Container
        the window where the magic shall happen
    prefix : str, default "on"
        name prefix of the event handler methods
    excludes : list
        list of methods names that should be excluded from auto connecting
    """
    for attr in dir(window):
        if ((attr not in excludes) and (attr.startswith(prefix))):
            value = getattr(window, attr)
            if (callable(value)):
                # parse callable's name
                parts = attr.split('_')
                if ((len(parts) < 3) or (parts[0] != prefix)):
                    continue
                widget_name = parts[1]
                event = "-".join(parts[2:]).lower()
                # is widget available?
                if (widget_name == 'self'):
                    widget = window
                else:
                    widget = getattr(window, widget_name)
                if (widget == None):
                    raise Exception("Widget %s not available." % widget_name)
                widget.connect(event, value)

