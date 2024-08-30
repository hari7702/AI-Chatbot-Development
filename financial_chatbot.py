
import pandas as pd

# Sample data loaded from your CSV
df = pd.read_csv('financial_data_analysis.csv')

# Preprocessing to structure the data for easy access
df_pivot = df.pivot(index='Company', columns='Metric', values=['Year 0', 'Year 1', 'Year 2'])
df_pivot.columns = ['_'.join(col).strip() for col in df_pivot.columns.values]

# Define the simple chatbot function
def simple_chatbot(user_query):
    if user_query == "What is the total revenue for Company A in Year 2?":
        return f"The total revenue for Company A in Year 2 is {df_pivot.loc['Company A', 'Year 2_Operating revenue']}."
    elif user_query == "How has net income changed for Company B from Year 1 to Year 2?":
        net_income_change = (df_pivot.loc['Company B', 'Year 2_EBITDA'] - df_pivot.loc['Company B', 'Year 1_EBITDA']) / df_pivot.loc['Company B', 'Year 1_EBITDA'] * 100
        return f"The net income for Company B has changed by {net_income_change:.3f}% from Year 1 to Year 2."
    elif user_query == "What is the total revenue for Company X in Year 1?":
        return f"The total revenue for Company X in Year 1 is {df_pivot.loc['Company X', 'Year 1_Operating revenue']}."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Example of interaction
if __name__ == "__main__":
    print(simple_chatbot("What is the total revenue for Company A in Year 2?"))
    print(simple_chatbot("How has net income changed for Company B from Year 1 to Year 2?"))
    print(simple_chatbot("What is the total revenue for Company X in Year 1?"))
