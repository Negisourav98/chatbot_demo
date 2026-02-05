# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.services.llm_service import generate_response
#     # from app.services.retrieval_service import search_context

# router = APIRouter()

# class ChatRequest(BaseModel):
#     question: str

# @router.post("/chat")
# async def chat_bot(request: ChatRequest):


#     # context = search_context(request.question)
#     # print("Retrieved Context:", context)

#     prompt = f"""
# You are StarZopp AI Assistant.

# Answer ONLY using this context.
# If answer is not found say: I don't know.

# # Context:
# # {context}

# Question:
# {request.question}
# """

#     answer = generate_response(prompt)
#     print(answer)
#     return {"answer": answer}

# @router.post("/chat")
# async def chat_bot(request: ChatRequest):

#     prompt = f"""
# You are StarZopp AI Assistant.

# Question:
# {request.question}
# """

#     answer = generate_response(prompt)
#     print(answer)

#     return {"answer": answer}


from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.services.llm_service import generate_response
from app.services.retrieval_service import search_context

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
async def chat_bot(request: ChatRequest):

    
    # Check for greetings
    greetings = ["hi", "hello", "hey", "greetings", "hi there", "hello there"]
    if request.question.strip().lower() in greetings:
        return JSONResponse(content={"answer": "Hello! Welcome to StarZopp. How can I assist you today?"})

    context = search_context(request.question)
    print(f"DEBUG: Retrieved Context for '{request.question}':\n{context}\n---\n")

    prompt = f"""Instruct: You are StarZopp AI Assistant.
Context:
{context}

User Question: {request.question}

Answer the question simply and concisely using the Context.
- Keep it to 1-2 sentences.
- Do not add unnecessary details.

Response:"""

    # Return streaming response
    # return StreamingResponse(generate_response(prompt), media_type="text/plain")
    answer = generate_response(prompt)
    return JSONResponse({
        "answer": answer
    })
