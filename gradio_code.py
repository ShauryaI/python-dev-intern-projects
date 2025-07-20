import gradio as gr
import io
import sys

# This function will process the code entered by the user
def analyze_code(code_input):
    try:
        return "Hello"
    except Exception as e:
        return f"### An error occurred:\n{str(e)}"

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Code Analyzer")
    gr.Markdown("Enter your Python code in the text area below and click 'Analyze' to see the output or any errors.")

    with gr.Row():
        code_input_box = gr.TextArea(
            label="Enter your Python code here:",
            placeholder="Example - Python code",
            lines=15,  # Sets the initial number of visible lines
            max_lines=30,  # Sets the maximum number of lines before scrolling
            autoscroll=True,  # Automatically scrolls to the bottom for new text
            show_copy_button=True, # Allows users to easily copy the text
            elem_id="code-input",
        )

    with gr.Row():
        analyze_button = gr.Button("Analyze Code", elem_id="analyze-button")

    with gr.Row():
        output_box = gr.Textbox(
            label="Analysis Result:",
            interactive=False,  # Make the output box read-only
            lines=10,
            max_lines=20,
            autoscroll=True,
            show_copy_button=True,
            elem_id="output-box",
        )

    # Connect the button click event to the analyze_code function
    # The input to the function is the content of code_input_box
    # The output of the function will update the output_box
    analyze_button.click(
        fn=analyze_code,
        inputs=code_input_box,
        outputs=output_box
    )

# Launch the Gradio app
demo.launch(show_error=True)