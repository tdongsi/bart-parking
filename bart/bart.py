import logging
import re
import requests

import mylog

# create logger
logger = logging.getLogger("bart")


def get_permits(username, password):

    HOMEPAGE = "https://www.select-a-spot.com/bart/"
    HEADERS = {"Referer": HOMEPAGE}
    s = requests.Session()

    def download_permit(permit_id):
        params = {"id": permit_id,
                  "date": "0"}
        r = s.get("https://www.select-a-spot.com/bart/reservations/print_permit/", params=params, headers=HEADERS);
        logger.debug(r.url)
        logger.debug(r.status_code)
        logger.debug(r.text)

        params = {"id": permit_id}
        r = s.get("https://www.select-a-spot.com/bart/reservations/permit_pdf/", stream=True, params=params, headers=HEADERS);
        with open("permit"+permit_id+ ".pdf", "wb") as fd:
            for chunk in r.iter_content(1024):
                fd.write(chunk)
        logger.info("Finish downloading permit %d." % permit_id)
        pass

    def login(username, password):
        # get the home page to get CSRF token to login
        r = s.get("https://www.select-a-spot.com/bart/")
        logger.debug(r.status_code)
        logger.debug("==========")

        params = {"username": username,
                  "password": password,
                  "csrfmiddlewaretoken": r.cookies["csrftoken"],
                  "login": "Login"}
        r = s.post("https://www.select-a-spot.com/bart/users/login/", headers=HEADERS, data=params, allow_redirects=False)
        logger.debug(r.url)
        logger.debug(r.status_code)
        logger.debug("==========")

    def get_permit_ids():
        r = s.get("https://www.select-a-spot.com/bart/users/reservations/", headers=HEADERS);
        logger.debug(r.url)
        logger.debug(r.status_code)
        permits = re.findall('<td class="bold">Permit #:</td>\s*<td>(\d+)</td>', r.text)
        logger.debug(permits)
        logger.debug("==========")
        return permits

    login(username, password)
    for permit_id in get_permit_ids():
        download_permit(permit_id)
