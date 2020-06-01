from users import Users
from users import Admin
from users import Privileges

network_engineer = Admin('Ron','Swanson','rswanson','rswa123@mail.com')
network_engineer.show_privileges()
network_engineer.desc_user()