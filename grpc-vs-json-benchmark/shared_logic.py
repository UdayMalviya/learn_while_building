def process_request_json(user: dict, events: list[dict]) -> int:
    """
    Deterministic, CPU-bound processing function.

    This function is intentionally minimal to isolate:
    - Serialization/deserialization cost
    - Framework overhead

    It avoids:
    - I/O operations
    - Randomness
    - External dependencies
    """

    acc = 0

    acc +=user['id']

    profile = user['profile']

    # 2. Process phones 
    for phone in profile["phones"]:
        acc +=len(phone)

    # 3. Process addresses
    for addr in profile["addresses"]:
        acc +=(
            len(addr["street"]) +
            len(addr["city"]) +
            len(addr["state"]) +
            len(addr["zip"])
        )
    # 4. Process events latency
    for event in events:
        metadata = event["metadata"]
        acc += metadata['latency']
    return acc

def process_request_grpc(user, events) -> int:
    """
    Same logic as JSON version but operates directly on protobuf objects.
    Avoids unnecessary conversions.
    """
    acc = 0

    acc +=user.id

    profile = user.profile

    # 2. Process phones 
    for phone in profile.phones:
        acc +=len(phone)

    # 3. Process addresses
    for addr in profile.addresses:
        acc +=(
            len(addr.street) +
            len(addr.city) +
            len(addr.state) +
            len(addr.zip)
        )
    # 4. Process events latency
    for event in events:
        metadata = event.metadata
        acc += metadata.latency
    return acc

def test_equivilance(json_payload, proto_payload):
    json_result = process_request_json(
        json_payload['user'],
        json_payload["events"]
    )

    grpc_result = process_request_grpc(
        proto_payload.user, proto_payload.events

    )

    assert json_result == grpc_result

if __name__ == "__main__":
    pass
    
