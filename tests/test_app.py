# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===


"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'


"""
POST /sort-names
   Body Parameters:
      names=Joe,Alice,Zoe,Julia,Keiran  
   Expected response (200 OK):
   Alice,Joe,Julia,Kieran,Zoe
"""
def test_post_sort_names_returns_ok(web_client):
    response = web_client.post('/sort-names', 
                               data={'names':'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'


"""
POST /sort-names
   Body Parameters:
      names=Joe,Zoe,Julia,Keiran  
   Expected response (200 OK):
   Alice,Joe,Julia,Kieran,Zoe
"""
def test_post_sort_more_names_returns_ok(web_client):
    response = web_client.post('/sort-names', 
                               data={'names':'Joe,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Joe,Julia,Kieran,Zoe'


"""
# POST /sort-names
#    Parameters: none
#    Expected response (404 Invalid Request):
You didnt submit any names
"""
def test_post_sort_with_no_names(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'You didnt submit any names'

"""
POST /sort-names
   Parameters: 'JoeZoeJuliaKeiran'
   Expected response (400 Invalid Request):
Please provide a comma-separated list of names
"""
def test_post_sort_with_list_not_comma_sep(web_client):
    response = web_client.post('/sort-names', data={'names':'JoeZoeJuliaKeiran'})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Please provide a comma-separated list of names'

"""
Request:
GET /names?add=Eddie
   Parameters: add=Eddie (query parameter)
Expected response (2OO OK):
Julia, Alice, Karim, Eddie
"""
def test_get_add_eddie_name_added(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

"""
Request:
GET /names?add=Xenia
   Parameters: add=Xenia (query parameter)
Expected response (2OO OK):
Julia, Alice, Karim, Xenia
"""
def test_get_add_xenia_name_added(web_client):
    response = web_client.get('/names?add=Xenia')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Xenia'

"""
Request:
GET /names
   Parameters: none (query parameter)
Expected response (200 OK):
Julia, Alice, Karim
"""
def test_get_add_no_name_added(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim'




"""
Request:
        GET /names?add=Eddie,Leo
Parameters: 
        add=Eddie,Leo (query parameters)
Expected response (2OO OK):
        Alice, Eddie, Julia, Karim, Leo
"""
def test_get_add_two_names_added(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo'
