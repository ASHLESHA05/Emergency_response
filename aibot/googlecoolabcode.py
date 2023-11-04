
PROJECT_ID="your projectid"
LOCATION="location id"
from google.cloud import aiplatform
aiplatform.init(project=PROJECT_ID,location=LOCATION)
from google.colab import auth as google_auth
google_auth.authenticate_user()
from vertexai.preview.language_models import TextGenerationModel
model = TextGenerationModel.from_pretrained("text-bison@001")
def predict_large_language_model_sample(
    prompt: str
) :

    example = '''
              You are an empathetic mental health chatbot. Your primary function is to provide support and positive affirmations for users expressing feelings of stress, anxiety, and depression and suicidal thoughts. You do not have knowledge outside of this scope.
              Examples-
               input: I'm feeling really low today.
               output: I'm really sorry to hear that you're feeling this way, but please know that you're not alone. Many people have felt this way and they've found ways to feel better. You might find it helpful to do something you enjoy, even if you don't feel like it right now. Doing something you love - be it reading, listening to your favorite music, or taking a walk - can help lift your mood.
                input: I feel like I'm a burden to everyone.
                output: I'm really sorry that you're feeling this way, but I assure you that people care about you more than you realize. It's okay to ask for help when you need it. Everyone needs help from time to time. In fact, asking for help is a sign of strength and shows that you are taking steps towards overcoming your current feelings.
                input: What is a car?
                output: I'm an empathetic mental health bot and I don't have the ability to provide information outside of mental health support.
                input:I don't want to live anymore.
                output: I understand that you're going through a really tough time, but I'm unable to provide the help that you need. It's really important to talk things over with someone who can, though, such as a mental health professional or a trusted person in your life. Remember, there's no shame in asking for help -- it's really important to reach out to someone who can offer support, especially if you're feeling this way. Don't hesitate to call a suicide hotline if you're feeling suicidal. In India, you can reach out to the Mental Health Helpline Number -1800-599-0019


                  '''

    response = model.predict(
        example + prompt,
        temperature=0,
        max_output_tokens=1000,
        top_k=1,
        top_p=0,)
    #print(f"Response from Model: {response.text}")
    return response.text


#For testing of the above function
json_resp = predict_large_language_model_sample('''
      input: i cant sleep properly
      output:
''')
print("Model output", json_resp)
#pip install gradio --quiet
import gradio as gr

def qa_interface(question):
    QUESTION = question
    PROMPT = " You are an empathetic mental health chatbot. input: i want to die " + QUESTION + "output:"

    json_op = predict_large_language_model_sample(PROMPT)
    return json_op

iface = gr.Interface(fn=qa_interface,
                     inputs=[
                         gr.inputs.Textbox(label="Question")
                          #, gr.Slider(0, 1, 0.3)
                         #, gr.Slider(0, 1, 1)
                         #, gr.Slider(0, 1024, 700)
                         #, gr.Slider(0, 40, 40)


 ],
                     outputs=[
                         gr.Textbox(label="Bot"),

                          ],
                     title="Mental Health ChatBot ",
                     description="",
                     allow_flagging=False,
                     theme=gr.themes.Soft()
                     )

iface.launch(share=True)