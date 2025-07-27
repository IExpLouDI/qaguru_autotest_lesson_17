def test_delete_status_code_204(delete_request):
    assert delete_request.status_code == 204

