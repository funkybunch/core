"""Shark IQ Constants."""

from datetime import timedelta
import logging

from homeassistant.const import Platform

LOGGER = logging.getLogger(__package__)

# Integration setup
API_TIMEOUT = 20
PLATFORMS = [Platform.VACUUM]
DOMAIN = "sharkiq"
SHARK = "Shark"
UPDATE_INTERVAL = timedelta(seconds=30)

# Region metadata
SHARKIQ_REGION_EUROPE = "europe"
SHARKIQ_REGION_ELSEWHERE = "elsewhere"
SHARKIQ_REGION_DEFAULT = SHARKIQ_REGION_ELSEWHERE
SHARKIQ_REGION_OPTIONS = [SHARKIQ_REGION_EUROPE, SHARKIQ_REGION_ELSEWHERE]

# Actions
SERVICE_CLEAN_ROOM = "clean_room"

# Attributes
ATTR_ERROR_CODE = "last_error_code"
ATTR_ERROR_MSG = "last_error_message"
ATTR_LOW_LIGHT = "low_light"
ATTR_RECHARGE_RESUME = "recharge_and_resume"
ATTR_ROOMS = "rooms"
