from scripts.query import query_chat


def test_query_chat():
    question = "What is that creature that lives in Africa and has a long neck and brown spots? Please give a one word answer"
    messages = [ {"role": "system", "content": "You are a helpful assistant. Do not use punctuation"},
    {"role": "user", "content": question} ] 
    response = query_chat(messages=messages)
    response = response.lower()
    correct_answer = "giraffe"
    assert response == correct_answer


    question = "What is the second star wars film made called? Please be laconic."
    messages = [ {"role": "system", "content": "You are a helpful assistant, concise assistant. They do not respond with any punctuation or elaboration beyond the question asked"},
    {"role": "user", "content": question} ] 
    response = query_chat(messages=messages)
    response = response.lower()
    correct_answer = "the empire strikes back"
    assert response == correct_answer

# def test_query_completion():
#     question = "What is that creature that lives in Africa and has a long neck and brown spots? Please give a one word answer"
    
#     response = query_completion(prompt=question)
#     response = response.lower()
#     correct_answer = "giraffe"
#     # print(f"response: {response}")
#     # print(f"correct answer: {correct_answer}")

#     assert response == correct_answer

    