from techpriestDatabaseImport1 import TP_Database, Database_Admin_Login, Database_Priviledges_Login

Admin = Database_Admin_Login("helios", "archmagos")
Admin.show_priviledges()

Moderator = Database_Priviledges_Login("helios", "archmagos")
Moderator.show_priviledges2()

Helios = TP_Database('helios', 'archmagos')
Helios.read_login_attempts()
Helios.increment_login_attempts(6)
Helios.read_login_attempts()
Helios.reset_login_attempts()
Helios.read_login_attempts()
Helios.increment_login_attempts(4)
Helios.read_login_attempts()

Helios = TP_Database('helios', 'archmagos')
Helios.describe_TP('Location: Uldan','Age: 1800', 'Role: Artisan')
Helios.greet_TP()