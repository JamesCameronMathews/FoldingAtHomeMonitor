from homeassistant import config_entries
from .const import DOMAIN
from .foldingathome_client import FoldingAtHomeClient
from .config_flow import FoldingAtHomeConfigFlow

async def async_setup(hass, config):
    """Set up the Folding@Home component."""

    if DOMAIN in config:
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN, context={"source": config_entries.SOURCE_IMPORT}, data=config[DOMAIN]
            )
        )
    return True

async def async_setup_entry(hass, entry):
    host = entry.data["host"]
    port = entry.data["port"]
    ws_url = f"ws://{host}:{port}/api/websocket"
    client = FoldingAtHomeClient(ws_url)

    try:
        await client.connect()
    except Exception as e:
        raise config_entries.ConfigEntryNotReady from e

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = client

    # Load platforms
    hass.async_create_task(
        hass.helpers.discovery.async_load_platform(hass, "sensor", DOMAIN, entry.data, entry)
    )
    hass.async_create_task(
        hass.helpers.discovery.async_load_platform(hass, "switch", DOMAIN, entry.data, entry)
    )
    
    hass.loop.create_task(client.listen())
    
    return True

async def async_unload_entry(hass, entry):
    client = hass.data[DOMAIN].pop(entry.entry_id)
    await client.disconnect()
    return True
