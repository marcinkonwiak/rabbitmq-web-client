def test_get(db_session, message):
    from src.message.service import get

    assert get(db_session, message.id).id == message.id
