from nicegui import ui

# This function will process the code entered by the user
def analyze_code(code_input):
    try:
        return code_input
    except Exception as e:
        return f"### An error occurred:\n{str(e)}"

@ui.page('/')
def index():
    with ui.column().classes('w-full items-center'):  # Centers the content horizontally and takes full width
        ui.markdown("# Code Analyzer")
        ui.markdown("Enter your Python code in the text area below and click 'Analyze' to get the code review.")

        # Use ui.textarea for multi-line input
        # classes() and props() are used for styling and responsiveness
        code_input_box = ui.textarea(
            label="Enter your Python code here:",
            placeholder="Example - Python code",
        ).classes('w-full').props('rows=15 max-rows=30 autogrow outlined show-clear-button')

        # Use ui.button for the analysis action
        analyze_button = ui.button("Analyze Code", on_click=lambda: output_box.set_value(analyze_code(code_input_box.value)))

        # Use ui.textarea for multi-line output
        output_box = ui.textarea(
            label="Analysis Result:",
            value="",  # Initial empty value
            placeholder="",  # Placeholder for output
        ).classes('w-full').props('rows=10 max-rows=20 outlined readonly autogrow')

ui.run()
