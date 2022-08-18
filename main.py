"""The main script of the project.

"""

from tempfile import tempdir
from nation import Nation
from economy import Economy
from asset import Asset
from assetstore import AssetStore


list_nation = []
the_store = AssetStore(list_nation)

France = Nation("French Republic", 4, 3, 5, Economy(67390000000,54000000),the_store)
list_nation.append(France)

France.menu()

