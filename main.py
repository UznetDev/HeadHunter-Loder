from api.vacancy_loader import VacancyLoader

import logging


def main():
    try:
        loader = VacancyLoader()
        loader.fit()
    except Exception as err:
        logging.error(err)

main()
# if __name__ == "__main___":
#     main()