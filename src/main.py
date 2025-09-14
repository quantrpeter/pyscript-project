def main():
    print("Initializing PyScript application...")
    # Hide loading indicator
    from js import document
    loading = document.getElementById("loading")
    if loading:
        loading.style.display = "none"
    # Draw chart after loading
    draw_chart()
    # Here you can call functions from utils.py as needed
    # For example: result = utils.some_function()

from js import document, fetch, window
from pyodide.ffi import create_proxy, to_js
import asyncio
from js import console, Chart, Object

def draw_chart():
    console.log("Drawing chart...")
    ctx = document.getElementById("myChart")
    if ctx:
        console.log("Canvas element found!")
    else:
        console.log("Canvas element not found!")
        return
    if hasattr(window, "Chart"):
        console.log("Chart.js is available!")
    else:
        console.log("Chart.js is not available!")
        return
    try:
        chart_config = {
            "type": "bar",
            "data": {
                "labels": ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
                "datasets": [{
                    "label": "Number of Votes",
                    "data": [12, 19, 3, 5, 2, 3],
                    "backgroundColor": [
                        "rgba(255, 99, 132, 0.2)",
                        "rgba(54, 162, 235, 0.2)",
                        "rgba(255, 206, 86, 0.2)",
                        "rgba(75, 192, 192, 0.2)",
                        "rgba(153, 102, 255, 0.2)",
                        "rgba(255, 159, 64, 0.2)"
                    ],
                    "borderColor": [
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 235, 1)",
                        "rgba(255, 206, 86, 1)",
                        "rgba(75, 192, 192, 1)",
                        "rgba(153, 102, 255, 1)",
                        "rgba(255, 159, 64, 1)"
                    ],
                    "borderWidth": 1
                }]
            },
            "options": {
                "scales": {
                    "y": {
                        "beginAtZero": True
                    }
                },
                "responsive": False,  # Explicitly disable responsive to match canvas size
                "animation": False   # Disable animation to ensure immediate render
            }
        }
        # Create chart with explicit object conversion
        chart = Chart.new(ctx, to_js(chart_config, dict_converter=window.Object.new))
        console.log("Chart initialized successfully!")
        # Force chart update
        chart.update()
        console.log("Chart update called!")
    except Exception as e:
        console.log(f"Error initializing chart: {str(e)}")
def on_click(event):
    input_elem = document.getElementById("myInput")
    input_elem.value = "peter"
    input_elem.classList.add("blue-border")
    # Fetch version and display in div
    async def fetch_version():
        response = await fetch("https://semiblock.hkprog.org/api/version")
        data = await response.text()
        version_div = document.getElementById("versionDiv")
        if version_div:
            version_div.innerText = f"Version: {data}"
    asyncio.ensure_future(fetch_version())

proxy = create_proxy(on_click)
document.getElementById("myButton").addEventListener("click", proxy)

if __name__ == "__main__":
    main()