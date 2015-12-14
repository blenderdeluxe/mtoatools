import os
from maya import mel, cmds
from PySide import QtGui
from functools import partial

this_package = os.path.abspath(os.path.dirname(__file__))
shelf_path = partial(os.path.join, this_package)

buttons = {
    'mattes': {
        'command': (
            'import mtoatools\n'
            'mtoatools.show_matte_aov_ui()'
        ),
        'sourceType': 'python',
        'style': 'iconOnly',
        'image': shelf_path('mtoatools_mattes.png'),
        'annotation': 'AOV Matte management',
        'enableCommandRepeat': False,
        'useAlpha': True,
        'flat': True,
        'enableBackground': False,
    }
}


def create_shelf():
    '''Create the mtoatools shelf'''

    tab_layout = mel.eval('$pytmp=$gShelfTopLevel')
    shelf_exists = cmds.shelfLayout('mtoatools', exists=True)

    if shelf_exists:
        cmds.deleteUI('mtoatools', layout=True)

    shelf = cmds.shelfLayout('mtoatools', parent=tab_layout)

    for button, kwargs in buttons.items():

        img = QtGui.QImage(kwargs['image'])
        kwargs['width'] = img.width()
        kwargs['height'] = img.height()

        cmds.shelfButton(label=button, parent=shelf, **kwargs)


create_shelf()