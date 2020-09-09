import pandas as pd

sal = pd.read_csv('Salaries.csv')

# Check the head of the DataFrame, check how many entries

sal.head()
sal.info()

# What is the average BasePay ?
sal['BasePay'].mean()
# What is the highest amount of OvertimePay in the dataset ?
sal['OvertimePay'].max()
# What is the job title of JOSEPH DRISCOLL ?
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
# How much does JOSEPH DRISCOLL make (including benefits)?
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
# What is the name of highest paid person (including benefits)?
sal[sal ['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']
# What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']
# What was the average (mean) BasePay of all employees per year? (2011-2014)?
sal.groupby('Year').mean()['BasePay']
# How many unique job titles are there?
sal['JobTitle'].nunique()
# What are the top 5 most common jobs?
sal['JobTitle'].value_counts().head(5)
# How many Job Titles were represented by only one person in 2013?
sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)
# How many people have the word Chief in their job title?
def chief_name(jobname):
    if 'chief' in jobname.lower():
        return True
    else:
        return False
sum(sal['JobTitle'].apply(lambda x: chief_name(x)))

# Bonus: Is there a correlation between length of the Job Title string and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['title_len', 'TotalPayBenefits']].corr()

