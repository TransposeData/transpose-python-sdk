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
                margin=dict(b=150, t=225, l=170, r=70),
                height=1080, 
                width=1920,
                title_x=0.12,
                title=title + "<br><sup><i style=\"font-size: 35px;\">Powered by <span style=\"color: #ff5e48\">@TransposeData</span></i></sup>",
                #yaxis_title="<span style=\"font-size: 30px\">Gas Price (Gwei)</span>",
            )
        )
        self.transpose_image = dict(
            source="https://assets.website-files.com/624c8536aa7f872fe6829dbd/624f086dd9eb0bdb9ccfa731_med.png",
            xref="paper", yref="paper",
            x=0.01, y=1.05,
            sizex=0.2, sizey=0.2,
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
        data['x'] = data['x'][-len(data['y']):]
        
        return data
    
    def add_data(self, data: dict, smoothing: int=1) -> None:
        """
        Adds a set of data to the plot.
        
        :param data: A dictionary of data to add to the plot.
                     MUST follow the correct format of:
                     {
                         "x": [x_data],
                         "y": [y_data]
                     }
        """
        try:
            
            data = self.smooth_data(data, smoothing)
            
            # format large numbers 
            if isinstance(data['x'][0], (int, float,)) or (isinstance(data['x'][0], str) and data['x'][0].isnumeric()):
                self.plot.update_layout(xaxis_tickformat=",.4~s")
            if isinstance(data['y'][0], (int, float,)) or (isinstance(data['y'][0], str) and data['y'][0].isnumeric()):
                self.plot.update_layout(yaxis_tickformat=",.4~s")
            
            self.plot.add_trace(go.Scatter(
                x=data['x'],
                y=data['y'],
                line_shape='spline',
                line=dict(
                    color=self.color_swatches[len(self.data)],
                    width=8,
                    smoothing=1.3
                ),
            ))
            
            
        except Exception as e:
            print(e)
            raise PlotError("Invalid data format.")

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