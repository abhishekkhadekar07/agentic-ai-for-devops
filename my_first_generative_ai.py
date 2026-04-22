import ollama # importing package to connect with olama server

# Request
System_prompt = """
You are docker expert and you can explain things in one two lines max. you don't overthink and hallucinate and keep reasoning and u keep reason and act accordigy
below things you tell
1.you tell about errors
2.you tell about solution 
3.you tell about root cause 
"""
 
while True:
    user_input = input("enter the message:\n");
    if user_input == "exit":
        break
    response = ollama.chat(
        model="gpt-oss:120b-cloud",
        messages=[
        {'role':'system','content':System_prompt},
        {'role': 'user','content': user_input,}
        ]
    )

    print(response.message.content)