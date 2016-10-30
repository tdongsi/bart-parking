from datetime import datetime
import logging
import os
import re
import requests

import mylog

# create logger
logger = logging.getLogger("bart")


def get_permits(username, password):

    HOMEPAGE = "https://www.select-a-spot.com/bart/"
    HEADERS = {"Referer": HOMEPAGE}
    FILENAME_TEMPLATE = "{folder}/permit_{id}.pdf"
    DIRNAME = datetime.now().strftime("%Y%m%d_%H%M")
    s = requests.Session()

    def login(username, password):
        # get the home page to get CSRF token to login
        r = s.get("https://www.select-a-spot.com/bart/")
        logger.debug("Status: %s", r.status_code)

        params = {"username": username,
                  "password": password,
                  "csrfmiddlewaretoken": r.cookies["csrftoken"],
                  "login": "Login"}
        r = s.post("https://www.select-a-spot.com/bart/users/login/", headers=HEADERS, data=params, allow_redirects=False)
        logger.debug(r.url)
        logger.debug(r.status_code)
        return

    def get_permit_ids():
        r = s.get("https://www.select-a-spot.com/bart/users/reservations/", headers=HEADERS);
        logger.debug(r.url)
        logger.debug(r.status_code)
        permits = re.findall('<td class="bold">Permit #:</td>\s*<td>(\d+)</td>', r.text)
        logger.debug("List of permit IDs: %s", permits)
        return permits

    def download_permit(permit_id):
        filename = FILENAME_TEMPLATE.format(folder=DIRNAME, id=permit_id)
        logger.debug("Output permit file: %s", filename)

        params = {"id": permit_id,
                  "date": "0"}
        r = s.get("https://www.select-a-spot.com/bart/reservations/print_permit/", params=params, headers=HEADERS);
        logger.debug(r.url)
        logger.debug(r.status_code)
        logger.debug(r.text)

        params = {"id": permit_id}
        r = s.get("https://www.select-a-spot.com/bart/reservations/permit_pdf/", stream=True, params=params, headers=HEADERS);
        with open(filename, "wb") as fd:
            for chunk in r.iter_content(1024):
                fd.write(chunk)
        logger.info("Finished downloading permit %s." % permit_id)
        pass

    login(username, password)
    if not os.path.exists(DIRNAME):
        try:
            os.makedirs(DIRNAME)
        except OSError as ex:
            logger.error("Cannot create folder " + DIRNAME)
            raise
    logger.info("Created folder to save permit PDF files.")

    for permit_id in get_permit_ids():
        download_permit(permit_id)
