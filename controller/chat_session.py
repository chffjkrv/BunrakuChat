from model.llm_chain import create_llm_chain
from model.roles import mask

def start_chat_session():
    while True:
        selected_role = input(">>> Select role [N1, N2, M, G, C or exit]: ")
        if selected_role.lower() == "exit":
            break
        if selected_role in ["N1", "N2", "M", "G", "C"]:
            role = mask(selected_role)
            conversation = create_llm_chain(role)
            while True:
                user_input = input(">>> ")
                if user_input == '/chao':
                    break
                response = conversation.invoke({"question": user_input})
                print(response['text'])
        else:
            print("Invalid role. Please try again.")