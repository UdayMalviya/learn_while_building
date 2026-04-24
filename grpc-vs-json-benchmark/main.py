from fastapi import FastAPI, Request, Response
import orjson


from shared_logic import process_request_json

app = FastAPI()


@app.post("/json")
async def json_endpoint(request: Request):
    """
    Minimal-overhead JSON endpoint.

    Avoid:
    - Pydantic models
    - Validation overhead
    -Extra allocations
    """

    body = await request.body()

    data = orjson.loads(body)
    result = process_request_json(
        data['user'],
        data['events']
    )

    return Response(content=orjson.dumps({"result":result}), media_type='application/json')
    