# Import libraries
# Import figure from bokeh.plotting
from bokeh.plotting import figure
# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Basic circle plot
plot = figure(plot_width=400, tools='pan,box_zoom')
plot.circle([1,2,3,4,5], [8,6,5,2,3])
output_file('circle.html')
show(plot)

# Female literacy (y) versus fertility (x)
# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(x=fertility_latinamerica, y=female_literacy_latinamerica, color='blue', size=10, alpha=0.8)

# Add an x glyph to the figure p
p.x(x=fertility_africa, y=female_literacy_africa, color='red', size=10, alpha=0.8)

# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

# Display the plot
show(p)

# Time series plot: price (x) vs. time (y)
# Create a figure with x_axis_type='datetime': p
p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')

# Plot date along the x-axis and price along the y-axis
p.line(x=date, y=price)

# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p.circle(x=date, y=price, fill_color='white', size=4)

# Specify the name of the output file and show the result
output_file('line.html')
show(p)

# Plot states
# Create a list of az_lons, co_lons, nm_lons and ut_lons: x
x = [az_lons, co_lons, nm_lons, ut_lons]

# Create a list of az_lats, co_lats, nm_lats and ut_lats: y
y = [az_lats, co_lats, nm_lats, ut_lats]

# Add patches to figure p with line_color=white for x and y
p.patches(x, y, line_color='white')


# Specify the name of the output file and show the result
output_file('four_corners.html')
show(p)