"""The main script of the project.

"""

from nation import Nation
from economy import Economy
from asset import Asset
from assetstore import AssetStore


#France = Nation("French Republic", 4, 3, 5, Economy(67390000000,54000000))
#France.menu()
TempCountry = Nation("Temp", 1, 1, 1 ,Economy(0,0))

AssetStore(TempCountry)