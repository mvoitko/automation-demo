from selenium.webdriver import Chrome


def test_search():
    browser = Chrome()
    browser.get('https://duckduckgo.com')

    search_form = browser.find_element_by_id('search_form_input_homepage')
    search_form.send_keys('real python')
    search_form.submit()
    results = browser.find_elements_by_class_name('result')
    first_result_text = results[0].text
    print(first_result_text)
    browser.close()
    assert first_result_text == 'Python Tutorials - Real Python\nPython "while" Loops (Indefinite Iteration) In this tutorial, you\'ll learn about indefinite iteration using the Python while loop. You\'ll be able to construct basic and complex while loops, interrupt loop execution with break and continue, use the else clause with a while loop, and deal with infinite loops.\nhttps://realpython.com'
