def auto_bind(window, prefix='on', excludes=[]):
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

