letter= '''

Letter format
Dear [Candidate Name],
 
We are pleased to offer you the [full-time, part-time, etc.] position of [job title] at [Company Name] with a start date of [start date], You will be reporting directly to [manager/supervisor name] at [workplace location]. We believe your skills and experience are an excellent match for our company.
 
The annual starting salary for this position is [dollar amount] to be paid on a monthly basis by deposit, starting on first pay period.
 
Your employment with [Company Name] will be on an at-will basis, which means you and the company are free to terminate the employment relationship at any time for any reason. This letter is not a contract or guarantee of employment for a definitive period of time.
 
As an employee of [Company Name], you are also eligible for our benefits program, which includes medical insurance, 50(k), vacation time, etc, and other benefits which will be described in more detail in the employee handbook, orientation package, etc.
 
Please confirm your acceptance of this offer by signing and returning this letter by [offer expiration date].
 
We are excited to have you join our team! If you have any questions, please feel free to reach out at any time.

Have a Good Day!
Thanks....
Sincerely,
[HR Name]
[current date]


'''
# name of the selected candidate......
client_name=input("Enter name of succeful candinate name Here:\n ")
# job duration means of weather this job is for half_time full_time or something else.......
job_duration=input("job duration write here for employee:\n ")
# job tite means which job you are giving to selected candidte.....................
job_title=input("write the job title for successful candidate:\n ")
# here we have the name of your company that will be contant in every place.........
company_name=input("Write company name here:\n ")
# strat date is a date on which your selected employee will start his/her work..........
start_date=input("starting date for the work:\n ")
# report to means to whom successfull candiate will report............................
report_to=input("write the name of person to whom cadidate will report:\n ")
# loaction here referce the block or room of your reporting area.....................
location_of_reportor=input("write the location of person whom to be reporting:\n ")
# salary which you will provide to your selected candidate...........................
salary_per_month=input("write the amount of salary:\n ")
# name of your company CEO..........................................................
hr_name=input("write the name of your CEO:\n ")
# write expiray date here............................
expire_date=input("write expiration date her :\n ")
# HERE WE WILL WRITE DESIGNATION OF YOUR OWNER OF THE COMPANY AS HE IS CEO...................
# we we will write current date for your letter.....................................
current_date=input("write the current date:\n ")
letter=letter.replace("[Candidate Name]",client_name)
letter=letter.replace("[full-time, part-time, etc.]",job_duration)
letter=letter.replace("[job title]",job_title)
letter=letter.replace("[Company Name]",company_name)
letter=letter.replace("[start date]",start_date)
letter=letter.replace("[manager/supervisor name]",report_to)
letter=letter.replace("[workplace location]",location_of_reportor)
letter=letter.replace("[dollar amount]",salary_per_month)
letter=letter.replace("[HR Name]",hr_name)
letter=letter.replace("[offer expiration date]",expire_date)
letter=letter.replace("[current date]",current_date)
print(letter)