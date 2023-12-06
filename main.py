import plotly.express as px 
import pandas as pd



data = pd.DataFrame(dict(keys=[10, 50, 20, 70], values=["Labour Cost", "Manufacturing Cost", "Promotion Cost", "Selling Cost"]))
figure = px.line_polar(data, r='keys', theta='values', line_close=True)
figure.update_traces(fill="toself")
figure.show()
