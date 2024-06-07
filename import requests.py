import requests
import logging

# Configure logging
logging.basicConfig(filename='application_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Application URL
APPLICATION_URL = 'https://github.com'

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Application is up. Status code: {response.status_code}")
            print("Application is up")
        else:
            logging.warning(f"Application is down. Status code: {response.status_code}")
            print("Application is down")
    except requests.exceptions.RequestException as e:
        logging.error(f"Application is down. Error: {e}")
        print("Application is down")

if __name__ == "__main__":
    check_application_health(APPLICATION_URL)
    print("Application health check complete. Check application_health.log for details.")
