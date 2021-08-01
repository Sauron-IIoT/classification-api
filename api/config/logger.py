import coloredlogs, logging

# Create a logger object.
LOGGER = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')