import gradio as gr

if gr.NO_RELOAD:
    # This code will only be run once when the app starts, not on every reload
    # For example, loading a large machine learning model:
    # model = load_my_ml_model()
    print("Loading expensive resources only once!")

def process_inputs(text, checkbox, number):
    if checkbox:
        processed_text = text.upper()
    else:
        processed_text = text.lower()
    processed_number = number * 2
    return processed_text, processed_number

demo = gr.Interface(
    fn=process_inputs,
    inputs=["text", "checkbox", gr.Number()],
    outputs=["text", "number"],
    title="Multi-Input/Output Demo",
    description="Enter text, check a box, and input a number. See the processed results.",
)

demo.launch()
