from homeassistant.helpers.entity import Entity
from .const import DOMAIN

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    if discovery_info is None: return
    client = hass.data[DOMAIN][discovery_info["entry_id"]]

    sensors = [
        FoldingSensor(client, "ETA"),
        FoldingSensor(client, "PPD"),
        FoldingSensor(client, "UNIT_PROGRESS"),
        FoldingSensor(client, "CORE")
    ]
    async_add_entities(sensors)

class FoldingSensor(Entity):
    def __init__(self, client, subject):
        self._client = client
        self._subject = subject
        self._state = None
        client.register_listener(self._handle_update)

    @property
    def name(self):
        return f"foldingathome_{self._subject.lower()}"

    @property
    def state(self):
        return self._state

    def _handle_update(self, msg):
        if "units" in msg:
            unit = msg["units"][0]
            if self._subject == "ETA":
                self._state = unit.get("eta")
            elif self._subject == "PPD":
                self._state = unit.get("ppd")
            elif self._subject == "UNIT_PROGRESS":
                self._state = unit.get("wu_progress")
        elif "core" in msg and self._subject == "CORE":
            self._state = msg["core"].get("type")
        self.schedule_update_ha_state()