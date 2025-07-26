def test_post_status(post_request):
    assert post_request.status_code == 201