# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()


loan_status.plot(kind='bar')

# display plot
plt.show()


# --------------
#Code starts here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
#print(property_and_loan)
property_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.title('Bar Graph1')
plt.legend()
plt.show()



# --------------
#Code starts here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked='true',figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
#plt.xticks('45')
plt.show()




# --------------
#Code starts here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

graduate=data[data['Education'] == 'Graduate']
not_graduate=data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind='density',label='graduate')
not_graduate['LoanAmount'].plot(kind='density',label='not_graduate')

#Code ends here

#For automatic legend display
plt.legend()
plt.show()


# --------------
#Code starts here
import matplotlib.pyplot as plt
import numpy as np

fig, (ax_1,ax_2,ax_3) = plt.subplots(3)
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
plt.show()


