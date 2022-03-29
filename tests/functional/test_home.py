def test_home_page(client):
    '''
    GIVEN a Flask application
    WHEN  the '/' page is hit with GET method
    THEN check that 200 is returned
    '''
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Wecolme to Google Cloud DevOps!' in resp.data
