"""The main script of the project.

"""

from nation import Nation
from economy import Economy
from asset import Asset

France = Nation("French Republic", 4, 3, 5, Economy(67390000000,54000000))
France.menu()