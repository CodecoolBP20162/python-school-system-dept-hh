from administrator import AdministratorData
from prettytable import PrettyTable

table=PrettyTable(None,None)
data=AdministratorData()

data.applicants_personal_data()
table=PrettyTable(data.results,data.tags)
table.draw_table()

print("\n")

data.applicants_by_status("new")
table=PrettyTable(data.results,data.tags)
table.draw_table()

print("\n")

data.applicants_by_interview("2017-05-18")
table=PrettyTable(data.results,data.tags)
table.draw_table()

print("\n")

data.applicants_by_location("Budapest")
table=PrettyTable(data.results,data.tags)
table.draw_table()

print("\n")

data.applicants_by_city("Budapest")
table=PrettyTable(data.results,data.tags)
table.draw_table()

print("\n")

data.applicants_by_mentor("Besenyei Judit")
table=PrettyTable(data.results,data.tags)
table.draw_table()

print("\n")

data.applicant_email_by_applicant_code("3QBa9s")
table=PrettyTable(data.results,data.tags)
table.draw_table()

print("\n")