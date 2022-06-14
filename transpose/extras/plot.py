import plotly.graph_objects as go
import pandas as pd

from plotly.graph_objs import Figure


class PlotError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Plot:
    def __init__(self, title: str=None):
        """
        The Plot class is used to create a plotly figure.
        
        :param data: A list of response objects from the Transpose API.
        :param x: The x-axis attribute to get from each API response.
        :param y: The y-axis attribute to get from each API response.
        :param title: The title of the plot.
        :param data_points: The maximum number of data points to plot.
                            If this is < len(data), then the plot will be moving averaged.
        
        """
        self.plot = go.Figure()
        
        # a list of data addded to the plot
        self.data = []
        
        # the plotly default theme for transpose
        self.color_swatches = ['#FF5E48', '#272E33', '#59548C', '#7396BF', '#C7BBE2']
        self.transpose_theme = dict(
            layout=go.Layout(
                paper_bgcolor="#ffffff",
                plot_bgcolor="#ffffff",
                
                font_color="#000000",
                font_family="Arial",
                font_size=40,
                margin=dict(b=210, t=235, l=200, r=70),
                height=1080, 
                width=1920,
                title_x=0.14,
                title=title + "<br><sup><i style=\"font-size: 35px;\">Powered by <span style=\"color: #ff5e48\">@TransposeData</span></i></sup>",
                #yaxis_title="<span style=\"font-size: 30px\">Gas Price (Gwei)</span>",
            )
        )
        self.transpose_image = dict(
            source="https://assets.website-files.com/624c8536aa7f872fe6829dbd/624f086dd9eb0bdb9ccfa731_med.png",
            xref="paper", yref="paper",
            x=0.009, y=1.05,
            sizex=0.25, sizey=0.25,
            xanchor="right", yanchor="bottom"
        )        
        
        self.create_plot()
        
        
    def create_plot(self):
        
        # apply the transpose theme
        self.plot.update_layout(template=self.transpose_theme)
        self.plot.add_layout_image(self.transpose_image)
    
    
    def smooth_data(self, data: dict, window_size: int=10) -> dict:        
        
        # calculate the moving average of the data with a window of window_size
        data['y'] = pd.Series(data['y']).rolling(window_size).mean().dropna().tolist()
        
        # make sure x len is the same as y len
        data['x'] = data['x'][-len(data['y']):]
        
        return data
    
    
    def group_data(self, data: dict, window_size: int=10) -> dict:
        import numpy as np
        
        arr = np.array(data['y'])
        remainder = len(arr) % window_size
        if remainder == 0:
            avg = np.mean(arr.reshape(-1, window_size), axis=1)
            avg = np.repeat(avg, window_size)
            data['y'] = avg
        else:
            avg_head = np.mean(arr[:-remainder].reshape(-1, window_size), axis=1)
            avg_tail = np.mean(arr[-remainder:])
            data['y'] = np.append(avg_head, avg_tail)
                    
        # make sure x len is the same as y len
        data['x'] = data['x'][::window_size][-len(data['y']):]
        
        return data
    
    
    def add_data(self, data: dict, type: str="line", shape: str="linear", smoothing: int=1) -> None:
        """
        Adds a set of data to the plot.
        
        :param data: A dictionary of data to add to the plot.
                     MUST follow the correct format of:
                     {
                         "x": [x_data],
                         "y": [y_data],
                         "y_axis": "y_axis_name",
                         "x_axis": "x_axis_name",
                     }
        :param type: The type of plot to add.
        :param shape: LINE ONLY. The shape of the line. One of ["linear", "spline", "vh", "hv", "hvh", or "vhv"]
        :param smoothing: The number of points to smooth the data with. 
        """
            
        try:
            # format large numbers 
            if isinstance(data['x'][0], (int, float,)) or (isinstance(data['x'][0], str) and data['x'][0].isnumeric()):
                self.plot.update_layout(xaxis_tickformat="4~s")
            if isinstance(data['y'][0], (int, float,)) or (isinstance(data['y'][0], str) and data['y'][0].isnumeric()):
                self.plot.update_layout(yaxis_tickformat="4~s")
                    
            # set the axis titles
            if 'y_axis' in data: 
                self.plot.update_layout(yaxis_title = data['y_axis'])
            if 'x_axis' in data:
                self.plot.update_layout(xaxis_title = data['x_axis'])

            # generate a line charts
            if type == "line":
                
                # smooth the data if smoothing is set > 1
                if smoothing != 1:
                    data = self.smooth_data(data, smoothing)

                # add the data to the plot
                self.plot.add_trace(go.Scatter(
                    x=data['x'],
                    y=data['y'],
                    line_shape=shape,
                    line=dict(
                        color=self.color_swatches[len(self.data)],
                        width=10,
                        smoothing=1.3
                    ),
                ))

            # generate a bar chart
            elif type == "bar":
                
                 # group the data if smoothing is set > 1
                if smoothing != 1:
                    data = self.group_data(data, smoothing)
                
                # add the data to the plot
                self.plot.add_bar(
                    x=data['x'],
                    y=data['y'],
                    marker_color=self.color_swatches[len(self.data)],
                )
            
        except Exception as e:
            print(e)
            raise PlotError("Invalid data format.")

        # add the data to the list of data for coloration
        self.data.append(data)
        
        
    def show(self) -> None:
        """
        Will open the plot in a browser.
        """
        
        if len(self.data) == 0: raise PlotError("No data to show.")
        
        self.plot.show()
        
        
    def render(self, path: str, format: str="png") -> None:
        """
        Render the plot to a image file.
        
        :param path: The path to save the image to.
        """
        
        if len(self.data) == 0: raise PlotError("No data to render.")
        
        self.plot.write_image(path, format=format)
        
        
    def plotly(self) -> Figure:
        """
        Returns the internal plotly figure for the chart.
        """
        
        return self.plot