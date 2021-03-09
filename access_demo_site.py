import app
import webbrowser
import requests
from bs4 import BeautifulSoup

def get_recaptcha_response(site_key):
    app.pub_key = site_key
    app.app.run()
    return app.response.get('g-recaptcha-response')

def main():
    url = 'https://www.google.com/recaptcha/api2/demo'
    session = requests.Session()
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    session.headers.update(headers)
    
    # Load page using reCAPTCHA and extract the site key
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    site_key = soup.find('div', {'data-sitekey': True})['data-sitekey'] # Get div where 'data-sitekey' attribute exists

    # Open a browser to the local Flask App to solve the reCAPTCHA
    webbrowser.open('http://localhost:5000/')
    g_recaptcha_response = get_recaptcha_response(site_key)
    print(g_recaptcha_response)

    # Use the g-recaptcha-response to submit the form
    post_captcha = session.post(url, data={'g-recaptcha-response': g_recaptcha_response})
    print(post_captcha)         # Should be 200
    print(post_captcha.text)    # Body sould contain "Verification Success... Hooray!"

if __name__ == "__main__":
    main()

