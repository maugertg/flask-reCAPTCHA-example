# Python, Flask and reCAPTCHA tutorial

Article [written](https://hackernoon.com/python-3-flask-and-recaptcha-connection-made-easy-v7713y3o) on Hacker Noon.

Check my other stories: https://hackernoon.com/u/hbrandao


## Example Successful Output
```
python access_demo_site.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [08/Mar/2021 21:40:24] "GET / HTTP/1.1" 200 -
03AGdBq24UqY5jDV9co6ttAms0sttLOyDmQPQnNEz13kIntI0f0cEJ4dPDUrtKNJDSt4xCmIOlMdLSM6_iPEJcGVXsW2WnUhrukJUfj-vm3EmmrIEPO7EhDTznzJxWWxZKOKaFnKwab3wDSgNybR7CTc8yIXYpGkhCy8wWF1ZueyNX743BDuhKNUhbD1hqhM91_ZbcY3nztqhiewsqhpzsdH4Gm95yBaSXYL9lD-VX598KkgKUljHHMqNu_PkKGvdwT4R5tRaNPFjMc0AfuIg-xD31YHsiuiGLHQ2PMNRZqMUEnYe8rfqJkWp0uaQHHsOzDTr7PNJ0NVrqKGZ8TchSIMjYyzJS3TNAxi-ngwq-ev50tZWclT_NXeWWXXfo5IgU5Ylxrl-JgyqaG0Q8n3zbi69Q2L6li_ZA0XBbr4ygDTborv6dA7x7sfMr24ahfjUdtt3X38f76wg2JOsx90jyIcRTpbOfuPZHQ6FPJkIjgInV5mODo6Lww1Rf3ix0b9fybpxLqbFSFNwtPxnG4pMu_xpZdYCgeepUcClzlVMqedVc4hWgL6i5YFDLYk5xQlSlF3x_0DALaMMM9_gS9ht7XXhhelmQ0TUzxLf9Fph5AC_a3HrOdo51bj79cEReVmK1o6fx6X1cKsNqwaskds4YugIijr1Z4d5tUur-AtIyUgf3Rh22FDHMZjejrHbQ6h0kqK3qLHK2Bx76_FVcvQTFuOyBcrUz9TFyl0PNyUo1np_9y0pQ4J8_IzQIequLj7sF3xWUmy5VeM3EyvX4ZuA1p1KJuXsq1dfOdJVRVCXSz5s1wNrf2t5d7yYP8PF1LkM5Z8gJzG62Fz-ed_oXjos_EV227cRKhzWy33WKfmGRcjc_zchQ0HiKE9zsesAr0v3FGvv6CD3PGSVGcDGSeWa_KB-N7t0dRZ0rsgPqZMpt4Jdao0F1gsZDlCKq9H59vqOOO3RkobQj8YfVTMc-sW11YFK24RKSlkGImAoTpxx0LdF_QhvYaTloJNxHOOD0PuPWHo-TlWZN0eyMewD_YjtDqVZ7U8oqvsSGf2tvAL9cHRpWQgwi5JpMMBPcAb_OVkOLVn5BeKwgu70028QBitRzF9e6YFLL_ezoCDTWLm7rkH0k9tPWl-N1Qd0
127.0.0.1 - - [08/Mar/2021 21:40:34] "POST /success HTTP/1.1" 200 -
03AGdBq24UqY5jDV9co6ttAms0sttLOyDmQPQnNEz13kIntI0f0cEJ4dPDUrtKNJDSt4xCmIOlMdLSM6_iPEJcGVXsW2WnUhrukJUfj-vm3EmmrIEPO7EhDTznzJxWWxZKOKaFnKwab3wDSgNybR7CTc8yIXYpGkhCy8wWF1ZueyNX743BDuhKNUhbD1hqhM91_ZbcY3nztqhiewsqhpzsdH4Gm95yBaSXYL9lD-VX598KkgKUljHHMqNu_PkKGvdwT4R5tRaNPFjMc0AfuIg-xD31YHsiuiGLHQ2PMNRZqMUEnYe8rfqJkWp0uaQHHsOzDTr7PNJ0NVrqKGZ8TchSIMjYyzJS3TNAxi-ngwq-ev50tZWclT_NXeWWXXfo5IgU5Ylxrl-JgyqaG0Q8n3zbi69Q2L6li_ZA0XBbr4ygDTborv6dA7x7sfMr24ahfjUdtt3X38f76wg2JOsx90jyIcRTpbOfuPZHQ6FPJkIjgInV5mODo6Lww1Rf3ix0b9fybpxLqbFSFNwtPxnG4pMu_xpZdYCgeepUcClzlVMqedVc4hWgL6i5YFDLYk5xQlSlF3x_0DALaMMM9_gS9ht7XXhhelmQ0TUzxLf9Fph5AC_a3HrOdo51bj79cEReVmK1o6fx6X1cKsNqwaskds4YugIijr1Z4d5tUur-AtIyUgf3Rh22FDHMZjejrHbQ6h0kqK3qLHK2Bx76_FVcvQTFuOyBcrUz9TFyl0PNyUo1np_9y0pQ4J8_IzQIequLj7sF3xWUmy5VeM3EyvX4ZuA1p1KJuXsq1dfOdJVRVCXSz5s1wNrf2t5d7yYP8PF1LkM5Z8gJzG62Fz-ed_oXjos_EV227cRKhzWy33WKfmGRcjc_zchQ0HiKE9zsesAr0v3FGvv6CD3PGSVGcDGSeWa_KB-N7t0dRZ0rsgPqZMpt4Jdao0F1gsZDlCKq9H59vqOOO3RkobQj8YfVTMc-sW11YFK24RKSlkGImAoTpxx0LdF_QhvYaTloJNxHOOD0PuPWHo-TlWZN0eyMewD_YjtDqVZ7U8oqvsSGf2tvAL9cHRpWQgwi5JpMMBPcAb_OVkOLVn5BeKwgu70028QBitRzF9e6YFLL_ezoCDTWLm7rkH0k9tPWl-N1Qd0
<Response [200]>
<!DOCTYPE HTML><html dir="ltr"><head><meta http-equiv="content-type" content="text/html; charset=UTF-8"><meta name="viewport" content="width=device-width, user-scalable=yes"><title>ReCAPTCHA demo</title><link rel="stylesheet" href="https://www.gstatic.com/recaptcha/releases/4eHYAlZEVyrAlR9UNnRUmNcL/demo__ltr.css" type="text/css" nonce="D9SzAG1CokcVXba/I2X2cQ"></head><body><div class="recaptcha-success">Verification Success... Hooray!</div></body></html>
```
