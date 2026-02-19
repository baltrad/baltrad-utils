# Copyright (C) 2023- Swedish Meteorological and Hydrological Institute (SMHI)
#
# This file is part of baltrad-utils.
#
# baltrad-utils is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# baltrad-utils is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with baltrad-utils.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

from importlib.metadata import distribution
from importlib.metadata import entry_points

def load_entry_point(distname, group, name):
    for entry_point in distribution(distname).entry_points:
        if group == entry_point.group and name == entry_point.name:
            return entry_point.load()
    raise ImportError("Cant load entry point")

def get_entry_map(group):
    entry_map = {}
    entries = entry_points()
    if isinstance(entries, dict):
        matches = entries.get(group, [])
    else:
        matches = entries.select(group=group)
    for m in matches:
        entry_map[m.name] = m.load()
    return entry_map
