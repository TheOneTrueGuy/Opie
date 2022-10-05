# Openai python 3 sandbox
import os
import openai
import tkinter as tk

openai.api_key = "yourkeyhere"#os.getenv("OPENAI_API_KEY")

def get_response(query):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=query,
        max_tokens=128,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    ).choices[0].text
    return response



def sendQuery_fromtextbox():
    query = query_Textbox.get(1.0, tk.END)
    response = get_response(query)
    response_Textbox.delete(1.0, tk.END)
    response_Textbox.insert(1.0, response)
    
def eval_responseCode(cod):
    eval(cod)



root=tk.Tk()
root.title("Python 3 Sandbox")
root.geometry("600x400")
#textbox=tk.Text(root,height=200,width=400)
#textbox.pack(pady=20)
button_frame=tk.Frame(root)
button_frame.pack()
query_Textbox=tk.Text(root,height=10,width=50)
query_Textbox.pack(pady=20)
response_Textbox=tk.Text(root,height=10,width=50)
response_Textbox.pack(pady=20)
button=tk.Button(button_frame,text="Send Query",command=sendQuery_fromtextbox)
button.pack(side=tk.LEFT)
button_clearquery=tk.Button(button_frame,text="Clear Query",command=lambda:query_Textbox.delete("1.0", tk.END))
button_clearquery.pack(side=tk.LEFT)
button_clearresponse=tk.Button(button_frame,text="Clear Response",command=lambda:response_Textbox.delete("1.0", tk.END))
button_clearresponse.pack(side=tk.LEFT)
button_eval=tk.Button(button_frame,text="Eval",command=lambda:eval_responseCode(response_Textbox.get(1.0, tk.END)))
button_eval.pack(side=tk.LEFT)
button_saveQuery=tk.Button(button_frame,text="Save Query",command=lambda:query_Textbox.save("query.txt"))
button_saveQuery.pack(side=tk.LEFT)
button_saveResponse=tk.Button(button_frame,text="Save Response",command=lambda:response_Textbox.save("response.py"))
button_saveResponse.pack(side=tk.LEFT)

root.mainloop()













#response = openai.Completion.create(
#  engine="davinci-codex",
#  prompt="# Python 3\n# Calculate the mean distance between an array of points and the origin\n\nimport numpy as np\n\ndef mean_distance(points):\n    return np.mean(np.sqrt(np.sum(points**2, axis=1)))\n\npoints = np.array([[0, 0], [1, 0], [2,",
#  temperature=0,
#  max_tokens=64,
#  top_p=1,
#  frequency_penalty=0,
#  presence_penalty=0
#)
