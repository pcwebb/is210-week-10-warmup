#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Use update to  merge dictionaries."""

import data

data.BANDS.update({
    'Buckingham Nicks': {
        'Lindsey Buckingham': ['guitar', 'vocals'],
        'Stevie Nicks': ['vocals', 'tambourine'],
        }
    })
data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])