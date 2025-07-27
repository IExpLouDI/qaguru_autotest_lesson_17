def test_delete_status_code(delete_request):
    assert delete_request.status_code == 204

