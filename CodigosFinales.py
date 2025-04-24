#Juan Pablo
import plotly.express as px
df = px.data.iris()
colors = ['#56B4E9', '#E69F00', '#000000']  # Colores accesibles
fig = px.scatter(df, x="petal_width", y="petal_length", color="species",
                 size='sepal_length', hover_data=['sepal_width'], color_discrete_sequence=colors)
fig.update_layout(
    xaxis_title="petal width (cm)",
    yaxis_title="petal length (cm)"
)


fig.show()

#Renato

colors = ['#FF5843', '#000000', '#3357FF']
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'], color_discrete_sequence= colors)
fig.show()

#Andres

df = px.data.iris()
colors = [ '#E15E26', '#C3F4BF', '#E036A5', '#11AFF4', '#B4ED15']

fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species",
                 size='petal_length', hover_data=['species_id'],color_discrete_sequence= colors)

fig.update_traces(marker=dict(line=dict(color='black', width=1.5)))
fig.show()
