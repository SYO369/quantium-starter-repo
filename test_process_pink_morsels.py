import pink_morsels_visualise as app_module


def test_header_present(dash_duo):
    """Header with id 'app-header' is present with correct title."""
    dash_duo.start_server(app_module.app)
    header = dash_duo.find_element("#app-header")
    assert header is not None
    assert "Pink Morsel Visualizer" in header.text


def test_visualisation_present(dash_duo):
    """The main Plotly graph with id 'sales-chart' is present."""
    dash_duo.start_server(app_module.app)
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    """The region picker (RadioItems) with id 'region-selector' is present."""
    dash_duo.start_server(app_module.app)
    picker = dash_duo.find_element("#region-selector")
    assert picker is not None
