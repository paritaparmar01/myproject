import matplotlib.pyplot as plt

def generate_line_chart(df, I_company, Premium, Insurance_Compuny, Premimum, premium_by_Insurance_Compny):
    plt.plot(df['I_company'], df['Premium'])
    plt.xlabel('Insurance Compuny')  # Label for x-axis
    plt.ylabel('Premimum')  # Label for y-axis
    plt.title('premium by Insurance Compny')  # Title of the chart
    plt.show()