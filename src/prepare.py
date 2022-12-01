from dvc import api
import pandas as pd
from io import StringIO
import sys
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logging.info('Fetching data...')


movie_data_path = api.read('dataset/movies.csv', remote='dataset-track')
finantial_data_path = api.read('dataset/finantials.csv', remote='dataset-track')
opening_data_path = api.read('dataset/opening_gross.csv', remote='dataset-track')

movie_data = pd.read_csv(StringIO(movie_data_path))
fin_data = pd.read_csv(StringIO(finantial_data_path))
opening_data = pd.read_csv(StringIO(opening_data_path))


breakpoint()

